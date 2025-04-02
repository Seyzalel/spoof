import requests
import time
import threading
import telebot
from datetime import datetime

API_KEY = "ba12a79bed074ef5a1ba2deb6bd5a710"
SYMBOL = "EUR/USD"
INTERVAL = "1min"
TELEGRAM_TOKEN = "8033138211:AAFy57nWzcCiuCbT0u0hRHRhQIz_kmoipc0"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
subscribers = set()
running = False

def get_candle():
    url = f"https://api.twelvedata.com/time_series?symbol={SYMBOL}&interval={INTERVAL}&apikey={API_KEY}&outputsize=2"
    response = requests.get(url)
    data = response.json()
    candles = data["values"]
    latest = candles[0]
    return {
        "datetime": latest["datetime"],
        "open": float(latest["open"]),
        "high": float(latest["high"]),
        "low": float(latest["low"]),
        "close": float(latest["close"]),
    }

def calculate_ip(candle):
    corpo = abs(candle["close"] - candle["open"])
    pavio_sup = candle["high"] - max(candle["close"], candle["open"])
    pavio_inf = min(candle["close"], candle["open"]) - candle["low"]
    pavios = pavio_sup + pavio_inf
    ip = corpo / pavios if pavios > 0 else 999
    return round(ip, 2), corpo, pavios

def detectar_tendencia(candle):
    return "CALL" if candle["close"] > candle["open"] else "PUT"

def gerar_sinal(ip, corpo, pavios, direcao):
    if ip >= 2.2 and corpo > pavios and corpo > 0.0005:
        return f"ENTRADA CONFIÁVEL – {direcao} (Expiração 10s)"
    if ip < 0.6 and pavios > corpo and pavios > 0.0005:
        return f"REVERSÃO DETECTADA – {'PUT' if direcao == 'CALL' else 'CALL'} (Expiração 10s)"
    return "SEM ENTRADA – Mercado indefinido"

def formatar_mensagem(candle, ip, corpo, pavios, direcao, sinal):
    return (
        f"**SINAL GERADO** [{datetime.now().strftime('%H:%M:%S')}]\n"
        f"Ativo: `{SYMBOL}`\n"
        f"Data/Hora: `{candle['datetime']}`\n"
        f"Abertura: `{candle['open']}` | Fechamento: `{candle['close']}`\n"
        f"Máxima: `{candle['high']}` | Mínima: `{candle['low']}`\n"
        f"Corpo: `{round(corpo, 5)}` | Pavios: `{round(pavios, 5)}`\n"
        f"Pressão: `{ip}` | Tendência: `{direcao}`\n"
        f"\n**>> {sinal} <<**"
    )

def bot_worker():
    global running
    ultimo_candle = None
    while running:
        candle = get_candle()
        if candle and candle != ultimo_candle:
            ip, corpo, pavios = calculate_ip(candle)
            direcao = detectar_tendencia(candle)
            sinal = gerar_sinal(ip, corpo, pavios, direcao)
            if "ENTRADA" in sinal:
                mensagem = formatar_mensagem(candle, ip, corpo, pavios, direcao, sinal)
                for user_id in subscribers:
                    bot.send_message(user_id, mensagem, parse_mode="Markdown")
            ultimo_candle = candle
        time.sleep(10)

@bot.message_handler(commands=["start"])
def start(message):
    global running
    user_id = message.chat.id
    subscribers.add(user_id)
    bot.reply_to(message, "Bot de sinais ativo! Você receberá entradas confiáveis automaticamente.")
    if not running:
        running = True
        threading.Thread(target=bot_worker).start()

@bot.message_handler(commands=["stop"])
def stop(message):
    global running
    running = False
    bot.reply_to(message, "Bot pausado. Use /start para reativar.")

@bot.message_handler(commands=["status"])
def status(message):
    msg = "Bot ativo e monitorando o mercado!" if running else "Bot está pausado. Use /start para ativar."
    bot.reply_to(message, msg)

bot.infinity_polling()