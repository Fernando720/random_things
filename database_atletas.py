import sqlite3

db = sqlite3.connect("atletas.db")

cursor = db.cursor()

cursor.execute("""
CREATE TABLE Treinador(
    treinador_id INTEGER NOT NULL PRIMARY KEY,
    nome TEXT,
    altura FLOAT,
    idade INTEGER,
    sexo TEXT,
    peso INTEGER
    );
""")

cursor.execute("""
CREATE TABLE Turma(
    turma_id INTEGER NOT NULL PRIMARY KEY,
    centro TEXT,
    treinador_turma INTEGER,
    FOREIGN KEY(treinador_turma) REFERENCES Treinador(treinador_id)
);
""")

cursor.execute("""
CREATE TABLE Atleta(
    atleta_id INTEGER NOT NULL PRIMARY KEY,
    nome TEXT,
    altura FLOAT,
    idade INTEGER,
    sexo TEXT,
    peso INTEGER
);
""")

cursor.execute("""
CREATE TABLE Treino(
    treino_id INTEGER NOT NULL PRIMARY KEY,
    data TEXT,
    hora TEXT,
    local TEXT,
    vel_media FLOAT,
    turma_treino INTEGER,
    FOREIGN KEY(turma_treino) REFERENCES Turma(turma_id)
);
""")
        
cursor.execute("""
CREATE TABLE Treinamento(
    atletas_treinos INTEGER,
    treinos_atletas INTEGER,
    FOREIGN KEY(atletas_treinos) REFERENCES Atleta(atleta_id),
    FOREIGN KEY(treinos_atletas) REFERENCES Treino(treino_id)
);
""")

cursor.execute("INSERT INTO Treinador(nome,altura,idade,sexo,peso) values(?,?,?,?,?)",("Fernando",1.77,24,"Masculino",80))

cursor.execute("SELECT * FROM Treinador")

resultado = cursor.fetchall()

print(resultado)

cursor.close()
db.close()
