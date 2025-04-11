javascript:(function(){
    const valorTotal = 2068.50;
    const qtdVendasPainel = 15;
    const valorTopo = 'R$ 2.068,50';
    const progresso = '20.68%';
    const meta = 'R$ 2.0K / R$ 10K';

    document.querySelectorAll('*').forEach(function(el) {
        if (el.children.length === 0 && el.innerText !== undefined) {
            if (el.innerText.includes('R$ 0,00')) el.innerText = valorTopo;
            if (el.innerText.trim() === '0') el.innerText = qtdVendasPainel.toString();
            if (el.innerText.includes('R$ 0K / R$ 10K')) el.innerText = meta;
        }
    });

    const barras = document.querySelectorAll('div[style*="width"]');
    barras.forEach(function(barra){
        if (barra.style.width && barra.style.width.includes('%')) {
            barra.style.width = progresso;
        }
    });

    const tabela = document.querySelector('table');
    if (tabela) {
        let corpo = tabela.querySelector('tbody');
        if (!corpo) {
            corpo = document.createElement('tbody');
            tabela.appendChild(corpo);
        } else {
            corpo.innerHTML = '';
        }

        const nomes = [
            'Aurora Lima', 'Alice Barbosa', 'Levi Castro', 'Isabela Nunes', 'Davi Lucca',
            'Luna Moreira', 'Miguel Souza', 'Laura Teixeira', 'Noah Fernandes', 'Helena Farias',
            'Gael Henrique', 'Sophia Martins', 'Theo Almeida', 'Valentina Rocha', 'Enzo Gabriel'
        ];

        const horarios = [
            '16:00:25', '15:56:25', '15:23:25', '14:54:25', '14:53:25',
            '14:52:25', '14:38:25', '14:37:25', '14:34:25', '14:32:25',
            '14:21:25', '14:10:25', '13:56:25', '13:45:25', '13:43:25'
        ];

        const now = new Date();
        const dataHoje = now.toLocaleDateString('pt-BR');

        for (let i = 0; i < horarios.length; i++) {
            const horaStr = horarios[i];
            const cliente = nomes[i];
            const valor = (137.90).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

            const linha = document.createElement('tr');
            linha.innerHTML = `
                <td style="font-size:14px; padding: 12px;">${dataHoje}<br><span style="font-size:12px; color:#666;">${horaStr}</span></td>
                <td style="font-size:14px; padding: 12px;">Sistema Viral</td>
                <td style="font-size:14px; padding: 12px;">${cliente}</td>
                <td style="font-size:14px; padding: 12px;">
                    <div style="display:inline-block; background:rgba(0,128,0,0.1); color:#008000; font-weight:600; padding:2px 6px; border-radius:4px;">Pago</div><br>
                    <span style="font-size:12px; color:#888;">Pix</span>
                </td>
                <td style="font-size:14px; padding: 12px;">${valor}</td>
            `;
            corpo.appendChild(linha);
        }
    }
})();
