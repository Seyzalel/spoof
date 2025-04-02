import requests
import time
import threading
import telebot
from datetime import datetime
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

API_KEY = "e6962dcbc82c45bd89d9b773ad9820c0"
SYMBOL = "EUR/USD"
INTERVAL = "1min"
TELEGRAM_TOKEN = "8033138211:AAFy57nWzcCiuCbT0u0hRHRhQIz_kmoipc0"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
subscribers = set()
running = {}
win = {}
loss = {}
stop_win = 5
stop_loss = 3
ultima_analise = {}

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
        return f"ENTRADA SEGURA – {direcao} (Expiração 1min)"
    if ip < 0.7 and pavios > corpo:
        return f"REVERSÃO CLÁSSICA – {'PUT' if direcao == 'CALL' else 'CALL'} (Expiração 1min)"
    return "SEM ENTRADA SEGURA NO MOMENTO"

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
        f"ANÁLISE [{datetime.now().strftime('%H:%M:%S')}]\n"
        f"Ativo: {SYMBOL}\n"
        f"Candle: {c['datetime']}\n"
        f"O: {c['open']} | C: {c['close']} | H: {c['high']} | L: {c['low']}\n"
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

def painel():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(KeyboardButton("✅ SINAL AGORA"), KeyboardButton("📊 STATUS"), KeyboardButton("♻️ RESET"))
    return kb

def analisar(user_id):
    c = get_candle()
    if not c or c['datetime'] == ultima_analise.get(user_id): return
    ip, corpo, pavios = calculate_ip(c)
    d = detectar_tendencia(c)
    s = gerar_sinal(ip, corpo, pavios, d)
    msg = formatar_msg(c, ip, corpo, pavios, d, s, user_id)
    bot.send_message(user_id, msg)
    ultima_analise[user_id] = c['datetime']

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.chat.id
    subscribers.add(user_id)
    running[user_id] = True
    win[user_id] = 0
    loss[user_id] = 0
    bot.send_message(user_id,
        "Bem-vindo ao BOT DE SINAIS PREMIUM (Expiração 1min)\n\n"
        "Este bot analisa o par EUR/USD a cada minuto e envia sinais somente quando a entrada é extremamente segura.\n\n"
        "Comandos disponíveis:\n"
        "✅ SINAL AGORA → pede o sinal do candle atual\n"
        "📊 STATUS → mostra seu desempenho\n"
        "♻️ RESET → zera suas estatísticas\n\n"
        "Resultado da entrada:\n"
        "Digite: `win` ou `loss` após a operação.\n\n"
        "Análises automáticas ativas. Apenas entradas com confiança extrema serão enviadas.",
        reply_markup=painel())

@bot.message_handler(func=lambda m: m.text == "✅ SINAL AGORA")
def manual_signal(message):
    analisar(message.chat.id)

@bot.message_handler(func=lambda m: m.text == "📊 STATUS")
def status(message):
    user_id = message.chat.id
    barra = gerar_barra(user_id)
    ativo = running.get(user_id, False)
    estado = "Ativo" if ativo else "Pausado"
    bot.send_message(user_id, f"Bot: {estado}\n{barra}")

@bot.message_handler(func=lambda m: m.text == "♻️ RESET")
def resetar(message):
    user_id = message.chat.id
    win[user_id] = 0
    loss[user_id] = 0
    bot.send_message(user_id, "Estatísticas zeradas com sucesso.")

@bot.message_handler(func=lambda m: m.text.lower() in ["win", "loss"])
def resultado(message):
    registrar_resultado(message.text, message.chat.id)
    bot.send_message(message.chat.id, "Resultado registrado.")

def automatico(user_id):
    ultima = None
    while running.get(user_id, False):
        try:
            c = get_candle()
            if c and c != ultima:
                ip, corpo, pavios = calculate_ip(c)
                d = detectar_tendencia(c)
                s = gerar_sinal(ip, corpo, pavios, d)
                if "ENTRADA" in s:
                    msg = formatar_msg(c, ip, corpo, pavios, d, s, user_id)
                    bot.send_message(user_id, msg)
                ultima = c
        except:
            pass
        time.sleep(60)

@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    resetar(message)

@bot.message_handler(commands=["status"])
def cmd_status(message):
    status(message)

@bot.message_handler(commands=["stop"])
def stop(message):
    user_id = message.chat.id
    running[user_id] = False
    bot.send_message(user_id, "Bot pausado com sucesso.")

@bot.message_handler(commands=["signal"])
def cmd_signal(message):
    manual_signal(message)

@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.send_message(message.chat.id, "Use os botões abaixo ou envie /start para recomeçar.", reply_markup=painel())

def iniciar_automatico(user_id):
    threading.Thread(target=automatico, args=(user_id,)).start()

@bot.message_handler(commands=["start"])
def full_start(message):
    start(message)
    iniciar_automatico(message.chat.id)

bot.infinity_polling()