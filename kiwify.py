import time
import random
import os
from datetime import datetime, timedelta

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_horarios_em_ordem(qtd):
    agora = datetime.now()
    base_minutos = random.randint(180, 360)
    horarios = []
    for i in range(qtd):
        minutos_atras = base_minutos - (qtd - i)
        horario = agora - timedelta(minutes=minutos_atras)
        horarios.append(horario)
    return horarios

def animacao(titulo, duracao=0.9):
    etapas = ['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏']
    for _ in range(12):
        for etapa in etapas:
            print(f'\r{titulo} {etapa}', end='', flush=True)
            time.sleep(duracao / len(etapas))
    print()

def executar_registro():
    limpar()
    print("╭────────────────────────────────────────────────────────────╮")
    print("│             Relatório De Execução — Sistema K             │")
    print("╰────────────────────────────────────────────────────────────╯\n")

    animacao("Acessando registros do monitoramento")
    time.sleep(0.7)

    total_eventos = random.randint(28, 54)
    total_vendas = random.randint(5, 19)
    total_leads = random.randint(6, 14)
    total_cliques = total_eventos - total_vendas - total_leads

    eventos = []
    horarios = gerar_horarios_em_ordem(total_eventos)
    tipos = (["venda"] * total_vendas) + (["lead"] * total_leads) + (["clique"] * total_cliques)
    random.shuffle(tipos)

    for i in range(total_eventos):
        eventos.append((horarios[i], tipos[i]))
    eventos.sort()

    print("Monitoramento iniciado anteriormente foi registrado com sucesso.\n")
    time.sleep(1.1)

    vendas_registradas = 0
    valor_unitario = 137.90

    for horario, tipo in eventos:
        hora = horario.strftime("%H:%M:%S")
        if tipo == "clique":
            print(f"[{hora}] Clique recebido no link afiliado.")
        elif tipo == "lead":
            print(f"[{hora}] Lead qualificado detectado durante a campanha.")
        elif tipo == "venda":
            print(f"[{hora}] Venda confirmada — Comissão registrada: R$ 137,90 — Produto: Sistema Viral")
            vendas_registradas += 1
        time.sleep(0.15)

    cliques_total = len([e for e in eventos if e[1] == "clique"])
    leads_total = len([e for e in eventos if e[1] == "lead"])
    lucro_total = vendas_registradas * valor_unitario
    taxa_conversao = (vendas_registradas / total_eventos) * 100

    time.sleep(1.3)
    print("\nResumo do monitoramento encerrado:\n")
    print("╭──────────────────────────────────────────────────────╮")
    print("│                   Detalhes Da Operação               │")
    print("╰──────────────────────────────────────────────────────╯\n")
    print(f"Eventos Registrados: {total_eventos}")
    print(f"Cliques Validados: {cliques_total}")
    print(f"Leads Qualificados: {leads_total}")
    print(f"Vendas Confirmadas: {vendas_registradas}")
    print(f"Produto Monitornado: Sistema Viral")
    print(f"Comissão Por Venda: R$ 137,90")
    print(f"Lucro Total: R$ {lucro_total:,.2f}")
    print(f"Taxa De Conversão: {taxa_conversao:.2f}%\n")
    print("O bot encerrou sua execução após cumprir totalmente o objetivo proposto.")
    print("Todos os registros foram salvos e analisados com êxito.")

if __name__ == "__main__":
    executar_registro()
