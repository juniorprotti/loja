import sqlite3 as lite

# criando conexao
con = lite.connect('loja.db')

# inserir clientes

def inserir_clientes(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO clientes (nome, provincia, cidade, codigop, endereco, telefone, email) VALUES (?,?,?,?,?,?,?)"
        cur.execute(query, i)


# acessar clientes

def mostrar_clientes():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM clientes"
        cur.execute(query)
        informacao = cur.fetchall()
        for i in informacao:
            lista.append(i)
    return lista



def inserir_produtos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO produtos (descricao, valor_compra, valor_venda, quantidade) VALUES (?, ?, ?, ?)"
        cur.execute(query, i)

def mostrar_produtos():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM produtos"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista

def atualizar_clientes(i):
    with con:
        cur = con.cursor()
        query = "UPDATE clientes SET nome=?,provincia=?,cidade=?,codigop=?, endereco=?, telefone=?, email=? WHERE id=?"
        cur.execute(query, i)

def atualizar_produtos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE produtos SET descricao=?,valor_compra=?,valor_venda=?, quantidade=? WHERE id=?"
        cur.execute(query, i)

def deletar_clientes(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM clientes WHERE id=?"
        cur.execute(query, i)

def deletar_produtos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM produtos WHERE id=?"
        cur.execute(query, i)





