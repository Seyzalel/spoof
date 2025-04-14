javascript:(function(){
    const valorTotal = 7034.25;
    const qtdVendasPainel = 235;
    const valorTopo = 'R$ 7.034,25';
    const progresso = '70.34%';
    const meta = 'R$ 7.0K / R$ 10K';

    document.querySelectorAll('*').forEach(function(el) {
        if (el.children.length === 0 && el.innerText !== undefined) {
            if (el.innerText.includes('R$ 0,00')) el.innerText = valorTopo;
            if (el.innerText.trim() === '0') el.innerText = qtdVendasPainel.toString();
            if (el.innerText.includes('R$ 0K / R$ 10K') || el.innerText.includes('R$ 0K / R$ 0K')) el.innerText = meta;
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
            'Bianca Tavares', 'Eduardo Lima', 'Isis Ferreira',
            'Pedro Henrique', 'Lorena Moura', 'Igor Nascimento',
            'Nathalia Ramos', 'Vinícius Monteiro', 'Emily Santos', 'Thiago Silveira'
        ];

        const horarios = [
            '14:29', '14:25', '14:07',
            '14:01', '13:59', '13:58',
            '13:56', '13:55', '13:53', '13:25'
        ];

        const now = new Date();
        const dataHoje = now.toLocaleDateString('pt-BR');

        for (let i = 0; i < horarios.length; i++) {
            const horaMinuto = horarios[i];
            const cliente = nomes[i];
            const valor = (21.45).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

            const linha = document.createElement('tr');
            linha.innerHTML = `
                <td style="font-size:14px; padding: 12px;">${dataHoje}<br><span style="font-size:12px; color:#666;">${horaMinuto}</span></td>
                <td style="font-size:14px; padding: 12px; max-width:150px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">MAPA DA PROSPERIDADE</td>
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
