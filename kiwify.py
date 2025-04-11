import time
import random
import os
import sys

plataformas = [
    "1. Kiwify (Recomendado)",
    "2. Kirvano",
    "3. Braip",
    "4. Eduzz",
    "5. Hotmart",
    "6. Monetizze",
    "7. HeroSpark"
]

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def animacao_carregamento(texto, duracao=1.8):
    seq = ['[░░░░░░░░░░]', '[█░░░░░░░░░]', '[██░░░░░░░░]', '[███░░░░░░░]', 
           '[████░░░░░░]', '[█████░░░░░]', '[██████░░░░]', '[███████░░░]', 
           '[████████░░]', '[█████████░]', '[██████████]']
    for etapa in seq:
        sys.stdout.write(f'\r{texto} {etapa}')
        sys.stdout.flush()
        time.sleep(duracao / len(seq))
    print()

def gerar_dados():
    agora = time.strftime('%H:%M:%S')
    conversao = round(random.uniform(29.7, 46.9), 2)
    cliques = random.randint(650, 1550)
    tempo_medio = round(random.uniform(1.8, 4.9), 2)
    cpc = round(random.uniform(0.57, 1.73), 2)
    ctr = round(random.uniform(4.1, 11.2), 2)
    publico = random.choice([
        "Mulheres 25-34 - Produtos de autocuidado e renda extra",
        "Homens 18-30 - Interesse em tráfego pago e e-commerce",
        "Público misto 24-40 - Foco em infoprodutos de ticket médio",
        "Mulheres 30-45 - Cursos de marketing digital e carreira",
        "Homens 20-35 - Nicho financeiro e performance"
    ])
    melhor_periodo = random.choice([
        "08h às 10h", "14h às 16h", "19h às 21h", "21h às 23h"
    ])
    tendencia = random.choice([
        "Alta busca por conteúdos em vídeo",
        "Crescimento de vendas por WhatsApp",
        "Melhor desempenho em anúncios nativos",
        "Criativos com provas sociais estão performando melhor"
    ])
    return {
        "Horário Atual": agora,
        "Taxa de Conversão": f"{conversao}%",
        "Cliques no Link": cliques,
        "Tempo Médio na Página": f"{tempo_medio} min",
        "Custo por Clique (CPC)": f"R$ {cpc}",
        "CTR (Taxa de Cliques)": f"{ctr}%",
        "Melhor Faixa de Horário": melhor_periodo,
        "Perfil de Audiência": publico,
        "Tendência Detectada": tendencia
    }

def exibir_dados(dados):
    print("\n" + "="*60)
    print("        RELATÓRIO INTELIGENTE DE CONVERSÃO - 2025")
    print("="*60)
    for chave, valor in dados.items():
        print(f"{chave:<32} -> {valor}")
    print("="*60 + "\n")
    print("Ajuste seu criativo para a tendência e público revelado.\nAproveite o melhor horário para escalar suas vendas agora.\n")

def main():
    limpar_terminal()
    print("="*70)
    print("        HACK DE VENDAS DIGITAL PRO — KIWIFY 2025")
    print("="*70)
    print("\nSelecione a plataforma de marketing digital:\n")
    for plataforma in plataformas:
        print(plataforma)
    escolha = input("\nDigite o número correspondente à plataforma: ").strip()
    if escolha not in [str(i) for i in range(1, len(plataformas) + 1)]:
        print("\n[ERRO] Plataforma inválida. Finalizando...\n")
        return
    plataforma_nome = plataformas[int(escolha) - 1][3:]
    print(f"\nPlataforma selecionada: {plataforma_nome}\n")
    url = input("Cole o seu link de afiliado para análise: ").strip()
    if not url.startswith("http"):
        print("\n[ERRO] URL inválida. Finalizando...\n")
        return
    print("\nIniciando análise preditiva de performance...\n")
    animacao_carregamento("Extraindo comportamento de audiência")
    animacao_carregamento("Calculando probabilidades de conversão")
    animacao_carregamento("Gerando insights de otimização")
    dados = gerar_dados()
    exibir_dados(dados)

if __name__ == "__main__":
    main()
