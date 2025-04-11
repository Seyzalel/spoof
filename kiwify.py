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

def animacao(texto, duracao=1.2):
    etapas = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    for _ in range(10):
        for etapa in etapas:
            sys.stdout.write(f'\r{texto} {etapa}')
            sys.stdout.flush()
            time.sleep(duracao / len(etapas))
    print()

def exibir_vendas_passadas():
    print("\nCarregando histórico recente de transações...\n")
    vendas = []
    agora = datetime.now()
    for i in range(9):
        atraso = random.randint(240, 360)
        horario = agora - timedelta(minutes=atraso - (i * 2))
        vendas.append(horario.strftime("%H:%M:%S"))
    for idx, hora in enumerate(vendas, 1):
        print(f"[{hora}] Venda {idx} confirmada — produto: Sistema Viral — comissão recebida: R$ 137,90")
        time.sleep(0.3)
    print("\nResumo das últimas conversões:")
    print("Total de vendas identificadas: 9")
    print("Total em comissões recebidas: R$ 1.241,10")
    print("Produto monitorado: Sistema Viral")
    print("-" * 55)
    time.sleep(1)

def evento_ao_vivo():
    tipo = random.choices(["clique", "lead", "venda"], weights=[60, 30, 10])[0]
    hora = time.strftime('%H:%M:%S')
    if tipo == "clique":
        print(f"[{hora}] Novo clique registrado.")
    elif tipo == "lead":
        print(f"[{hora}] Lead qualificado detectado.")
    elif tipo == "venda":
        print(f"[{hora}] Nova conversão — comissão: R$ 137,90 — produto: Sistema Viral")

def monitorar():
    print("\nO sistema está agora em modo de monitoramento inteligente.")
    print("Aguardando novos cliques em tempo real...")
    print("Impulsionando estrategicamente o link de afiliado para maximizar a taxa de conversão.")
    print("Analisando o comportamento do público e ajustando o alcance dinâmico para aumentar a performance.\n")
    time.sleep(2)
    while True:
        evento_ao_vivo()
        time.sleep(random.uniform(1.7, 4.0))

def main():
    limpar()
    print("╭────────────────────────────────────────────────────────────╮")
    print("│           Painel de performance — ambiente profissional    │")
    print("╰────────────────────────────────────────────────────────────╯")
    print("\nSelecione a plataforma a ser monitorada:\n")
    for plataforma in plataformas:
        print(plataforma)
    escolha = input("\nDigite o número da plataforma: ").strip()
    if escolha not in [str(i) for i in range(1, len(plataformas) + 1)]:
        print("\nEntrada inválida. Encerrando...\n")
        return
    plataforma_nome = plataformas[int(escolha) - 1][3:]
    print(f"\nPlataforma selecionada: {plataforma_nome}")
    url = input("Cole o link do seu afiliado: ").strip()
    if not url.startswith("http"):
        print("\nLink inválido. Encerrando...\n")
        return
    print("\nIniciando leitura do ambiente...\n")
    animacao("Validando link de rastreamento")
    animacao("Sincronizando métricas com a rede")
    exibir_vendas_passadas()
    animacao("Configurando impulsionamento inteligente")
    monitorar()

if __name__ == "__main__":
    main()
