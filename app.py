#!/usr/bin/env python3
import sys
import time
import random
import os
from datetime import datetime, timedelta
from collections import defaultdict
from instagram_private_api import Client, ClientError, ClientLoginError
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track, Progress, SpinnerColumn, BarColumn, TimeElapsedColumn
from rich import box

LOGIN_USUARIO = "seyzalel"
LOGIN_SENHA = "guilherme/seyzalel"
LOG_DIR = os.path.dirname(os.path.abspath(__file__))
console = Console()

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def inicializar_sistema():
    limpar_tela()
    console.rule("[bold blue]BOOT // PRESENZ AI TURBO PLUS")
    console.print(Panel.fit(
        "[bold cyan]Infraestrutura de Telemetria Social Integrada Avançada[/bold cyan]\n"
        "[dim]Unidade Tática de Observação Digital – Sigint+Turbinado[/dim]",
        title="[bold]INICIALIZAÇÃO",
        border_style="cyan"
    ))
    fases = [
        "Estabelecendo túnel criptografado TLS 1.3",
        "Validando token interno no núcleo privado",
        "Coletando metadata de perfil",
        "Sincronizando mapa heurístico do alvo",
        "Carregando módulo emocional E-Frame v2.1",
        "Analisando hashtags e menções",
        "Gerando pipeline de inferência social Deep",
        "Detectando anomalias comportamentais"
    ]
    with Progress(SpinnerColumn(), "[progress.description]{task.description}", BarColumn(), TimeElapsedColumn(), transient=True) as progress:
        for etapa in fases:
            progress.add_task(description=etapa, total=None)
            time.sleep(random.uniform(1.2, 2.0))
    console.print(Panel.fit(
        "[bold green]PRESENZ AI TURBO PLUS ONLINE[/bold green]\n"
        "[bold]Instância validada com sucesso[/bold]\n"
        "[bold]Modo de operação:[/bold] Análise de interação social avançada",
        title="[bold white]SISTEMA PRONTO",
        border_style="green"
    ))
    time.sleep(1.5)

def pode_gerar_novo_relatorio(alvo):
    path = os.path.join(LOG_DIR, f"{alvo.lower()}.last_run")
    agora = datetime.now()
    if os.path.exists(path):
        with open(path) as f:
            ultima = datetime.fromisoformat(f.read().strip())
            if agora - ultima < timedelta(hours=12):
                return False
    with open(path, "w") as f:
        f.write(agora.isoformat())
    return True

def login(usuario, senha):
    try:
        return Client(usuario, senha)
    except (ClientLoginError, ClientError) as e:
        console.print(f"[bold red]Erro de autenticação:[/bold red] {e}")
        sys.exit(1)

def coletar_conexoes(api, alvo):
    info = api.username_info(alvo)["user"]
    followers = info.get("follower_count", 0)
    following = info.get("following_count", 0)
    if followers >= 100_000:
        perfil_tamanho = "grande"
        limite = 30
    elif followers >= 10_000:
        perfil_tamanho = "medio"
        limite = 20
    else:
        perfil_tamanho = "pequeno"
        limite = 10
    rank_token = Client.generate_uuid()
    segs = api.user_followers(info["pk"], rank_token).get("users", [])
    segs2 = api.user_following(info["pk"], rank_token).get("users", [])
    todos = list({u["username"] for u in segs + segs2})
    random.shuffle(todos)
    conexoes = todos[:limite] if len(todos) >= limite else todos[:]
    if perfil_tamanho == "grande":
        min_vis, max_vis = 5, min(12, len(todos))
    elif perfil_tamanho == "medio":
        min_vis, max_vis = 3, min(8, len(todos))
    else:
        min_vis, max_vis = 1, min(6, len(todos))
    num_visitas = random.randint(min_vis, max_vis) if max_vis >= min_vis else max_vis
    visitados = random.sample(todos, num_visitas) if todos else []
    return conexoes, visitados, perfil_tamanho, followers, following, info

def gerar_timestamp(periodo_horas):
    agora = datetime.now()
    horas_atras = random.randint(0, periodo_horas - 1)
    minutos = random.randint(0, 59)
    segundos = random.randint(0, 59)
    instante = agora - timedelta(hours=horas_atras, minutes=minutos, seconds=segundos)
    return instante.strftime("%H:%M:%S"), horas_atras

def gerar_emocao():
    pesos = ["neutra"] * 4 + ["leve"] * 2 + ["intensa", "hesitante", "tensa", "ambígua", "evasiva"]
    return random.choice(pesos)

def gerar_interacao(usuario, perfil_tamanho, periodo_horas):
    timestamp, horas_atras = gerar_timestamp(periodo_horas)
    if perfil_tamanho == "grande":
        inter = int(random.gauss(10, 5))
        inter = max(0, min(inter, 30))
        dura_max = 120
    elif perfil_tamanho == "medio":
        inter = int(random.gauss(5, 3))
        inter = max(0, min(inter, 20))
        dura_max = 60
    else:
        inter = int(random.gauss(2, 1.5))
        inter = max(0, min(inter, 10))
        dura_max = 30
    if inter > 0:
        dur_min = random.randint(1, min(inter * 3, dura_max))
        duracao = f"{dur_min}m{random.randint(0,59):02d}s"
    else:
        dur_min = 0
        duracao = "0m00s"
    if perfil_tamanho == "grande":
        reels = f"{random.randint(1,5)}m{random.randint(0,59):02d}s" if dur_min >= 5 and random.random() > 0.3 else "0m00s"
    elif perfil_tamanho == "medio":
        reels = f"{random.randint(0,3)}m{random.randint(5,59):02d}s" if dur_min >= 3 and random.random() > 0.5 else "0m00s"
    else:
        reels = f"{random.randint(0,2)}m{random.randint(10,59):02d}s" if dur_min >= 2 and random.random() > 0.7 else "0m00s"
    return {
        "timestamp": timestamp,
        "usuario": usuario,
        "interacoes": inter,
        "duracao_min": dur_min,
        "duracao": duracao,
        "reels": reels,
        "emocao": gerar_emocao(),
        "horas_atras": horas_atras
    }

def salvar_log(alvo, dados, visitados, perfil_tamanho, followers, following, info, visitas_count, frequentes, sessoes):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    caminho = os.path.join(LOG_DIR, f"{alvo}_{now}.txt")
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(f"Relatório Presenz AI Turbo Plus - @{alvo} - {perfil_tamanho.upper()} - {followers} seguidores - {following} seguindo\n")
        f.write(f"Data e hora da análise: {now}\n")
        f.write(f"Nome completo: {info.get('full_name','')}\n")
        f.write(f"Biografia: {info.get('biography','')}\n")
        f.write(f"URL Externa: {info.get('external_url','') or ''}\n\n")
        f.write("=== Interações Detalhadas ===\n")
        for d in dados:
            f.write(f"[{d['timestamp']} | -{d['horas_atras']}h] @{d['usuario']} -> {d['interacoes']} msgs, {d['duracao']}, reels {d['reels']}, emoção {d['emocao']}\n")
        f.write("\n=== Perfis Visitados Recentemente ===\n")
        for v in visitados:
            f.write(f"- @{v}\n")
        total_msgs = sum(d["interacoes"] for d in dados)
        avg_msgs = total_msgs / len(dados) if dados else 0
        avg_dur = sum(d["duracao_min"] for d in dados) / len(dados) if dados else 0
        f.write("\n=== Estatísticas Gerais ===\n")
        f.write(f"Total de interações: {total_msgs}\n")
        f.write(f"Média de interações por contato: {avg_msgs:.2f}\n")
        f.write(f"Média de duração (min): {avg_dur:.2f}\n\n")
        f.write("=== Perfil Favorito ===\n")
        for u, c in visitas_count.items():
            if u == max(visitas_count, key=visitas_count.get):
                f.write(f"- @{u}: {c} visitas\n")
        f.write("\n=== Conversas Frequentes ===\n")
        for u, c in frequentes:
            f.write(f"- @{u}: {c} msgs\n")
        f.write("\n=== Sessões Abertas ===\n")
        for u in sessoes:
            f.write(f"- @{u}\n")
        f.write("\nFim do Relatório\n")

def gerar_relatorios(alvo, conexoes, visitados, perfil_tamanho, followers, following, info, periodo_horas):
    console.rule(f"[bold blue]ANÁLISE OSINT — @{alvo} ({perfil_tamanho.upper()}, {followers} seg, {following} seg)")
    periodo_texto = "Última 1 hora" if periodo_horas == 1 else "Últimas 24 horas"
    console.print(Panel.fit(f"{periodo_texto}", title="[bold yellow]Período de Análise", border_style="yellow"))
    console.print(Panel.fit(
        f"Nome de usuário: @{alvo}\n"
        f"Nome completo: {info.get('full_name','')}\n"
        f"Biografia: {info.get('biography','')}\n"
        f"Seguidores: {followers}\n"
        f"Seguindo: {following}\n"
        f"Privado: {'Sim' if info.get('is_private') else 'Não'}\n"
        f"URL externa: {info.get('external_url','') or 'Nenhuma'}",
        title="[bold green]Metadados do Alvo",
        border_style="green"
    ))
    titulo = "Atividades na última hora" if periodo_horas == 1 else "Atividades nas últimas 24h"
    table = Table(title=titulo, box=box.SIMPLE_HEAVY)
    table.add_column("Horário", style="cyan", justify="center")
    table.add_column("Contato", style="magenta")
    table.add_column("Interações", style="green", justify="center")
    table.add_column("Duração", style="yellow", justify="center")
    table.add_column("Reels", style="blue", justify="center")
    table.add_column("Emoção", style="red", justify="center")
    dados = []
    total_msgs = 0
    engajamento = defaultdict(int)
    tempo_total = defaultdict(int)
    for contato in track(conexoes, description="[cyan]Rastreamento de sessões...", transient=True):
        d = gerar_interacao(contato, perfil_tamanho, periodo_horas)
        dados.append(d)
        total_msgs += d["interacoes"]
        engajamento[d["usuario"]] += d["interacoes"]
        tempo_total[d["usuario"]] += d["duracao_min"]
        table.add_row(d["timestamp"], f"@{d['usuario']}", str(d["interacoes"]), d["duracao"], d["reels"], d["emocao"])
        time.sleep(random.uniform(0.5, 1.0))
    console.print(table)
    console.print(Panel.fit(
        f"Total de interações: {total_msgs}\n"
        f"Perfis visitados: {', '.join('@'+v for v in visitados)}",
        title="[bold white]Resumo OSINT",
        border_style="bright_blue"
    ))
    visitas_count = {}
    if perfil_tamanho == "grande":
        min_v, max_v = 5, 15
    elif perfil_tamanho == "medio":
        min_v, max_v = 3, 10
    else:
        min_v, max_v = 1, 5
    for v in visitados:
        visitas_count[v] = random.randint(min_v, max_v)
    top_visitado = max(visitas_count, key=visitas_count.get) if visitas_count else None
    table_fav = Table(title="Perfil Favorito", box=box.ROUNDED)
    table_fav.add_column("Contato", style="magenta")
    table_fav.add_column("Visitas", style="green", justify="center")
    if top_visitado:
        table_fav.add_row(f"@{top_visitado}", str(visitas_count[top_visitado]))
    console.print(table_fav)
    frequentes = sorted(engajamento.items(), key=lambda x: x[1], reverse=True)[:3]
    console.print(Panel.fit(
        "\n".join(f"@{u}: {c} msgs" for u, c in frequentes) or "Nenhuma interação significativa",
        title="[bold magenta]Conversas Frequentes",
        border_style="magenta"
    ))
    sessoes = [u for u, c in engajamento.items() if c >= (8 if perfil_tamanho=="grande" else 5 if perfil_tamanho=="medio" else 3)]
    console.print(Panel.fit(
        "\n".join(f"@{u}" for u in sessoes) or "Nenhuma sessão significativa detectada",
        title="[bold red]Sessões Abertas",
        border_style="red"
    ))
    ranking = Table(title="Top Engajamento", box=box.MINIMAL)
    ranking.add_column("Contato", style="magenta")
    ranking.add_column("Interações", style="green", justify="center")
    ranking.add_column("Tempo (min)", style="yellow")
    for user, count in sorted(engajamento.items(), key=lambda x: x[1], reverse=True):
        mins = tempo_total[user]
        label = " (alto)" if mins >= 90 else " (médio)" if mins >= 45 else ""
        ranking.add_row(f"@{user}", str(count), f"{mins}{label}")
    console.print(ranking)
    salvar_log(alvo, dados, visitados, perfil_tamanho, followers, following, info, visitas_count, frequentes, sessoes)

def main():
    inicializar_sistema()
    console.print("\n[bold cyan]Informe o nome do perfil-alvo (@usuario):[/bold cyan]", end=" ")
    alvo = input().strip().lstrip("@")
    if not alvo:
        console.print("[bold red]Entrada inválida.[/bold red]")
        sys.exit(1)
    console.print("\n[bold cyan]Selecione o período de análise:[/bold cyan]\n[bold cyan]1[/bold cyan] Últimas 24 horas\n[bold cyan]2[/bold cyan] Última 1 hora")
    option = input().strip()
    periodo_horas = 1 if option == "2" else 24
    if not pode_gerar_novo_relatorio(alvo):
        console.print("[bold yellow]Acesso recente detectado. Aguarde antes de gerar novo relatório.[/bold yellow]")
        sys.exit(0)
    api = login(LOGIN_USUARIO, LOGIN_SENHA)
    conexoes, visitados, perfil_tamanho, followers, following, info = coletar_conexoes(api, alvo)
    gerar_relatorios(alvo, conexoes, visitados, perfil_tamanho, followers, following, info, periodo_horas)

if __name__ == "__main__":
    main()
