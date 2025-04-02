import requests
import time
import threading
import telebot
from datetime import datetime

API_KEY = "e6962dcbc82c45bd89d9b773ad9820c0"
SYMBOL = "USD/BRL"
INTERVAL = "1min"
TELEGRAM_TOKEN = "8033138211:AAFy57nWzcCiuCbT0u0hRHRhQIz_kmoipc0"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
subscribers = set()
running = False
win = 0
loss = 0
stop_win = 5
stop_loss = 3

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
        return f"EXPLOSÃO DIRECIONAL – ENTRADA: {direcao} (Expiração 10s)"
    if ip < 0.7 and pavios > corpo:
        return f"REVERSÃO TÁTICA – ENTRADA: {'PUT' if direcao == 'CALL' else 'CALL'} (Expiração 10s)"
    return "SEM SINAL – MERCADO NEUTRO"

def formatar_msg(c, ip, corpo, pavios, direcao, sinal):
    barra = gerar_barra_lucro()
    return (
        f"SINAL [{datetime.now().strftime('%H:%M:%S')}]\n"
        f"Ativo: {SYMBOL}\n"
        f"Candle: {c['datetime']}\n"
        f"Abertura: {c['open']} | Fechamento: {c['close']}\n"
        f"Alta: {c['high']} | Baixa: {c['low']}\n"
        f"Corpo: {round(corpo, 5)} | Pavios: {round(pavios, 5)} | IP: {ip}\n"
        f"Tendência: {direcao}\n\n>> {sinal} <<\n\n{barra}"
    )

def gerar_barra_lucro():
    total = win + loss if (win + loss) > 0 else 1
    taxa = int((win / total) * 10)
    barra = "█" * taxa + "-" * (10 - taxa)
    return f"Vitórias: {win} | Derrotas: {loss}\nPrecisão: [{barra}] {int((win / total) * 100)}%"

def registrar_resultado(texto):
    global win, loss
    if "win" in texto.lower():
        win += 1
    elif "loss" in texto.lower():
        loss += 1

def bot_worker():
    global running
    ultima = None
    while running:
        if win >= stop_win or loss >= stop_loss:
            for u in subscribers:
                bot.send_message(u, f"Gestão de risco atingida.\nVitórias: {win} | Derrotas: {loss}")
            running = False
            break
        c = get_candle()
        if c and c != ultima:
            ip, corpo, pavios = calculate_ip(c)
            d = detectar_tendencia(c)
            s = gerar_sinal(ip, corpo, pavios, d)
            msg = formatar_msg(c, ip, corpo, pavios, d, s)
            if "ENTRADA" in s:
                for u in subscribers:
                    bot.send_message(u, msg)
            ultima = c
        time.sleep(10)

@bot.message_handler(commands=["start"])
def start(message):
    global running
    user_id = message.chat.id
    subscribers.add(user_id)
    bot.send_message(user_id, "Bot ativo. Sinais com expiração de 10 segundos.")
    if not running:
        running = True
        threading.Thread(target=bot_worker).start()

@bot.message_handler(commands=["stop"])
def stop(message):
    global running
    running = False
    bot.send_message(message.chat.id, "Bot pausado.")

@bot.message_handler(commands=["status"])
def status(message):
    estado = "ativo" if running else "pausado"
    barra = gerar_barra_lucro()
    bot.send_message(message.chat.id, f"Status: {estado}\n{barra}")

@bot.message_handler(commands=["reset"])
def reset(message):
    global win, loss
    win = 0
    loss = 0
    bot.send_message(message.chat.id, "Estatísticas reiniciadas.")

@bot.message_handler(func=lambda m: True)
def monitorar_resultado(message):
    registrar_resultado(message.text)

bot.infinity_polling()