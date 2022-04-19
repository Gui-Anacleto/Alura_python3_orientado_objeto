from tkinter import *
from tkinter import ttk
import sqlite3
    
class Funcs():
    def limpa_tela(self):
        self.cod.delete(0, END)
        self.nome.delete(0, END)
        self.telefone.delete(0, END)
        self.cidade.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor();print("Conectando ao banco de dados")
    def desconecta_bd(self):
        self.conn.close();print("Desconectando do banco de dados")
    def montaTabelas(self):
        self.conecta_bd()
        #Cria tabela caso ela nao exista
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit();print("Banco de dados criado")
        self.desconecta_bd()
    def variaveis(self):
        self.codigo_add = self.cod.get()
        self.nome_add = self.nome.get()
        self.telefone_add = self.telefone.get()
        self.cidade_add = self.cidade.get()
    def OnDoubleClick(self,event):
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, "values")
            self.cod.insert(END, col1)
            self.nome.insert(END, col2)
            self.telefone.insert(END, col3)
            self.cidade.insert(END, col4)         
    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """,(self.codigo_add))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()

    def alterar_cliete(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade= ?
        WHERE cod = ?""",(self.nome_add,self.telefone_add,self.cidade_add,self.codigo_add))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def add_Cliente(self): 
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""
        INSERT INTO clientes (nome_cliente, telefone, cidade)
        VALUES (?,?,?)""",(self.nome_add, self.telefone_add, self.cidade_add) 
        )
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()

        lista = self.cursor.execute("""
        SELECT cod, nome_cliente, telefone, cidade FROM clientes 
        ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()

    def busca_Cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())
        self.nome.insert(END, '%')
        nome = self.nome.get()
        self.cursor.execute(""" 
        SELECT cod, nome_cliente, telefone, cidade FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("", END, values=i)
        self.limpa_tela()
        self.desconecta_bd()
        
