import pandas as pd
import mysql.connector

#ABRIR O ARQUIVO
file = 'dados/vendas_att.csv'

df = pd.read_csv(file, encoding='utf-8', sep=';')

#CONVERTER , PRA .

df['dinheiro'] = df['dinheiro'].str.replace(',','.', regex=False)
df['total_vendas'] = df['total_vendas'].str.replace(',','.', regex=False)

#CONVERTER OBJETO PARA NUMERICO

df['quantidade'] = pd.to_numeric(df['quantidade'])
df['dinheiro'] = pd.to_numeric(df['dinheiro'])
df['total_vendas'] = pd.to_numeric(df['total_vendas'])

#CONVERTER OBJETO PRA DATATIME

df['data'] = pd.to_datetime(df['data'], format='mixed', dayfirst=True)

df['mes'] = df['data'].dt.to_period('M').astype(str)

v_por_produto = df.groupby('café_nome')['total_vendas'].sum()
media_vendas_m = df.groupby(['mes', 'café_nome'])['quantidade'].mean()
v_m_total = df.groupby('mes')['total_vendas'].sum()
total_p_v = df['quantidade'].sum()

p_t = df.groupby(df['café_nome'])['quantidade'].sum()
p_mais_v = p_t.idxmax()
q_total = p_t.max()

df_p_mais_v_total = pd.DataFrame({
    'Produto Mais Vendido': [p_mais_v],
    'Quantidade Total': [q_total]

})

conectar = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    password='1234',
)

cursor = conectar.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS vendas_analise")

cursor.execute("USE vendas_analise")

cursor.execute('''
CREATE TABLE IF NOT EXISTS v_por_produto (
               cafe_nome VARCHAR(20),
               total_vendido FLOAT     
)
               ''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS media_vendas_m (
               mes CHAR(7),
               cafe_nome VARCHAR(20),
               media_vendas FLOAT    
)   
               ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS v_m_total (
               mes CHAR(7),
               total_vendas FLOAT  
)   
               ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS total_p_v (
               
               descricao varchar(100),
               quantidade INT
)   
               ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS p_mais_v_total (
               
               Produto_Mais_Vendido VARCHAR(20),
               Quantidade INT
)               
               ''')

for produto, TotalVendido in v_por_produto.items():
    cursor.execute('''
    INSERT INTO v_por_produto (cafe_nome, total_vendido) VALUES (%s, %s)
    ''', (produto, TotalVendido))

for (mes,produto), media_venda in media_vendas_m.items():
    cursor.execute('''
    INSERT INTO media_vendas_m (mes, cafe_nome, media_vendas) VALUES (%s, %s, %s)
    ''', (mes, produto, media_venda))

for mes, TotalVendido in v_m_total.items():
    cursor.execute('''
    INSERT INTO v_m_total (mes, total_vendas) VALUES (%s, %s)
    ''', (mes, TotalVendido))

cursor.execute('''
INSERT INTO total_p_v (descricao, Quantidade) VALUES (%s, %s)
''', ('Total de Produtos Vendidos', int(total_p_v)))


produto = df_p_mais_v_total.iloc[0]['Produto Mais Vendido']
quantidade = int(df_p_mais_v_total.iloc[0]['Quantidade Total'])

cursor.execute('''
INSERT INTO p_mais_v_total (Produto_Mais_Vendido, Quantidade) VALUES (%s, %s)
''', (produto, quantidade))
    
conectar.commit()

cursor.close()
conectar.close()

print("Dados inseridos com sucesso no MySQL!")



#print(media_vendas_m)

#print(df.info())
