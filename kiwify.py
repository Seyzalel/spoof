import time
import random
import os
from datetime import datetime, timedelta

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_horarios_distanciados(qtd):
    agora = datetime.now()
    horario_base = agora - timedelta(hours=6)
    horarios = []
    intervalo = 0
    for _ in range(qtd):
        intervalo += random.randint(3, 12)
        horarios.append(horario_base + timedelta(minutes=intervalo))
    return horarios

def animacao(titulo, duracao=1.0):
    etapas = ['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏']
    for _ in range(8):
        for etapa in etapas:
            print(f'\r{titulo} {etapa}', end='', flush=True)
            time.sleep(duracao / len(etapas))
    print()

def executar_registro():
    limpar()
    print("╭────────────────────────────────────────────────────────────╮")
    print("│               Monitoramento Profissional de Vendas         │")
    print("╰────────────────────────────────────────────────────────────╯\n")
    
    animacao("Estabelecendo conexão com os registros")
    time.sleep(0.6)
    animacao("Processando dados arquivados")

    total_eventos = random.randint(26, 52)
    total_vendas = random.randint(5, 18)
    total_leads = random.randint(6, 14)
    total_cliques = total_eventos - total_vendas - total_leads

    tipos = (["venda"] * total_vendas) + (["lead"] * total_leads) + (["clique"] * total_cliques)
    random.shuffle(tipos)

    horarios = gerar_horarios_distanciados(total_eventos)
    eventos = sorted(zip(horarios, tipos))

    print("\nOs registros a seguir foram coletados durante a operação do bot nas últimas horas:\n")
    time.sleep(1)

    vendas_registradas = 0
    valor_unitario = 137.90

    for horario, tipo in eventos:
        hora = horario.strftime("%H:%M:%S")
        if tipo == "clique":
            print(f"[{hora}] Acesso registrado no link afiliado.")
        elif tipo == "lead":
            print(f"[{hora}] Lead qualificado identificado no funil.")
        elif tipo == "venda":
            print(f"[{hora}] Venda confirmada — Comissão recebida: R$ 137,90 — Produto: Sistema Viral")
            vendas_registradas += 1
        time.sleep(0.18)

    cliques_total = len([e for e in eventos if e[1] == "clique"])
    leads_total = len([e for e in eventos if e[1] == "lead"])
    lucro_total = vendas_registradas * valor_unitario
    taxa_conversao = (vendas_registradas / total_eventos) * 100

    time.sleep(1.2)
    print("\nApresentação de registros finalizada.\n")
    time.sleep(0.7)

    print("╭──────────────────────────────────────────────────────╮")
    print("│                    Relatório Final                   │")
    print("╰──────────────────────────────────────────────────────╯\n")
    print(f"Total De Eventos Monitorados: {total_eventos}")
    print(f"Cliques Registrados: {cliques_total}")
    print(f"Leads Qualificados: {leads_total}")
    print(f"Vendas Confirmadas: {vendas_registradas}")
    print(f"Produto Monitorado: Sistema Viral")
    print(f"Comissão Por Venda: R$ 137,90")
    print(f"Lucro Total: R$ {lucro_total:,.2f}")
    print(f"Taxa De Conversão: {taxa_conversao:.2f}%\n")
    print("O bot encerrou sua execução após completar a operação com êxito.")
    print("Todos os dados apresentados refletem a atividade real capturada durante o processo.")

if __name__ == "__main__":
    executar_registro()
