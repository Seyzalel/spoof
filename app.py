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
running = {}
win = {}
loss = {}
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

def gerar_barra(user_id):
    w = win.get(user_id, 0)
    l = loss.get(user_id, 0)
    total = w + l if w + l > 0 else 1
    taxa = int((w / total) * 10)
    barra = "█" * taxa + "-" * (10 - taxa)
    return f"Vitórias: {w} | Derrotas: {l}\nPrecisão: [{barra}] {int((w / total) * 100)}%"

def formatar_msg(c, ip, corpo, pavios, direcao, sinal, user_id):
    barra = gerar_barra(user_id)
    return (
        f"SINAL [{datetime.now().strftime('%H:%M:%S')}]\n"
        f"Ativo: {SYMBOL}\n"
        f"Candle: {c['datetime']}\n"
        f"Abertura: {c['open']} | Fechamento: {c['close']}\n"
        f"Alta: {c['high']} | Baixa: {c['low']}\n"
        f"Corpo: {round(corpo, 5)} | Pavios: {round(pavios, 5)} | IP: {ip}\n"
        f"Tendência: {direcao}\n\n>> {sinal} <<\n\n{barra}"
    )

def registrar_resultado(texto, user_id):
    if user_id not in win: win[user_id] = 0
    if user_id not in loss: loss[user_id] = 0
    if "win" in texto.lower():
        win[user_id] += 1
    elif "loss" in texto.lower():
        loss[user_id] += 1

def bot_worker(user_id):
    ultima = None
    while running.get(user_id, False):
        if win.get(user_id, 0) >= stop_win or loss.get(user_id, 0) >= stop_loss:
            bot.send_message(user_id, f"Gestão atingida.\nVitórias: {win.get(user_id, 0)} | Derrotas: {loss.get(user_id, 0)}")
            running[user_id] = False
            break
        try:
            c = get_candle()
            if c and c != ultima:
                ip, corpo, pavios = calculate_ip(c)
                d = detectar_tendencia(c)
                s = gerar_sinal(ip, corpo, pavios, d)
                msg = formatar_msg(c, ip, corpo, pavios, d, s, user_id)
                if "ENTRADA" in s:
                    bot.send_message(user_id, msg)
                ultima = c
        except:
            pass
        time.sleep(10)

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.chat.id
    subscribers.add(user_id)
    running[user_id] = True
    win[user_id] = 0
    loss[user_id] = 0
    bot.send_message(user_id, "Bot ativado. Sinais com expiração de 10 segundos.")
    threading.Thread(target=bot_worker, args=(user_id,)).start()

@bot.message_handler(commands=["stop"])
def stop(message):
    user_id = message.chat.id
    running[user_id] = False
    bot.send_message(user_id, "Bot pausado.")

@bot.message_handler(commands=["status"])
def status(message):
    user_id = message.chat.id
    barra = gerar_barra(user_id)
    ativo = running.get(user_id, False)
    estado = "ativo" if ativo else "pausado"
    bot.send_message(user_id, f"Status: {estado}\n{barra}")

@bot.message_handler(commands=["reset"])
def reset(message):
    user_id = message.chat.id
    win[user_id] = 0
    loss[user_id] = 0
    bot.send_message(user_id, "Estatísticas zeradas.")

@bot.message_handler(func=lambda m: True)
def resultado_manual(message):
    user_id = message.chat.id
    registrar_resultado(message.text, user_id)

bot.infinity_polling()