import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import pandas as pd

global personagens     #deixando esta variável global por nenhum motivo aparente, mas acho que será importante (sei lá, tá dando no mesmo)
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

########################################################## INICIATIVA #########################################################################

def ordem_iniciativa(lista_personagens):

    iniciativa = []

    count_2 = 0

    while True:
        try:
            #loop para adicionar iniciativa de cada personagem
            while count_2 <len(lista_personagens):
                iniciativa.append(int(input('Digite a iniciativa de ' + lista_personagens[count_2] + ': ')))
                count_2+=1
            break

        except:
            print("Digitou algum número errado? Digite novamente.")

    #combinando as duas listas, ou seja, atribuindo a iniciativa ao personagem:
    combinacao = list(zip(lista_personagens,iniciativa))

    #ordenando a fila de forma decrescente
    fila = sorted(combinacao, key=lambda fila: fila[1],reverse=True)

    # Arrumando um jeito mais bonito de printar a fila (enquanto não se tem um GUI)
    df_fila = pd.DataFrame(fila, columns=['Personagem', 'Iniciativa'],
                           index=[(x + 1) for x in range(len(lista_personagens))])
    return df_fila

############################################################ COMBATE #############################################################################

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

                    while True:
                        try:
                            dano_causado.append(int(input('quanto de dano %s causou neste turno? ' % ordem_batalha['Personagem'][vez])))
                            dano_sofrido.append(int(input('quanto de dano %s sofreu neste turno? ' % ordem_batalha['Personagem'][vez])))
                            cura_realizada.append(int(input('quanto de cura %s realizou neste turno? ' % ordem_batalha['Personagem'][vez])))
                            controle_causado.append(int(input('quanto de controle %s causou neste turno? ' % ordem_batalha['Personagem'][vez])))
                            dano_automitigado.append(int(input('quanto de dano %s automitigou nesta turno? ' % ordem_batalha['Personagem'][vez])))
                            break

                        except ValueError:
                            print('Digitou algum número errado? Preencha novamente os dados do personagem.')
                            try:
                                dano_causado.pop(vez-1)
                                dano_sofrido.pop(vez-1)
                                cura_realizada.pop(vez-1)
                                controle_causado.pop(vez-1)
                                dano_automitigado.pop(vez-1)

                            except IndexError:
                                pass


                else:
                    while True:
                        print('Vez de %s' % ordem_batalha['Personagem'][vez])
                        try:

                            aux_dc = int(input('quanto de dano %s causou neste turno? ' %ordem_batalha['Personagem'][vez]))
                            aux_ds = int(input('quanto de dano %s sofreu neste turno? ' % ordem_batalha['Personagem'][vez]))
                            aux_cr = int(input('quanto de cura %s realizou neste turno? ' % ordem_batalha['Personagem'][vez]))
                            aux_cc = int(input('quanto de controle %s causou neste turno? ' % ordem_batalha['Personagem'][vez]))
                            aux_da = int(input('quanto de dano %s automitigou nesta turno? ' % ordem_batalha['Personagem'][vez]))
                            break

                        except ValueError:
                            print('Digitou algum número errado? Preencha novamente os dados do personagem.')

                    dano_causado[vez-1] += aux_dc
                    dano_sofrido[vez-1] += aux_ds
                    cura_realizada[vez-1] += aux_cr
                    controle_causado[vez-1] += aux_cc
                    dano_automitigado[vez-1] += aux_da

                vez += 1

        turno += 1

    return np.array([dano_causado, dano_sofrido, cura_realizada, controle_causado, dano_automitigado])

#juntar os dados de combate e os dados dos jogadores numa só tabela
def dataframing_everything(dados_combate,ordem_batalha):

    df_dados = pd.DataFrame(ordem_batalha, columns=['Personagem','Iniciativa','dano causado', 'dano sofrido',
                                                'cura realizada', 'controle causado', 'dano automitigado'])

    df_dados['dano causado'] = dados_combate[0]
    df_dados['dano sofrido'] = dados_combate[1]
    df_dados['cura realizada'] = dados_combate[2]
    df_dados['controle causado'] = dados_combate[3]
    df_dados['dano automitigado'] = dados_combate[4]

    tabela_dados = df_dados.drop(columns='Iniciativa')

    return tabela_dados

################################################################## GRÁFICOS #####################################################################
def plotting(tabela_dados):

    df = tabela_dados
    #criando figuras
    fig = plt.figure(1)

    largura_barra = 0.3

    '''Specifies the geometry of the grid that a subplot can be placed in.'''
    gs = gridspec.GridSpec(1,3,figure=fig)


    '''criando primeiro subplot (Dano causado)'''
    ax1 = fig.add_subplot(gs[0,0])
    y1 = list(df['dano causado'])
    ax1.barh(df['Personagem'], y1, color='orange', height=largura_barra)
    plt.title('Dano causado por personagem')
    for i, v in enumerate(y1):
        if v != 0:
            ax1.text(v - 0.2*v, i, str(v), color='white', fontweight='bold')

    '''Criando os demais subplots (primeira linha os danos, segunda linha os demais)'''
    ax2 = fig.add_subplot(gs[0,1])
    #plt.figure(2)
    y2 = list(df['dano sofrido'])


    ax2.barh(df['Personagem'], y2,color='red', height=largura_barra)
    plt.title('Dano sofrido por personagem')
    for i, v in enumerate(y2):
        if v != 0:
            ax2.text(v - 0.2*v, i, str(v), color='white', fontweight='bold')

    #plt.figura(3)
    ax3 = fig.add_subplot(gs[0,2])
    y3 = list(df['dano automitigado'])
    ax3.barh(df['Personagem'], y3,color='gray', height=largura_barra)
    plt.title('Dano automitigado por personagem')
    for i, v in enumerate(y3):
        if v != 0:
            ax3.text(v - 0.2*v, i, str(v), color='black', fontweight='bold')

    fig2 = plt.figure(2)
    gs2 = gridspec.GridSpec(1, 2, figure=fig2)
    #plt.figure(4)
    ax4 = fig2.add_subplot(gs2[0,0])
    y4 = list(df['cura realizada'])
    ax4.barh(df['Personagem'], y4,color='green', height=largura_barra)
    plt.title('Cura realizada por personagem')
    for i, v in enumerate(y4):
        if v != 0:
            ax4.text(v - 0.2*v, i, str(v), color='white', fontweight='bold')

    #plt.figure(5)
    ax5 = fig2.add_subplot(gs2[0,1])
    y5 = list(df['controle causado'])
    ax5.barh(df['Personagem'], y5,color='blue', height=largura_barra)
    plt.title('Controle causado por personagem')
    for i, v in enumerate(y5):
        if v != 0:
            ax5.text(v - 0.2*v, i, str(v), color='white', fontweight='bold')

    plt.show()

########################################################### "FUNÇÃO PRINCIPAL" ##################################################################
if __name__ == '__main__':

    fila_turno_RPG = ordem_iniciativa(adicionando_personagens())
    print(fila_turno_RPG)
    dados_combate = combate(fila_turno_RPG)
    print(dados_combate)
    tabela = dataframing_everything(dados_combate, fila_turno_RPG)
    print(tabela)

    plotting(tabela)




