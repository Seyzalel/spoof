import requests
import time
import threading
import telebot
from datetime import datetime

API_KEY = "e6962dcbc82c45bd89d9b773ad9820c0"
SYMBOL = "EUR/USD"
INTERVAL = "1min"
TELEGRAM_TOKEN = "8033138211:AAFy57nWzcCiuCbT0u0hRHRhQIz_kmoipc0"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
subscribers = set()
running = False

def get_candle():
    url = f"https://api.twelvedata.com/time_series?symbol={SYMBOL}&interval={INTERVAL}&apikey={API_KEY}&outputsize=2"
    r = requests.get(url)
    d = r.json()
    c = d["values"][0]
    return {
        "datetime": c["datetime"],
        "open": float(c["open"]),
        "high": float(c["high"]),
        "low": float(c["low"]),
        "close": float(c["close"]),
    }

def calculate_ip(c):
    corpo = abs(c["close"] - c["open"])
    sup = c["high"] - max(c["close"], c["open"])
    inf = min(c["close"], c["open"]) - c["low"]
    pavios = sup + inf
    ip = corpo / pavios if pavios > 0 else 999
    return round(ip, 2), corpo, pavios

def detectar_tendencia(c):
    return "CALL" if c["close"] > c["open"] else "PUT"

def gerar_sinal(ip, corpo, pavios, direcao):
    if ip >= 2.0 and corpo > pavios:
        return f"CONTINUIDADE EXTREMA – ENTRADA: {direcao} (1 MIN)"
    if ip < 0.6 and pavios > corpo:
        return f"REVERSÃO PRECISA – ENTRADA: {'PUT' if direcao == 'CALL' else 'CALL'} (1 MIN)"
    return "SEM SINAL CLARO – AGUARDE"

def formatar_msg(c, ip, corpo, pavios, direcao, sinal):
    return (
        f"SINAL DETECTADO [{datetime.now().strftime('%H:%M:%S')}]\n"
        f"Ativo: {SYMBOL}\n"
        f"Candle: {c['datetime']}\n"
        f"Abertura: {c['open']} | Fechamento: {c['close']}\n"
        f"Máxima: {c['high']} | Mínima: {c['low']}\n"
        f"Corpo: {round(corpo, 5)} | Pavios: {round(pavios, 5)}\n"
        f"Pressão (IP): {ip}\n"
        f"Tendência: {direcao}\n"
        f"\n>> {sinal} <<"
    )

def bot_worker():
    global running
    ultima = None
    while running:
        c = get_candle()
        if c and c != ultima:
            ip, corpo, pavios = calculate_ip(c)
            d = detectar_tendencia(c)
            s = gerar_sinal(ip, corpo, pavios, d)
            msg = formatar_msg(c, ip, corpo, pavios, d, s)
            for u in subscribers:
                bot.send_message(u, msg)
            ultima = c
        time.sleep(10)

@bot.message_handler(commands=["start"])
def start(message):
    global running
    user_id = message.chat.id
    subscribers.add(user_id)
    bot.send_message(user_id, "Sinais ativados. Você receberá entradas 100% filtradas e lucrativas.")
    if not running:
        running = True
        threading.Thread(target=bot_worker).start()

@bot.message_handler(commands=["stop"])
def stop(message):
    global running
    running = False
    bot.send_message(message.chat.id, "Bot pausado. Use /start para reativar.")

@bot.message_handler(commands=["status"])
def status(message):
    estado = "ativo" if running else "pausado"
    bot.send_message(message.chat.id, f"O bot está {estado}.")

bot.infinity_polling()