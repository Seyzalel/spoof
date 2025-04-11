import time
import random
import os
import sys
from datetime import datetime, timedelta

plataformas = [
    "1. Kiwify (recomendado)",
    "2. Kirvano",
    "3. Braip",
    "4. Eduzz",
    "5. Hotmart",
    "6. Monetizze"
]

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def animacao(texto, duracao=1.4):
    etapas = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    for _ in range(12):
        for etapa in etapas:
            sys.stdout.write(f'\r{texto} {etapa}')
            sys.stdout.flush()
            time.sleep(duracao / len(etapas))
    print()

def mostrar_vendas_passadas():
    print("\nAnalisando histórico de vendas recentes...\n")
    vendas = []
    agora = datetime.now()
    for i in range(9):
        atraso = random.randint(120, 180)
        horario = agora - timedelta(minutes=atraso - (i * 3))
        vendas.append(horario.strftime("%H:%M:%S"))

    for idx, hora in enumerate(vendas, 1):
        print(f"[{hora}] Venda {idx} confirmada — produto: Sistema Viral — comissão: R$ 15,32")
        time.sleep(0.25)

    print("\nResumo:")
    print(f"Total de vendas encontradas: 9")
    print(f"Valor total recebido: R$ 137,90")
    print(f"Produto monitorado: Sistema Viral")
    print("-" * 50)
    time.sleep(1)

def evento_ao_vivo():
    tipo = random.choices(["clique", "lead", "venda"], weights=[60, 30, 10])[0]
    valor = round(random.uniform(37.00, 197.00), 2)
    hora = time.strftime('%H:%M:%S')
    if tipo == "clique":
        print(f"[{hora}] Novo clique registrado.")
    elif tipo == "lead":
        print(f"[{hora}] Lead identificado — usuário engajado.")
    elif tipo == "venda":
        print(f"[{hora}] Venda detectada — comissão estimada: R$ {valor:.2f} — produto: Sistema Viral")

def monitorar_ao_vivo():
    print("\nIniciando monitoramento em tempo real...\n(Pressione CTRL+C para sair)\n")
    while True:
        evento_ao_vivo()
        time.sleep(random.uniform(1.5, 3.5))

def main():
    limpar()
    print("──────────────────────────────────────────────────────")
    print("         painel inteligente de vendas — 2025")
    print("──────────────────────────────────────────────────────")
    print("\nEscolha a plataforma para análise:\n")
    for plataforma in plataformas:
        print(plataforma)

    escolha = input("\nDigite o número da plataforma: ").strip()
    if escolha not in [str(i) for i in range(1, len(plataformas) + 1)]:
        print("\nPlataforma inválida. Encerrando...\n")
        return

    plataforma_nome = plataformas[int(escolha) - 1][3:]
    print(f"\nPlataforma selecionada: {plataforma_nome}")

    url = input("Cole seu link de afiliado: ").strip()
    if not url.startswith("http"):
        print("\nURL inválida. Encerrando...\n")
        return

    print("\nAnalisando seu link...\n")
    animacao("Validando rastreamento")
    animacao("Extraindo conversões")
    mostrar_vendas_passadas()
    animacao("Ativando painel em tempo real")
    monitorar_ao_vivo()

if __name__ == "__main__":
    main()
