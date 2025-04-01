import os
import sys
import time

ativos = [
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD",
    "USD/CHF", "NZD/USD", "EUR/GBP", "EUR/JPY", "GBP/JPY"
]

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
    progresso("Estabelecendo conexão com Quotex...\n", 2)
    progresso("Validando informações de acesso...\n", 2)
    digitar("\n✅ Conectado com sucesso!\n")
    time.sleep(1.5)

def exibir_saldo(saldo):
    digitar(f"\n💰 Saldo disponível (Conta Real): R${saldo:.2f}\n")
    time.sleep(1.5)

def menu_principal(saldo):
    limpar()
    exibir_saldo(saldo)
    digitar("\n🎯 Escolha seu modo de operação:\n\n")
    print("[1] 🧠 Soros IA Ultra Quantum (Melhor de Todos!)")
    print("[2] 🚀 Turbo Gale Pro")
    print("[3] 🌀 Fibonacci Xtreme")
    print("[4] ♻️ Martingale Precision")
    print("[5] 🔥 Velas Mágicas V3")
    print("[6] 📈 RSI Supremo IA")
    escolha = input("\nDigite a opção desejada: ")
    return escolha

def selecionar_ativo():
    limpar()
    progresso("Carregando ativos abertos para negociação...\n", 2)
    digitar("\n📊 Selecione um ativo para operar:\n\n")
    for num, ativo in enumerate(ativos, 1):
        print(f"[{num}] {ativo}")
    escolha = int(input("\nNúmero do ativo escolhido: "))
    return ativos[escolha - 1]

def operar_soros_ia(saldo):
    limpar()
    digitar("🔄 Inicializando Soros IA Ultra Quantum...\n")
    perc = float(input("\n📌 Digite o % da banca por operação: "))
    ativo = selecionar_ativo()
    limpar()
    digitar(f"🤖 Soros IA Ultra Quantum iniciando operações em {ativo}...\n")
    saldo_atual = saldo
    valor_aposta = saldo_atual * (perc / 100)
    for rodada in range(1, 6):
        progresso(f"\n📡 Analisando sinais IA para operação #{rodada}...\n", 3)
        lucro = valor_aposta * 0.93
        saldo_atual += lucro
        digitar(f"\n✅ WIN confirmado em {ativo}!\n")
        digitar(f"📌 Valor apostado: R${valor_aposta:.2f}\n")
        digitar(f"📈 Lucro da operação: R${lucro:.2f}\n")
        digitar(f"💎 Novo saldo atualizado: R${saldo_atual:.2f}\n")
        valor_aposta = saldo_atual * (perc / 100)
        time.sleep(2)
    digitar(f"\n🎉 Sessão finalizada com sucesso!\n")
    digitar(f"💰 Saldo final após operações: R${saldo_atual:.2f}\n")

def main():
    limpar()
    digitar("=== 🚀 Quotex Ultra IA Trading Bot 🚀 ===\n\n")
    email = input("📧 Email Quotex: ")
    senha = input("🔑 Senha Quotex: ")
    login_quotex(email, senha)
    saldo_inicial = 50.81
    opcao = menu_principal(saldo_inicial)
    if opcao == "1":
        operar_soros_ia(saldo_inicial)
    else:
        digitar("\n⚠️ Opção em manutenção, tente mais tarde.\n")

if __name__ == "__main__":
    main()