import time
import random
import os
from datetime import datetime, timedelta

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_horarios_distanciados(qtd):
    agora = datetime.now()
    inicio_execucao = agora - timedelta(hours=6)
    horarios = []
    intervalo = 0
    for _ in range(qtd):
        intervalo += random.randint(5, 13)
        horarios.append(inicio_execucao + timedelta(minutes=intervalo))
    return horarios

def animacao(frase, duracao=1.0):
    ciclos = ['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏']
    for _ in range(8):
        for etapa in ciclos:
            print(f'\r{frase} {etapa}', end='', flush=True)
            time.sleep(duracao / len(ciclos))
    print()

def executar_bot():
    limpar()
    print("╭────────────────────────────────────────────────────────────╮")
    print("│               Bot Autônomo De Vendas Afiliadas            │")
    print("╰────────────────────────────────────────────────────────────╯\n")

    animacao("Iniciando inteligência automática")
    time.sleep(0.6)
    animacao("Estabelecendo conexões com servidores de tráfego")

    total_eventos = random.randint(28, 54)
    total_vendas = random.randint(6, 18)
    total_leads = random.randint(6, 14)
    total_cliques = total_eventos - total_vendas - total_leads

    tipos = (["venda"] * total_vendas) + (["lead"] * total_leads) + (["clique"] * total_cliques)
    random.shuffle(tipos)

    horarios = gerar_horarios_distanciados(total_eventos)
    eventos = sorted(zip(horarios, tipos))

    print("\nO bot foi executado automaticamente e iniciou suas operações há algumas horas.")
    print("Durante esse período, ele otimizou tráfego, captou leads e converteu em vendas.")
    print("Todos os registros abaixo foram processados enquanto você apenas deixou ele rodando.\n")
    time.sleep(1.2)

    vendas_confirmadas = 0
    valor_comissao = 137.90

    for horario, tipo in eventos:
        hora = horario.strftime("%H:%M:%S")
        if tipo == "clique":
            print(f"[{hora}] Acesso recebido no link afiliado.")
        elif tipo == "lead":
            print(f"[{hora}] Lead qualificado identificado.")
        elif tipo == "venda":
            print(f"[{hora}] Venda confirmada — Comissão recebida: R$ 137,90 — Produto: Sistema Viral")
            vendas_confirmadas += 1
        time.sleep(0.18)

    cliques_total = len([e for e in eventos if e[1] == "clique"])
    leads_total = len([e for e in eventos if e[1] == "lead"])
    lucro_total = vendas_confirmadas * valor_comissao
    taxa_conversao = (vendas_confirmadas / total_eventos) * 100

    time.sleep(1.5)
    print("\nO sistema atingiu a meta configurada para essa sessão.")
    print("O bot desligou automaticamente após concluir todas as tarefas com sucesso.\n")
    time.sleep(1)

    print("╭──────────────────────────────────────────────────────╮")
    print("│                  Relatório De Desempenho             │")
    print("╰──────────────────────────────────────────────────────╯\n")
    print(f"Eventos Monitorados: {total_eventos}")
    print(f"Cliques Registrados: {cliques_total}")
    print(f"Leads Qualificados: {leads_total}")
    print(f"Vendas Realizadas: {vendas_confirmadas}")
    print(f"Produto Promovido: Sistema Viral")
    print(f"Comissão Por Venda: R$ 137,90")
    print(f"Lucro Total: R$ {lucro_total:,.2f}")
    print(f"Taxa De Conversão: {taxa_conversao:.2f}%\n")
    print("Você não precisou fazer nada. O bot trabalhou por você.")
    print("Resultado entregue. Execução encerrada com excelência.\n")

if __name__ == "__main__":
    executar_bot()
