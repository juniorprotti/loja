import sys
import os


from cgitb import text
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox

#importando view
from view import *

#### criando janela ####
janela = Tk()
janela.title("")
janela.geometry('1125x700')
janela.configure(background='white')
janela.resizable(width=FALSE, height=FALSE)

#### dividindo a janela ####

frame_principal = Frame(janela, width=250, height=700, bg='sky blue', relief='flat')
frame_principal.grid(row=0, column=0)

frame_direita = Frame(janela, width=1125, height=700, bg='light blue', relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

# variavel tree global
global tree



def clientes():
    frame_esquerda_clientes = Frame(janela, width=250, height=900, bg='sky blue', relief='flat')
    frame_esquerda_clientes.grid(row=0, column=0)

    frame_direita_clientes = Frame(janela, width=250, height=803, bg='light blue', relief='flat')
    frame_direita_clientes.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)


    ### CONFIGURANDO FRAME CLENTES ####
    l_nome = Label(frame_esquerda_clientes, text='Nome', anchor=NW, font=('Ivy 10 bold'), bg='lightblue', fg='black',relief='flat')
    l_nome.place(x=15, y=10)
    e_nome = Entry(frame_esquerda_clientes, width=20, justify='left', relief='flat', bg='white', fg='black')
    e_nome.place(x=15, y=30)

    l_provincia = Label(frame_esquerda_clientes, text='Provincia', anchor=NW, font=('Ivy 10 bold'), bg='lightblue',fg='black', relief='flat')
    l_provincia.place(x=15, y=70)
    e_provincia = Entry(frame_esquerda_clientes, width=20, justify='left', relief='flat', bg='white', fg='black')
    e_provincia.place(x=15, y=90)

    l_cidade = Label(frame_esquerda_clientes, text='Cidade', anchor=NW, font=('Ivy 10 bold'), bg='lightblue',fg='black', relief='flat')
    l_cidade.place(x=15, y=130)
    e_cidade = Entry(frame_esquerda_clientes, width=20, justify='left', relief='flat', bg='white', fg='black')
    e_cidade.place(x=15, y=150)

    l_codigop = Label(frame_esquerda_clientes, text='Codigo Postal', anchor=NW, font=('Ivy 10 bold'), bg='lightblue',fg='black', relief='flat')
    l_codigop.place(x=15, y=190)
    e_codigop = Entry(frame_esquerda_clientes, width=20, justify='left', relief='flat', bg='white', fg='black')
    e_codigop.place(x=15, y=210)

    l_endereco = Label(frame_esquerda_clientes, text='Endereço', anchor=NW, font=('Ivy 10 bold'), bg='lightblue', fg='black',relief='flat')
    l_endereco.place(x=15, y=250)
    e_endereco = Entry(frame_esquerda_clientes, width=20, justify='left', relief='flat', bg='white', fg='black')
    e_endereco.place(x=15, y=270)

    l_telefone = Label(frame_esquerda_clientes, text='Telefone', anchor=NW, font=('Ivy 10 bold'), bg='lightblue', fg='black',relief='flat')
    l_telefone.place(x=15, y=310)
    e_telefone = Entry(frame_esquerda_clientes, width=20, justify='left', relief='flat', bg='white', fg='black')
    e_telefone.place(x=15, y=330)

    l_email = Label(frame_esquerda_clientes, text='Email', anchor=NW, font=('Ivy 10 bold'), bg='lightblue',fg='black', relief='flat')
    l_email.place(x=15, y=370)
    e_email = Entry(frame_esquerda_clientes, width=20, justify='left', relief='flat', bg='white', fg='black')
    e_email.place(x=15, y=390)

    #### BOTAO INSERIR
    #b_inserir = Button(frame_esquerda_clientes, text='Inserir', width=25, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
    #b_inserir.place(x=15, y=350)

    #### BOTAO ATUALIZAR
    #b_atualizar = Button(frame_esquerda_clientes, text='Atualizar', width=25, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
    #b_atualizar.place(x=15, y=400)

    #### BOTAO DELETAR
    #b_deletar = Button(frame_esquerda_clientes, text='Deletar', width=25, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
    #b_deletar.place(x=15, y=450)

    #### BOTAO VOLTAR
    b_voltar = Button(frame_esquerda_clientes,command=lambda: [frame_esquerda_clientes.grid_forget(), frame_direita_clientes.grid_forget()], text='Voltar', width=7, font=('Ivy 9 bold'), bg='skyblue', fg='black',relief='raised', overrelief='ridge')
    b_voltar.place(x=15, y=650)

    def mostrar_cli():
        global tree

        lista = mostrar_clientes()

        # lista para cabecario
        tabela_head = ['Id', 'Nome','Provincia', 'Cidade','Codigo Postal','Endereço','Telefone','Email']

        # criando tabela
        tree = ttk.Treeview(frame_direita_clientes, selectmode='extended', columns=tabela_head, show='headings')
        tree.column('Id', minwidth=0, width=25)
        tree.column('Nome', minwidth=0, width=130)
        tree.column('Provincia', minwidth=0, width=200)
        tree.column('Cidade', minwidth=0, width=100)
        tree.column('Codigo Postal', minwidth=0, width=80)
        tree.column('Endereço', minwidth=0, width=280)
        tree.column('Telefone', minwidth=0, width=110)
        tree.column('Email', minwidth=0, width=150)

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_direita_clientes, orient=VERTICAL, command=tree.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_direita_clientes, orient=HORIZONTAL, command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.place(relx=0.01, rely=0.01, relwidth=0.76, relheight=0.76)
        #tree.grid(column=0, row=0, sticky='nsew')
        #vsb.grid(column=1, row=0, sticky='ns')
        #hsb.grid(column=0, row=1, sticky='ew')

        frame_direita_clientes.grid_rowconfigure(0, weight=12)

        hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw", "nw"]
        h = [30, 170, 100, 100, 80, 180, 110, 100]
        n = 0

        for col in tabela_head:
            tree.heading(col, text=col.title(), anchor=CENTER)
            # adjust the colummns width to the header string
            tree.column(col, width=h[n], anchor=hd[n])

            n += 1

        for item in lista:
            tree.insert('', 'end', values=item)

    # chamando a funcao mostrar
    mostrar_cli()

    def inserir_cliente():
        nome = e_nome.get()
        provincia = e_provincia.get()
        cidade = e_cidade.get()
        codigop = e_codigop.get()
        endereco = e_endereco.get()
        telefone = e_telefone.get()
        email = e_email.get()

        lista = [nome,provincia,cidade,codigop, endereco, telefone, email]

        if nome == '':
            messagebox.showerror('ERRO', 'O campo nome deve ser preenchido')
        else:
            inserir_clientes(lista)
            messagebox.showinfo('Sucesso', 'Cliente cadastrado com sucesso')

            e_nome.delete(0, 'end')
            e_provincia.delete(0, 'end')
            e_cidade.delete(0, 'end')
            e_codigop.delete(0, 'end')
            e_endereco.delete(0, 'end')
            e_telefone.delete(0, 'end')
            e_email.delete(0, 'end')

        for widget in frame_direita_clientes.winfo_children():
            widget.destroy()


        mostrar_cli()

    b_inserir = Button(frame_esquerda_clientes,command=inserir_cliente, text='Inserir', width=25, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
    b_inserir.place(x=15, y=450)


    def atualizar_cliente():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = tree_lista[0]

            e_nome.delete(0, 'end')
            e_provincia.delete(0, 'end')
            e_cidade.delete(0, 'end')
            e_codigop.delete(0, 'end')
            e_endereco.delete(0, 'end')
            e_telefone.delete(0, 'end')
            e_email.delete(0, 'end')

            e_nome.insert(0, tree_lista[1])
            e_provincia.insert(0, tree_lista[2])
            e_cidade.insert(0, tree_lista[3])
            e_codigop.insert(0, tree_lista[4])
            e_endereco.insert(0, tree_lista[5])
            e_telefone.insert(0, tree_lista[6])
            e_email.insert(0, tree_lista[7])

            #funcao atualizar
            def update():
                nome = e_nome.get()
                provincia = e_provincia.get()
                cidade = e_cidade.get()
                codigop = e_codigop.get()
                endereco = e_endereco.get()
                telefone = e_telefone.get()
                email = e_email.get()

                lista = [nome,provincia,cidade,codigop, endereco, telefone, email, valor_id]

                if nome == '':
                    messagebox.showerror('ERRO', 'Todos os campos devem ser preenchidos')
                else:
                    atualizar_clientes(lista)
                    messagebox.showinfo('Sucesso', 'Cliente atualizado com sucesso')

                    e_nome.delete(0, 'end')
                    e_provincia.delete(0, 'end')
                    e_cidade.delete(0, 'end')
                    e_codigop.delete(0, 'end')
                    e_endereco.delete(0, 'end')
                    e_telefone.delete(0, 'end')
                    e_email.delete(0, 'end')

                for widget in frame_direita_clientes.winfo_children():
                    widget.destroy()

                mostrar_cli()

            #botao confirmar
            b_confirmar = Button(frame_esquerda_clientes, command=update, text='Confirmar', width=25, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
            b_confirmar.place(x=15, y=600)

        except IndexError:
            messagebox.showerror('ERRO', 'Selecione um cliente da tabela')

    b_atualizar = Button(frame_esquerda_clientes,command=atualizar_cliente, text='Atualizar', width=25, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
    b_atualizar.place(x=15, y=500)


    def deletar():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = [tree_lista[0]]

            deletar_clientes(valor_id)
            messagebox.showinfo('Sucesso', 'O cliente foi deletado')

            for widget in frame_direita_clientes.winfo_children():
                widget.destroy()

            mostrar_cli()

        except IndexError:
            messagebox.showerror('ERRO', 'Selecione um dos clientes da tabela')

    b_deletar = Button(frame_esquerda_clientes,command=deletar, text='Deletar', width=25, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
    b_deletar.place(x=15, y=550)



def produtos():
    frame_esquerda_produtos = Frame(janela, width=250, height=700, bg='sky blue', relief='flat')
    frame_esquerda_produtos.grid(row=0, column=0)

    frame_direita_produtos = Frame(janela, width=700, height=703, bg='light blue', relief='flat')
    frame_direita_produtos.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

    ### CONFIGURANDO FRAME PRODUTOS ####
    l_descricao = Label(frame_esquerda_produtos, text='Descricao', anchor=NW, font=('Ivy 10 bold'), bg='lightblue', fg='black',relief='flat')
    l_descricao.place(x=15, y=10)
    e_descricao = Entry(frame_esquerda_produtos, width=20, justify='left', relief='flat', bg='white', fg='black')
    e_descricao.place(x=15, y=30)

    l_valor_compra = Label(frame_esquerda_produtos, text='Valor de Compra', anchor=NW, font=('Ivy 10 bold'), bg='lightblue',fg='black', relief='flat')
    l_valor_compra.place(x=15, y=90)
    e_valor_compra = Entry(frame_esquerda_produtos, width=20, justify='left', relief='flat', bg='white', fg='black')
    e_valor_compra.place(x=15, y=110)

    l_valor_venda = Label(frame_esquerda_produtos, text='Valor de Venda', anchor=NW, font=('Ivy 10 bold'), bg='lightblue',fg='black', relief='flat')
    l_valor_venda.place(x=15, y=170)
    e_valor_venda = Entry(frame_esquerda_produtos, width=20, justify='left', relief='flat', bg='white', fg='black')
    e_valor_venda.place(x=15, y=190)

    l_quantidade = Label(frame_esquerda_produtos, text='Quantidade', anchor=NW, font=('Ivy 10 bold'), bg='lightblue',fg='black', relief='flat')
    l_quantidade.place(x=15, y=250)
    e_quantidade = Entry(frame_esquerda_produtos, width=20, justify='left', relief='flat', bg='white', fg='black')
    e_quantidade.place(x=15, y=270)


    def mostrar_prod():
        global tree

        lista = mostrar_produtos()

        # lista para cabecario
        tabela_head = ['Id', 'Descrição','Valor Compra', 'Valor Venda','Quantidade']

        # criando tabela
        tree = ttk.Treeview(frame_direita_produtos, selectmode='extended', columns=tabela_head, show='headings')
        tree.column('Id', minwidth=0, width=25)
        tree.column('Descrição', minwidth=0, width=250)
        tree.column('Valor Compra', minwidth=0, width=25)
        tree.column('Valor Venda', minwidth=0, width=25)
        tree.column('Quantidade', minwidth=0, width=80)


        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_direita_produtos, orient=VERTICAL, command=tree.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_direita_produtos, orient=HORIZONTAL, command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.place(relx=0.01, rely=0.01, relwidth=0.76, relheight=0.96)

        frame_direita_produtos.grid_rowconfigure(0, weight=12)

        hd = ["nw", "nw", "nw", "nw", "nw"]
        h = [10, 250, 25, 25, 10]
        n = 0

        for col in tabela_head:
            tree.heading(col, text=col.title(), anchor=CENTER)
            # adjust the colummns width to the header string
            tree.column(col, width=h[n], anchor=hd[n])

            n += 1

        for item in lista:
            tree.insert('', 'end', values=item)

    # chamando a funcao mostrar
    mostrar_prod()

    def inserir_produto():
        descricao = e_descricao.get()
        valor_compra = e_valor_compra.get()
        valor_venda = e_valor_venda.get()
        quantidade = e_quantidade.get()


        lista = [descricao, valor_compra, valor_venda, quantidade]

        if descricao == '':
            messagebox.showerror('ERRO', 'O campo descriçāo deve ser preenchido')
        else:
            inserir_produtos(lista)
            messagebox.showinfo('Sucesso', 'Produto cadastrado com sucesso')

            e_descricao.delete(0, 'end')
            e_valor_compra.delete(0, 'end')
            e_valor_venda.delete(0, 'end')
            e_quantidade.delete(0, 'end')


        for widget in frame_direita_produtos.winfo_children():
            widget.destroy()


        mostrar_prod()

    b_inserir = Button(frame_esquerda_produtos,command=inserir_produto, text='Inserir', width=25, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
    b_inserir.place(x=15, y=350)


    def atualizar_produto():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = tree_lista[0]

            e_descricao.delete(0, 'end')
            e_valor_compra.delete(0, 'end')
            e_valor_venda.delete(0, 'end')
            e_quantidade.delete(0, 'end')

            e_descricao.insert(0, tree_lista[1])
            e_valor_compra.insert(0, tree_lista[2])
            e_valor_venda.insert(0, tree_lista[3])
            e_quantidade.insert(0, tree_lista[4])


            #funcao atualizar
            def update():
                descricao = e_descricao.get()
                valor_compra = e_valor_compra.get()
                valor_venda = e_valor_venda.get()
                quantidade = e_quantidade.get()

                lista = [descricao, valor_compra, valor_venda, quantidade, valor_id]

                if descricao == '':
                    messagebox.showerror('ERRO', 'Todos os campos devem ser preenchidos')
                else:
                    atualizar_produtos(lista)
                    messagebox.showinfo('Sucesso', 'Produto atualizado com sucesso')

                    e_descricao.delete(0, 'end')
                    e_valor_compra.delete(0, 'end')
                    e_valor_venda.delete(0, 'end')
                    e_quantidade.delete(0, 'end')

                for widget in frame_direita_produtos.winfo_children():
                    widget.destroy()

                mostrar_prod()

            #botao confirmar
            b_confirmar = Button(frame_esquerda_produtos, command=update, text='Confirmar', width=25, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
            b_confirmar.place(x=15, y=500)

        except IndexError:
            messagebox.showerror('ERRO', 'Selecione um produto da tabela')

    b_atualizar = Button(frame_esquerda_produtos,command=atualizar_produto, text='Atualizar', width=25, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
    b_atualizar.place(x=15, y=400)


    def deletar():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = [tree_lista[0]]

            deletar_produtos(valor_id)
            messagebox.showinfo('Sucesso', 'O produto foi deletado')

            for widget in frame_direita_produtos.winfo_children():
                widget.destroy()

            mostrar_prod()

        except IndexError:
            messagebox.showerror('ERRO', 'Selecione um dos produtos da tabela')

    b_deletar = Button(frame_esquerda_produtos,command=deletar, text='Deletar', width=25, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
    b_deletar.place(x=15, y=450)


    #### BOTAO INSERIR
    #b_inserir = Button(frame_esquerda_produtos,command=inserir_produto, text='Inserir', width=25, font=('Ivy 9 bold'), bg='skyblue', fg='black',relief='raised', overrelief='ridge')
    #b_inserir.place(x=15, y=350)

    #### BOTAO ATUALIZAR
    #b_atualizar = Button(frame_esquerda_produtos, text='Atualizar', width=25, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
    #b_atualizar.place(x=15, y=400)

    #### BOTAO DELETAR
    #b_deletar = Button(frame_esquerda_produtos, text='Deletar', width=25, font=('Ivy 9 bold'), bg='skyblue', fg='black',relief='raised', overrelief='ridge')
    #b_deletar.place(x=15, y=450)

    #### BOTAO VOLTAR
    b_voltar = Button(frame_esquerda_produtos, command=lambda: [frame_esquerda_produtos.grid_forget(), frame_direita_produtos.grid_forget()], text='Voltar', width=7,font=('Ivy 9 bold'), bg='skyblue', fg='black', relief='raised', overrelief='ridge')
    b_voltar.place(x=15, y=550)
    #frame_direita_produtos.grid_forget()


def vendas():
    frame_esquerda_vendas = Frame(janela, width=250, height=700, bg='sky blue', relief='flat')
    frame_esquerda_vendas.grid(row=0, column=0)

    frame_direita_vendas = Frame(janela, width=700, height=703, bg='light blue', relief='flat')
    frame_direita_vendas.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

    def nova_venda():
        frame_esquerda_nova_venda = Frame(janela, width=250, height=700, bg='sky blue', relief='flat')
        frame_esquerda_nova_venda.grid(row=0, column=0)

        frame_direita_nova_venda = Frame(janela, width=700, height=703, bg='light blue', relief='flat')
        frame_direita_nova_venda.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

        b_voltar = Button(frame_esquerda_nova_venda, command=lambda: [frame_esquerda_nova_venda.grid_forget(), frame_direita_nova_venda.grid_forget()], text='Voltar', width=7,font=('Ivy 9 bold'), bg='skyblue', fg='black', relief='raised', overrelief='ridge')
        b_voltar.place(x=15, y=650)

        l_pesqCli = Label(frame_direita_nova_venda, text='Pesquisar Cliente:', anchor=NW, font=('Ivy 18 bold'), bg='lightblue',fg='black', relief='flat')
        l_pesqCli.place(x=10, y=10)

        e_pesqCli = Entry(frame_direita_nova_venda, width=18, justify='left', relief='flat', bg='white', fg='black')
        e_pesqCli.place(x=180, y=10)

        b_pesqCli = Button(frame_direita_nova_venda, text='Pesquisar', width=7, font=('Ivy 9 bold'), bg='skyblue', fg='black', relief='raised',overrelief='ridge')
        b_pesqCli.place(x=370, y=10)

        b_selectCli = Button(frame_direita_nova_venda, text='Selecionar', width=7, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
        b_selectCli.place(x=470, y=10)


        l_pesqProd = Label(frame_direita_nova_venda, text='Pesquisar Produto:', anchor=NW, font=('Ivy 18 bold'),bg='lightblue', fg='black', relief='flat')
        l_pesqProd.place(x=10, y=360)

        e_pesqProd = Entry(frame_direita_nova_venda, width=18, justify='left', relief='flat', bg='white', fg='black')
        e_pesqProd.place(x=180, y=360)

        b_pesqProd = Button(frame_direita_nova_venda, text='Pesquisar', width=7, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
        b_pesqProd.place(x=370, y=360)

        b_selectProd = Button(frame_direita_nova_venda, text='Selecionar', width=7, font=('Ivy 9 bold'), bg='skyblue',fg='black', relief='raised', overrelief='ridge')
        b_selectProd.place(x=470, y=360)




        def mostrar_cli():
            global tree

            lista = mostrar_clientes()

            # lista para cabecario
            tabela_head = ['Id', 'Nome', 'Provincia', 'Cidade', 'Codigo Postal', 'Endereço', 'Telefone', 'Email']

            # criando tabela
            tree = ttk.Treeview(frame_direita_nova_venda, selectmode='extended', columns=tabela_head, show='headings')
            tree.column('Id', minwidth=0, width=25)
            tree.column('Nome', minwidth=0, width=130)
            tree.column('Provincia', minwidth=0, width=200)
            tree.column('Cidade', minwidth=0, width=100)
            tree.column('Codigo Postal', minwidth=0, width=80)
            tree.column('Endereço', minwidth=0, width=280)
            tree.column('Telefone', minwidth=0, width=110)
            tree.column('Email', minwidth=0, width=150)

            # vertical scrollbar
            vsb = ttk.Scrollbar(frame_direita_nova_venda, orient=VERTICAL, command=tree.yview)

            # horizontal scrollbar
            hsb = ttk.Scrollbar(frame_direita_nova_venda, orient=HORIZONTAL, command=tree.xview)

            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree.place(relx=0.01, rely=0.055, relwidth=0.76, relheight=0.44)


            frame_direita_nova_venda.grid_rowconfigure(0, weight=12)

            hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw", "nw"]
            h = [30, 170, 100, 100, 80, 180, 110, 100]
            n = 0

            for col in tabela_head:
                tree.heading(col, text=col.title(), anchor=CENTER)
                # adjust the colummns width to the header string
                tree.column(col, width=h[n], anchor=hd[n])

                n += 1

            for item in lista:
                tree.insert('', 'end', values=item)

        # chamando a funcao mostrar
        mostrar_cli()

        def mostrar_prod():
            global tree

            lista = mostrar_produtos()

            # lista para cabecario
            tabela_head = ['Id', 'Descrição', 'Valor Compra', 'Valor Venda', 'Quantidade']

            # criando tabela
            tree = ttk.Treeview(frame_direita_nova_venda, selectmode='extended', columns=tabela_head, show='headings')
            tree.column('Id', minwidth=0, width=25)
            tree.column('Descrição', minwidth=0, width=250)
            tree.column('Valor Compra', minwidth=0, width=25)
            tree.column('Valor Venda', minwidth=0, width=25)
            tree.column('Quantidade', minwidth=0, width=80)

            # vertical scrollbar
            vsb = ttk.Scrollbar(frame_direita_nova_venda, orient=VERTICAL, command=tree.yview)

            # horizontal scrollbar
            hsb = ttk.Scrollbar(frame_direita_nova_venda, orient=HORIZONTAL, command=tree.xview)

            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree.place(relx=0.01, rely=0.56, relwidth=0.76, relheight=0.5)
            # tree.grid(column=0, row=0, sticky='nsew')
            # vsb.grid(column=1, row=0, sticky='ns')
            # hsb.grid(column=0, row=1, sticky='ew')

            frame_direita_nova_venda.grid_rowconfigure(0, weight=12)

            hd = ["nw", "nw", "nw", "nw", "nw"]
            h = [10, 250, 25, 25, 10]
            n = 0

            for col in tabela_head:
                tree.heading(col, text=col.title(), anchor=CENTER)
                # adjust the colummns width to the header string
                tree.column(col, width=h[n], anchor=hd[n])

                n += 1

            for item in lista:
                tree.insert('', 'end', values=item)

        # chamando a funcao mostrar
        mostrar_prod()












    b_nova_venda = Button(frame_esquerda_vendas,command=nova_venda, text='Nova Venda', width=10, font='Ivy 15 bold', bg='skyblue',fg='black', relief='raised', overrelief='ridge')
    b_nova_venda.place(x=50, y=150)

    b_atualizar_venda = Button(frame_esquerda_vendas, text='Atualizar Venda', width=10, font='Ivy 15 bold', bg='skyblue',fg='black', relief='raised', overrelief='ridge')
    b_atualizar_venda.place(x=50, y=250)

    b_deletar_venda = Button(frame_esquerda_vendas, text='Deletar Venda', width=10, font='Ivy 15 bold', bg='skyblue',fg='black', relief='raised', overrelief='ridge')
    b_deletar_venda.place(x=50, y=350)

    b_voltar = Button(frame_esquerda_vendas, command=frame_esquerda_vendas.grid_forget, text='Voltar', width=7,font=('Ivy 9 bold'), bg='skyblue', fg='black', relief='raised', overrelief='ridge')
    b_voltar.place(x=15, y=550)











b_clientes = Button(frame_principal, command=clientes, text='Clientes', width=10, font='Ivy 15 bold', bg='skyblue',fg='black', relief='raised', overrelief='ridge')
b_clientes.place(x=50, y=150)

b_produtos = Button(frame_principal, command=produtos, text='Produtos', width=10, font='Ivy 15 bold', bg='skyblue',fg='black', relief='raised', overrelief='ridge')
b_produtos.place(x=50, y=250)

b_vendas = Button(frame_principal, command=vendas, text='Vendas', width=10, font='Ivy 15 bold', bg='skyblue',fg='black', relief='raised', overrelief='ridge')
b_vendas.place(x=50, y=350)













def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


janela.mainloop()

