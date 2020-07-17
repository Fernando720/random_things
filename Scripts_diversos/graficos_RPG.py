import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

global personagens
#'Cinthria','Eduardo','Glar','Naeris','Torphin'
personagens = ['Arya','Astrid','Welby']

def adicionando_personagens():


    print('os personagens pré-definidos são: ' )
    print(personagens)
    add_pers = int(input('Deseja adicionar personagens e/ou NPC? Se sim, quantos? '))
    count_1 = 0
    while count_1 <add_pers:
        personagens.append(input('Digite o nome do novo personagem: '))
        count_1+=1

    print('a nova lista de personagens é: ')
    print(personagens)
    return personagens



########## INICIATIVA ##############
def ordem_iniciativa(lista_personagens):

    iniciativa = []

    count_2 = 0
    while count_2 <len(lista_personagens):
        iniciativa.append(int(input('Digite a iniciativa de ' + lista_personagens[count_2] + ': ')))
        count_2+=1

    #combinando as duas listas, ou seja, atribuindo a iniciativa ao personagem:
    combinacao = list(zip(lista_personagens,iniciativa))

    #ordenando a fila
    fila = sorted(combinacao, key=lambda fila: fila[1],reverse=True)

    # Arrumando um jeito mais bonito de printar a fila (depois implementar um GUI com tkinter, se pá)
    df_fila = pd.DataFrame(fila, columns=['Personagem', 'Iniciativa'],
                           index=[(x + 1) for x in range(len(lista_personagens))])
    print(df_fila)

    return df_fila



def combate(ordem_batalha):

    continuar = True
    turno = 1

    # Métricas do jogo

    dano_causado = []
    dano_sofrido = []
    cura_realizada = []
    controle_causado = []
    dano_automitigado = []

    while continuar:

        print('############### TURNO %i #################'%turno)

        condicao_parada = input('Deseja continuar combate? (pressione "n" para parar; qualquer outro valor para continuar): ')

        if condicao_parada == 'n':
            continuar = False
        else:
            vez = 1

            while vez <= len(ordem_batalha['Personagem']):

                if turno == 1:
                    print('Vez de %s' % ordem_batalha['Personagem'][vez])

                    dano_causado.append(int(input('quanto de dano %s causou neste turno? ' % ordem_batalha['Personagem'][vez])))
                    dano_sofrido.append(int(input('quanto de dano %s sofreu neste turno? ' % ordem_batalha['Personagem'][vez])))
                    cura_realizada.append(int(input('quanto de cura %s realizou neste turno? ' % ordem_batalha['Personagem'][vez])))
                    controle_causado.append(int(input('quanto de controle %s causou neste turno? ' % ordem_batalha['Personagem'][vez])))
                    dano_automitigado.append(int(input('quanto de dano %s automitigou nesta turno? ' % ordem_batalha['Personagem'][vez])))

                else:
                    print('Vez de %s' % ordem_batalha['Personagem'][vez])
                    aux_dc = int(input('quanto de dano %s causou neste turno? ' %ordem_batalha['Personagem'][vez]))
                    aux_ds = int(input('quanto de dano %s sofreu neste turno? ' % ordem_batalha['Personagem'][vez]))
                    aux_cr = int(input('quanto de cura %s realizou neste turno? ' % ordem_batalha['Personagem'][vez]))
                    aux_cc = int(input('quanto de controle %s causou neste turno? ' % ordem_batalha['Personagem'][vez]))
                    aux_da = int(input('quanto de dano %s automitigou nesta turno? ' % ordem_batalha['Personagem'][vez]))

                    dano_causado[vez-1] += aux_dc
                    dano_sofrido[vez-1] += aux_ds
                    cura_realizada[vez-1] += aux_cr
                    controle_causado[vez-1] += aux_cc
                    dano_automitigado[vez-1] += aux_da

                vez += 1

        turno += 1
        '''print(dano_causado)
        print(dano_sofrido)
        print(cura_realizada)
        print(controle_causado)
        print(dano_automitigado)'''

    return np.array([dano_causado, dano_sofrido, cura_realizada, controle_causado, dano_automitigado])


if __name__ == '__main__':
    
    fila_turno_RPG = ordem_iniciativa(adicionando_personagens())
    dados_de_combate = combate(fila_turno_RPG)
    print(dados_de_combate)




