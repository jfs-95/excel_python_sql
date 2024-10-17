# excel_python_sql
Criei um projeto de análise de dados para transformar um arquivo CSV com informações de vendas de café em um banco de dados organizado e pronto para gerar insights. O primeiro passo foi carregar o arquivo `vendas_att.csv` usando a biblioteca `pandas`, configurando corretamente o separador de colunas e a codificação.

Durante o processo de preparação dos dados, identifiquei que os valores monetários estavam utilizando vírgulas como separadores decimais. Para padronizar, substituí as vírgulas por pontos e converti essas colunas para tipos numéricos, garantindo que 'quantidade', 'dinheiro' e 'total_vendas' pudessem ser manipulados com precisão. Também transformei a coluna de datas para um formato `datetime`, criando uma nova coluna que representava o mês e o ano de cada venda.

Com os dados prontos para análise, agrupei as informações para responder a algumas questões-chave:
- **Total de vendas por produto**: para identificar quais produtos geraram mais receita.
- **Média de vendas mensais por produto**: ajudando a entender o desempenho médio de cada café ao longo do tempo.
- **Vendas totais por mês**: para verificar as tendências mensais.
- **Quantidade total de produtos vendidos**: fornecendo uma visão geral do volume de vendas.
- **Produto mais vendido e sua quantidade total**: destacando o item mais popular.

Após essa agregação, estabeleci a conexão com um banco de dados MySQL, onde criei um novo banco chamado `vendas_analise` e tabelas específicas para armazenar cada conjunto de dados processados. As tabelas foram estruturadas para abrigar:
- **Vendas totais por produto** (`v_por_produto`).
- **Média de vendas mensais** (`media_vendas_m`).
- **Vendas totais mensais** (`v_m_total`).
- **Total de produtos vendidos** (`total_p_v`).
- **Produto mais vendido** (`p_mais_v_total`).

Finalmente, os dados foram inseridos nessas tabelas, e o banco de dados foi preenchido com informações organizadas e facilmente acessíveis para futuras análises. O projeto proporcionou uma solução robusta para transformar dados brutos em uma base estruturada, facilitando a tomada de decisões informadas sobre o desempenho das vendas de café.
Extraindo dados de uma planilha atraves do Python e inserindo no Banco de dados do SQL
