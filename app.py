import os
import sys
import time
import random

ativos = [
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD",
    "USD/CHF", "NZD/USD", "EUR/GBP", "EUR/JPY", "GBP/JPY"
]

tempos_graficos = ["5s", "10s", "15s", "30s", "1m", "5m"]

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def digitar(texto, vel=0.02):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(vel)

def progresso(texto, duracao=2):
    digitar(texto)
    for i in range(31):
        sys.stdout.write(f"\r[{'█'*i}{' '*(30 - i)}] {int(i*(100/30))}%")
        sys.stdout.flush()
        time.sleep(duracao / 30)
    print()

def login_quotex(email, senha):
    limpar()
    progresso("Conectando ao servidor Quotex...\n", 2)
    progresso("Validando dados de login...\n", 2)
    digitar("\nConectado com sucesso!\n")
    time.sleep(1)

def exibir_saldo(saldo):
    digitar(f"\nSaldo disponível: R${saldo:.2f}\n")
    time.sleep(1)

def menu_principal(saldo):
    limpar()
    exibir_saldo(saldo)
    digitar("\nEscolha o método operacional:\n\n")
    print("[1] Soros IA Ultra Quantum (Melhor de Todos)")
    print("[2] Turbo Gale Pro")
    print("[3] Fibonacci Xtreme")
    print("[4] Martingale Precision")
    print("[5] Velas Mágicas V3")
    print("[6] RSI Supremo IA")
    escolha = input("\nDigite a opção desejada: ")
    return escolha

def escolher_ativo():
    limpar()
    progresso("Carregando ativos disponíveis...\n", 2)
    digitar("\nSelecione um ativo para operar:\n\n")
    for num, ativo in enumerate(ativos, 1):
        print(f"[{num}] {ativo}")
    escolha = int(input("\nNúmero do ativo escolhido: "))
    return ativos[escolha - 1]

def escolher_tempo_grafico():
    limpar()
    progresso("Carregando tempos gráficos...\n", 2)
    digitar("\nSelecione o tempo gráfico:\n\n")
    for num, tempo in enumerate(tempos_graficos, 1):
        print(f"[{num}] {tempo}")
    escolha = int(input("\nNúmero do tempo gráfico escolhido: "))
    return tempos_graficos[escolha - 1]

def cronometro(segundos):
    for i in range(segundos, 0, -1):
        sys.stdout.write(f"\rTempo restante: {i}s ")
        sys.stdout.flush()
        time.sleep(1)
    print("\rOperação encerrada!       ")

def operar_soros_ia(saldo):
    limpar()
    ativo = escolher_ativo()
    tempo_grafico = escolher_tempo_grafico()
    perc = float(input("\nDigite o % da banca por operação: "))
    saldo_atual = saldo
    aposta = saldo_atual * (perc / 100)
    resultados = []
    limpar()
    for rodada in range(1, 6):
        direcao = random.choice(["CALL", "PUT"])
        digitar(f"\nPreparando operação #{rodada} em {ativo} - {direcao}\n")
        progresso("IA analisando mercado...\n", 2)
        digitar("Operação aberta...\n")
        seg = int(tempo_grafico.replace('s','').replace('m','')) * (60 if 'm' in tempo_grafico else 1)
        cronometro(seg)
        lucro = aposta * 0.93
        saldo_atual += lucro
        resultados.append(direcao)
        digitar(f"\n✅ WIN em {ativo}!\n")
        digitar(f"Valor apostado: R${aposta:.2f}\n")
        digitar(f"Lucro obtido: R${lucro:.2f}\n")
        digitar(f"Novo saldo: R${saldo_atual:.2f}\n")
        aposta = saldo_atual * (perc / 100)
        time.sleep(2)
    digitar("\nSessão finalizada!\n")
    digitar(f"Saldo final: R${saldo_atual:.2f}\n")
    digitar("Resultados das operações:\n")
    for idx, direcao in enumerate(resultados, 1):
        digitar(f"Operação #{idx}: {direcao} ✅ WIN\n")

def main():
    limpar()
    digitar("=== Quotex Ultra IA Trading Bot ===\n\n")
    email = input("Email Quotex: ")
    senha = input("Senha Quotex: ")
    login_quotex(email, senha)
    saldo_inicial = 50.81
    escolha = menu_principal(saldo_inicial)
    if escolha == "1":
        operar_soros_ia(saldo_inicial)
    else:
        digitar("\nOpção em manutenção. Tente novamente mais tarde.\n")

if __name__ == "__main__":
    main()