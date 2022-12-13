# importando SQLite
import sqlite3 as lite

# criando conexao
con = lite.connect('loja.db')

# criando tabela clientes
with con:
    cur = con.cursor()
    cur.execute\
    #("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, provincia TEXT, cidade TEXT, codigop INT, endereco TEXT, telefone REAL, email TEXT)");
    ("CREATE TABLE produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT, valor_compra REAL, valor_venda REAL, quantidade INT)");
    #("ALTER TABLE clientes ADD COLUMN (provincia TEXT)")





"""
e_descricao.delete(0, 'end')
e_valor_compra.delete(0, 'end')
e_valor_venda.delete(0, 'end')
e_quantidade.delete(0, 'end')

"""