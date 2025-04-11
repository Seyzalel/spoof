javascript:(function(){
    const valorTotal = 8927.36;
    const qtdVendas = 597;
    const valorTopo = 'R$ 8.927,36';
    const progresso = '89.27%';
    const meta = 'R$ 8.9K / R$ 10K';

    document.querySelectorAll('*').forEach(function(el) {
        if (el.children.length === 0 && el.innerText !== undefined) {
            if (el.innerText.includes('R$ 0,00')) el.innerText = valorTopo;
            if (el.innerText.trim() === '0') el.innerText = qtdVendas.toString();
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

        const nomes = ['Enzo Gabriel', 'Valentina Rocha', 'Theo Almeida', 'Sophia Martins', 'Gael Henrique', 'Helena Farias', 'Miguel Souza', 'Manuela Ribeiro', 'Davi Lucca', 'Isabela Nunes', 'Noah Fernandes', 'Laura Teixeira', 'Lorenzo Prado', 'Cecília Dias', 'Benício Gomes', 'Heloísa Carvalho', 'Isaac Monteiro', 'Antonella Silva', 'Levi Castro', 'Liz Rocha', 'Alice Barbosa', 'Otávio Ramos', 'Emanuel Duarte', 'Luna Moreira', 'Zoe Costa', 'Henrique Beltrão', 'Clara Santana', 'Yasmin Torres'];
        const produtos = ['Curso Completo', 'Mentoria Premium', 'E-book Digital PRO', 'Pack Estratégico 2025', 'Acesso VIP'];

        const valores = [];
        let total = 0;
        while (valores.length < qtdVendas - 1) {
            const v = (Math.random() * 100 + 50).toFixed(2);
            total += parseFloat(v);
            valores.push(parseFloat(v));
        }
        valores.push(parseFloat((valorTotal - total).toFixed(2)));

        const now = new Date();
        for (let i = 0; i < qtdVendas; i++) {
            const minutosRand = Math.floor(Math.random() * 45) + 1;
            const dataVenda = new Date(now.getTime() - i * minutosRand * 60000);
            const dataStr = dataVenda.toLocaleDateString('pt-BR');
            const horaStr = dataVenda.toTimeString().slice(0,5);
            const produto = produtos[Math.floor(Math.random() * produtos.length)];
            const cliente = nomes[Math.floor(Math.random() * nomes.length)];
            const valor = valores[i].toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

            const linha = document.createElement('tr');
            linha.innerHTML = `
                <td style="font-size:14px; padding: 12px;">${dataStr}<br><span style="font-size:12px; color:#666;">${horaStr}</span></td>
                <td style="font-size:14px; padding: 12px;">${produto}</td>
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
