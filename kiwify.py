import time
import random
import os
from datetime import datetime, timedelta

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_horarios(qtd_eventos):
    agora = datetime.now()
    horarios = []
    for _ in range(qtd_eventos):
        atraso = random.randint(180, 360)
        horario = agora - timedelta(minutes=atraso)
        horarios.append(horario)
    horarios.sort()
    return horarios

def animacao_inicial(texto, duracao=1.2):
    etapas = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    for _ in range(8):
        for etapa in etapas:
            print(f'\r{texto} {etapa}', end='', flush=True)
            time.sleep(duracao / len(etapas))
    print()

def executar_simulacao():
    limpar()
    print("╭────────────────────────────────────────────────────────────╮")
    print("│              Painel Automático De Conversão 2025          │")
    print("╰────────────────────────────────────────────────────────────╯\n")
    
    animacao_inicial("Inicializando Ambiente Inteligente")
    print("\nGerando sequência de eventos...\n")
    time.sleep(1)

    total_eventos = random.randint(25, 60)
    total_vendas = random.randint(5, 19)
    total_leads = random.randint(7, 15)
    total_cliques = total_eventos - (total_vendas + total_leads)

    eventos = []
    horarios = gerar_horarios(total_eventos)

    for i in range(total_eventos):
        if total_vendas > 0:
            tipo = "venda"
            total_vendas -= 1
        elif total_leads > 0:
            tipo = "lead"
            total_leads -= 1
        else:
            tipo = "clique"
            total_cliques -= 1

        eventos.append((horarios[i], tipo))

    eventos.sort()

    valor_por_venda = 137.90
    vendas_realizadas = 0

    for horario, tipo in eventos:
        hora_formatada = horario.strftime("%H:%M:%S")
        if tipo == "clique":
            print(f"[{hora_formatada}] Clique detectado.")
        elif tipo == "lead":
            print(f"[{hora_formatada}] Lead qualificado identificado.")
        elif tipo == "venda":
            print(f"[{hora_formatada}] Venda confirmada — Comissão: R$ 137,90 — Produto: Sistema Viral")
            vendas_realizadas += 1
        time.sleep(0.15)

    lucro_total = vendas_realizadas * valor_por_venda
    taxa_conversao = (vendas_realizadas / total_eventos) * 100

    print("\nProcesso finalizado com sucesso.\n")
    time.sleep(1)

    print("╭──────────────────────────────────────────────────────╮")
    print("│                   Relatório Final                   │")
    print("╰──────────────────────────────────────────────────────╯\n")
    print(f"Total de Eventos Monitorados: {len(eventos)}")
    print(f"Total de Cliques: {len([e for e in eventos if e[1] == 'clique'])}")
    print(f"Total de Leads Qualificados: {len([e for e in eventos if e[1] == 'lead'])}")
    print(f"Total de Vendas: {vendas_realizadas}")
    print(f"Produto Monitorado: Sistema Viral")
    print(f"Comissão por Venda: R$ 137,90")
    print(f"Lucro Total: R$ {lucro_total:,.2f}")
    print(f"Taxa de Conversão: {taxa_conversao:.2f}%\n")
    print("Painel finalizado. Dados simulados com sucesso.")

if __name__ == "__main__":
    executar_simulacao()
