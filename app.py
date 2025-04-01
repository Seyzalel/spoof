from quotexapi.stable import Quotex
import time
from datetime import datetime

q = Quotex(email="seyzalel@gmail.com", password="Sey17zalel17@$")
q.connect()
q.change_balance("demo")

def get_last_candle(pair, timeframe):
    q.get_candles(pair, timeframe, 3)
    while q.candles == []:
        time.sleep(0.5)
    return q.candles[-1], q.candles[-2], q.candles[-3]

def entrada_perfeita(segundos):
    return 5 <= segundos <= 20

def operacao_sniper():
    par = "EURUSD-OTC"
    valor = 50
    tempo_expiracao = 1

    vela_m5_atual, vela_m5_anterior, _ = get_last_candle(par, 300)
    if vela_m5_anterior['open'] < vela_m5_anterior['close']:
        direcao = "call"
    elif vela_m5_anterior['open'] > vela_m5_anterior['close']:
        direcao = "put"
    else:
        return

    vela_m1_atual, vela_m1_anterior, _ = get_last_candle(par, 60)
    agora = datetime.utcnow().second

    if direcao == "call" and vela_m1_atual['close'] > vela_m1_atual['open'] and entrada_perfeita(agora):
        q.buy(valor, par, "call", tempo_expiracao)
    elif direcao == "put" and vela_m1_atual['close'] < vela_m1_atual['open'] and entrada_perfeita(agora):
        q.buy(valor, par, "put", tempo_expiracao)

while True:
    operacao_sniper()
    time.sleep(10)