javascript:(function(){
    const valorTotal = 1241.10;
    const qtdVendasPainel = 9;
    const valorTopo = 'R$ 1.241,10';
    const progresso = '12.41%';
    const meta = 'R$ 1.2K / R$ 10K';

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
            'Otávio Bernardes', 'Melissa Duarte', 'Ícaro Sanches', 'Lívia Peixoto',
            'Eduardo Moura', 'Giovana Maciel', 'Tainá Silveira', 'Nathan Prado', 'Bianca Rezende'
        ];

        const horarios = [
            '09:41:30', '09:38:30', '09:32:30', '09:19:30', '09:08:30',
            '09:05:30', '08:47:30', '08:46:30', '08:17:30'
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
