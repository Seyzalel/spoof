import time
import random
import os
from datetime import datetime, timedelta

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_horarios_realistas(qtd):
    agora = datetime.now()
    inicio = agora - timedelta(hours=6)
    fim = agora - timedelta(hours=4)
    intervalo_total = int((fim - inicio).total_seconds() // 60)
    pontos = sorted(random.sample(range(10, intervalo_total - 10), qtd))
    return [inicio + timedelta(minutes=m) for m in pontos]

def animacao(frase, duracao=0.9):
    ciclos = ['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏']
    for _ in range(6):
        for etapa in ciclos:
            print(f'\r{frase} {etapa}', end='', flush=True)
            time.sleep(duracao / len(ciclos))
    print()

def executar_bot():
    limpar()
    print("╭────────────────────────────────────────────────────────────╮")
    print("│                  Bot Autônomo De Conversão                 │")
    print("╰────────────────────────────────────────────────────────────╯\n")

    animacao("Iniciando execução inteligente")
    time.sleep(0.6)
    animacao("Processando dados da operação")

    total_eventos = random.randint(28, 54)
    total_vendas = random.randint(6, 18)
    total_leads = random.randint(6, 14)
    total_cliques = total_eventos - total_vendas - total_leads

    tipos = (["venda"] * total_vendas) + (["lead"] * total_leads) + (["clique"] * total_cliques)
    random.shuffle(tipos)

    horarios = gerar_horarios_realistas(total_eventos)
    eventos = sorted(zip(horarios, tipos))

    print("\nOperação ativa.\n")
    time.sleep(1.2)

    vendas_realizadas = 0
    comissao = 137.90

    for horario, tipo in eventos:
        hora = horario.strftime("%H:%M:%S")
        if tipo == "clique":
            print(f"[{hora}] Clique recebido no link afiliado.")
        elif tipo == "lead":
            print(f"[{hora}] Lead qualificado identificado.")
        elif tipo == "venda":
            print(f"[{hora}] Venda confirmada — Comissão: R$ 137,90 — Produto: Sistema Viral")
            vendas_realizadas += 1
        time.sleep(0.17)

    total_cliques = len([e for e in eventos if e[1] == "clique"])
    total_leads = len([e for e in eventos if e[1] == "lead"])
    lucro_total = vendas_realizadas * comissao
    taxa = (vendas_realizadas / total_eventos) * 100

    time.sleep(1.3)
    print("\nMeta atingida. O bot finalizou automaticamente a operação.\n")
    time.sleep(0.7)

    print("╭──────────────────────────────────────────────────────╮")
    print("│                   Relatório Final                   │")
    print("╰──────────────────────────────────────────────────────╯\n")
    print(f"Eventos Monitorados: {total_eventos}")
    print(f"Cliques Registrados: {total_cliques}")
    print(f"Leads Qualificados: {total_leads}")
    print(f"Vendas Realizadas: {vendas_realizadas}")
    print(f"Produto Promovido: Sistema Viral")
    print(f"Comissão Por Venda: R$ 137,90")
    print(f"Lucro Total: R$ {lucro_total:,.2f}")
    print(f"Taxa De Conversão: {taxa:.2f}%\n")
    print("O bot executou todas as ações automaticamente.")
    print("Você não precisou fazer nada. Ele trabalhou e vendeu por você.\n")

if __name__ == "__main__":
    executar_bot()
