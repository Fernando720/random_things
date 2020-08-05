import sqlite3
from tkinter import *
import os


class Funcoes:

    def conecta_bd(self):
        self.con = sqlite3.connect('dadosRPG.db')
        self.cursor = self.con.cursor()
        print('Conectando ao banco de dados')

    def desconecta_bd(self):
        self.con.close()
        print('Tabela de personagens adquirida')

    def cria_tabela(self):
        self.conecta_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Personagens(
                id integer primary key,
                nome CHAR(20) NOT NULL
                );  
        """)
        self.con.commit()
        self.desconecta_bd()

    def add_personagem(self):
        self.nome = self.addPersonagem.get()

        self.conecta_bd()
        self.cursor.execute("""
            INSERT INTO Personagens (nome)
            VALUES (?) """, (self.nome,))
        self.con.commit()
        self.desconecta_bd()
        self.select_lista()

    def select_lista(self):
        self.listaPersonagem.delete(*self.listaPersonagem.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT nome FROM Personagens ORDER BY nome ASC;""")
        for item in lista:
            self.listaPersonagem.insert('', END, values=item)

        self.desconecta_bd()