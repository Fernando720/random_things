import pandas as pd
import sqlite3
from tkinter import *
import os


class Funcoes:
    def limpa_tela(self):
        self.addPersonagem.delete(0,END)

    def conecta_bd(self):
        self.con = sqlite3.connect('dadosRPG.db')
        self.cursor = self.con.cursor()
        #print('Conectando ao banco de dados')

    def desconecta_bd(self):
        self.con.close()


    def cria_tabela(self):
        self.conecta_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Personagens(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                nome TEXT NOT NULL,
                UNIQUE(nome)
                );  
        """)

        self.con.commit()
        self.desconecta_bd()

    def add_personagem(self, event=None):
        self.nome = self.addPersonagem.get()

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
            print("Ih, deu erro. Verifique se o personagem já existe! ")
            self.limpa_tela()


    def select_lista(self):
        self.listaPersonagem.delete(*self.listaPersonagem.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT nome FROM Personagens ORDER BY nome ASC;""")
        for item in lista:
            self.listaPersonagem.insert('', END, values=item)

        self.desconecta_bd()

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




