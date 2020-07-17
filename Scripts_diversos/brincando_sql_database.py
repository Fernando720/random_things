import pandas as pd
import numpy as np
import os
import sqlite3
import matplotlib.pyplot as plt


os.remove("Formula1.db") if os.path.exists("Formula1.db") else None

# criando conexão
db = sqlite3.connect("Formula1.db")
# criando cursor
cursor = db.cursor()


def create_table():
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Season2019(posicao INTEGER NOT NULL,piloto TEXT NOT NULL,equipe TEXT NOT NULL,' \
        'pontos INTEGER,vitorias INTEGER,podios INTEGER,DNF INTEGER,PRIMARY KEY(posicao))')


def insert_new_data(dados):
    # lendo os dados
    cursor.execute('SELECT * FROM Season2019')
    # para contar as linhas da tabela, que vai ser a quantidade de pilotos já adicionados.
    linhas = cursor.fetchall()
    tamanho_tabela = len(linhas)
    tamanho_dados = len(dados)
    contador = tamanho_tabela
    if tamanho_tabela != tamanho_dados:
        while contador < tamanho_dados:
            cursor.execute('INSERT INTO Season2019 VALUES(?,?,?,?,?,?,?)', dados[contador])
            contador = contador + 1
    db.commit()
    

def table_to_insert():

    data_to_insert = [(1, "Hamilton", "Mercedes", 413, 11, 17, 0),
                  (2, "Bottas", "Mercedes", 326, 4, 15, 2),
                  (3, "Verstappen", "Red Bull", 278, 3, 9, 2),
                  (4, "Leclerc", "Ferrari", 264, 2, 10, 2),
                  (5, "Vettel", "Ferrari", 240, 1, 9, 2),
                  (6, "Sainz", "Mclaren", 96, 0, 1, 3),
                  (7, "Gasly", "Red Bull/Toro Roso", 95, 0, 1, 1),
                  (9, "Ricciardo", "Renault", 54, 0, 0, 4),
                  (8, "Albon", "Toro Roso/Red Bull", 92, 0, 0, 1),
                  (10, "Perez", "Racing Point", 52, 0, 0, 2),
                  ]
    
    return data_to_insert

#transformando em dataframe o bagui do banco de dados que foi criado

def sql_table_to_dataframe():
    cursor.execute("SELECT * FROM Season2019")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows,columns=[x[0] for x in cursor.description])
    df = df.set_index("posicao")
    return df

#gráfico de pontos:

def plotting(dataframe):
    pilotos = list(dataframe['piloto'])
    pontos = list(dataframe['pontos'])
    pilotos.reverse()
    pontos.reverse()

    plt.figure(1)
    plt.barh(pilotos,pontos,color="brown")
    plt.title("Pontos conquistados em 21 corridas")
    plt.show()

if __name__ == '__main__':
    
    create_table()
    insert_new_data(table_to_insert())
    plotting(sql_table_to_dataframe())


    cursor.close()
    db.close()