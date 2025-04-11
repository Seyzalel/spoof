javascript:(function(){
    const valorTotal = 8927.36;
    const qtdVendasPainel = 42;
    const valorTopo = 'R$ 8.927,36';
    const progresso = '89.27%';
    const meta = 'R$ 8.9K / R$ 10K';

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

        const nomesModernos2025 = [
            'Enzo Gabriel', 'Valentina Rocha', 'Theo Almeida', 'Sophia Martins', 'Gael Henrique',
            'Helena Farias', 'Noah Fernandes', 'Laura Teixeira', 'Miguel Souza', 'Luna Moreira',
            'Davi Lucca', 'Isabela Nunes', 'Benício Gomes', 'Heloísa Carvalho', 'Levi Castro',
            'Liz Rocha', 'Alice Barbosa', 'Otávio Ramos', 'Emanuel Duarte', 'Cecília Dias',
            'Antonella Silva', 'Zoe Santana', 'Ravi Costa', 'Aurora Fernandes', 'Lorenzo Prado',
            'Eloá Monteiro', 'Calebe Ribeiro', 'Isis Moura', 'Henry Nogueira', 'Mel Andrade',
            'Yuri Rocha', 'Rebeca Luz', 'Gael Oliveira', 'Ayla Cardoso', 'João Lucas Freitas',
            'Maite Carvalho', 'Rael Dias', 'Yasmin Torres', 'Samuel Bernardes', 'Esther Azevedo',
            'Bryan Moreira', 'Bella Mello', 'Pietro Sales', 'Maya Rezende', 'Lucca Pinheiro',
            'Aurora Lima', 'Benjamin Correia', 'Antonny Melo', 'Milena Soares', 'Emanuelly Ribeiro'
        ];

        const produtosComPrecos = [
            { nome: 'PACK COMPLETO', preco: 22.20 },
            { nome: 'Design de Rótulos', preco: 120.00 },
            { nome: 'GOLDENFLIX', preco: 137.90 },
            { nome: 'Método Gringa Turbo', preco: 248.50 },
            { nome: 'Sistema Viral', preco: 137.90 }
        ];

        const now = new Date();
        let vendas = [];
        let total = 0;

        while (total < valorTotal) {
            const p = produtosComPrecos[Math.floor(Math.random() * produtosComPrecos.length)];
            if (total + p.preco > valorTotal) break;
            total += p.preco;
            vendas.push(p);
        }

        vendas = vendas.slice(-10);

        let nomesSorteados = [];
        while (nomesSorteados.length < 10) {
            const nome = nomesModernos2025[Math.floor(Math.random() * nomesModernos2025.length)];
            if (!nomesSorteados.includes(nome)) nomesSorteados.push(nome);
        }

        for (let i = 0; i < vendas.length; i++) {
            const dataVenda = new Date(now.getTime() - i * (Math.floor(Math.random() * 45) + 1) * 60000);
            const dataStr = dataVenda.toLocaleDateString('pt-BR');
            const horaStr = dataVenda.toTimeString().slice(0,5);
            const produto = vendas[i];
            const cliente = nomesSorteados[i];
            const valor = produto.preco.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

            const linha = document.createElement('tr');
            linha.innerHTML = `
                <td style="font-size:14px; padding: 12px;">${dataStr}<br><span style="font-size:12px; color:#666;">${horaStr}</span></td>
                <td style="font-size:14px; padding: 12px;">${produto.nome}</td>
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