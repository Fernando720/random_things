import pandas as pd
import sqlite3
from tkinter import *
from tkinter import messagebox
import os

'''FUNÇÕES DE INSERÇÃO E EXCLUSÃO DE DADOS'''
class Funcoes:
    def limpa_tela(self):
        self.addPersonagem.delete(0,END)

    def conecta_bd(self):
        self.con = sqlite3.connect('dadosRPG.db')
        self.cursor = self.con.cursor()
        #print('Conectando ao banco de dados')

    def desconecta_bd(self):
        self.con.close()


    def cria_tabela01(self):
        self.conecta_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Personagens(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                nome TEXT NOT NULL,
                iniciativa INTEGER,
                UNIQUE(nome)
                );  
        """)

        self.con.commit()
        self.desconecta_bd()

    def add_personagem(self, event=None):
        self.nome = self.addPersonagem.get()

        if self.addPersonagem.get() == '':
            print("É necessário o nome ter pelo menos um caractere")
            return None

        print(self.nome)
        self.conecta_bd()
        try:
            self.cursor.execute(""" INSERT INTO Personagens (nome)
                                        VALUES (?) """, (self.nome,))
            self.con.commit()
            self.desconecta_bd()
            self.select_lista()
            self.limpa_tela()

        except Exception as e:
            print(e)
            msg = "Ih, deu erro. Verifique se o personagem já existe! "
            messagebox.showinfo("Mensagem de erro", msg)
            print(msg)
            self.limpa_tela()


    def select_lista(self):
        self.listaPersonagem.delete(*self.listaPersonagem.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT nome FROM Personagens ORDER BY nome ASC;""")
        for item in lista:
            self.listaPersonagem.insert('', END, values=item)

        self.desconecta_bd()

    def select_personagem(self):
        self.conecta_bd()
        self.cursor.execute("""SELECT nome FROM Personagens""")
        lista_personagens = []
        for linha in self.cursor.fetchall():

            lista_personagens.append(linha[0])

        self.desconecta_bd()

        return lista_personagens

    def deleta_personagem(self):
        self.nome = self.addPersonagem.get()
        self.conecta_bd()

        self.con.execute("""DELETE FROM Personagens WHERE nome = ? """, (self.nome,))
        self.con.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def onDoubleClick(self, event):
        self.listaPersonagem.selection()

        for personagem in self.listaPersonagem.selection():
            self.limpa_tela()
            col1 = self.listaPersonagem.item(personagem, 'values')

            self.addPersonagem.insert(END, col1)

    def firstNextPressed(self):

        self.label1.destroy()
        self.label2.destroy()

        self.bt_continuar.destroy()
        self.bt_adicionar.destroy()
        self.bt_apagar.destroy()
        self.addPersonagem.destroy()
        self.listaPersonagem.destroy()
        self.listaScroll.destroy()

        self.tela02()
        self.criar_display_tela02()

        self.criar_botoes_tela02()
        self.criar_labels_tela02()


    def add_iniciativa(self):

        listaIniciativa = [display.get() for display in self.listaDisplays]

        print(listaIniciativa)

        self.label.destroy()
        for label in self.listaLabels:
            label.destroy()

        for display in self.listaDisplays:
            display.destroy()
        self.bt_continuar02.destroy()
        self.tela03()









