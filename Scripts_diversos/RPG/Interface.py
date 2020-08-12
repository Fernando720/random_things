from tkinter import *
from tkinter import ttk
from Funcoes import Funcoes
from tkinter import messagebox
root = Tk()

class Application(Funcoes):
    def __init__(self):

        '''ABRINDO A JANELA'''
        self.root = root

        '''CHAMANDO OS MÉTODOS DA APLICAÇÃO'''
        self.tela01() #Abrindo primeira tela (outras telas serão criadas a partir de funções num comando de botão)
        self.criar_botoes_tela01()
        self.criar_labels_tela01()
        self.criar_display_tela01()
        self.cria_view_lista_tela01()

        '''Chamando funções do backend (banco de dados e etc)'''
        self.cria_tabela01()
        self.select_lista()

        '''MANTENDO A JANELA ABERTA'''
        root.mainloop()
        
    
    def tela01(self):
        self.root.title('RPG - Lista de personagens')
        #self.root.configure(background='lightblue')
        self.root.geometry('800x600')
        self.root.resizable(False,False)
        self.root.maxsize(width=1800,height=700)
        self.root.minsize(width=400,height=100)

    '''def frames_de_tela(self):
        self.frame1 = Frame(self.root)

        self.frame1.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.96)'''

    def criar_botoes_tela01(self):

        #Botões da tela01\;
        self.bt_continuar = Button(text='Próximo>>>', command=self.firstNextPressed)
        self.bt_continuar.place(relx=0.7,rely=0.8,relwidth=0.2,relheight=0.1)

        self.bt_adicionar = Button(text='Adicionar',command=self.add_personagem)
        self.bt_adicionar.place(relx=0.7,rely=0.2,relwidth=0.1,relheight=0.05)

        self.bt_apagar = Button(text='Apagar', command=self.deleta_personagem)
        self.bt_apagar.place(relx=0.8,rely=0.2,relwidth=0.1,relheight=0.05)

    def criar_labels_tela01(self):

        #labels da tela01:
        self.label1 = Label(text="Personagens adicionados: ")
        self.label1.place(relx=0.05,rely=0.3,)

        self.label2 = Label(text="Adicionar personagem ao combate:")
        self.label2.place(relx=0.05,rely=0.15)
    
    def criar_display_tela01(self):

        #display da tela01
        self.addPersonagem = Entry()
        self.addPersonagem.place(relx=0.05,rely=0.2,relwidth=0.6,relheight=0.05)
        self.addPersonagem.config(font=(40,),justify='right')
        self.addPersonagem.bind('<Return>', self.add_personagem)

    def cria_view_lista_tela01(self):

        self.listaPersonagem = ttk.Treeview(height=1, column=('col1', 'col2'))
        self.listaPersonagem.heading('#0', text='')
        self.listaPersonagem.heading('#1', text='Personagens:')

        self.listaPersonagem.column('#0', width=1)
        self.listaPersonagem.column('#1', width=150)

        self.listaPersonagem.place(relx=0.05,rely=0.35,relwidth=0.275,relheight=0.6)

        self.listaScroll = Scrollbar(orient='vertical')
        self.listaPersonagem.config(yscroll=self.listaScroll.set)
        self.listaScroll.place(relx=0.29,rely=0.35,relwidth=0.04,relheight=0.6)

        self.listaPersonagem.bind('<Double-1>', self.onDoubleClick)
        self.listaPersonagem.delete()

    def tela02(self):

        self.root.title("RPG - Iniciativa dos personagens")
        self.root.geometry('600x400')
        self.root.resizable(False, False)

    def criar_botoes_tela02(self):
        self.bt_continuar02 = Button(text='Próximo>>>', command=self.add_iniciativa)
        self.bt_continuar02.place(relx=0.7,rely=0.8,relwidth=0.2,relheight=0.1)

    def criar_labels_tela02(self):
        self.label = Label(text="Digite a iniciativa de cada personagem abaixo: ", font= ('arial', 14,'bold'))
        self.label.place(relx = 0.1, rely = 0.05)

        '''Caixas de texto com o nome de cada personagem a receber iniciativa via input'''
        charactersList = self.select_personagem()
        counter=1
        i = 0.2
        j = 0.2
        self.listaLabels = []
        for character in charactersList:

            self.label1 = Label(text=character+':', font=18)
            self.listaLabels.append(self.label1)

            if counter < 6:
                self.listaLabels[counter-1].place(relx=0.1, rely=j)
                j = j + 0.1
            elif counter >= 6:
                self.listaLabels[counter-1].place(relx=0.5, rely=i)
                i = i + 0.1

            counter+=1

    def criar_display_tela02(self):
        tamanho = len(self.select_personagem())

        self.listaDisplays= []
        i=0.2
        j=0.2
        for n in range(tamanho):
            self.addIniciativa = Entry()
            self.listaDisplays.append(self.addIniciativa)
            self.listaDisplays[n].config(font=('arial', 14), justify='right')
            if n < 5:
                self.listaDisplays[n].place(relx=0.3,rely=i,relwidth=0.1,relheight=0.05)
                i = i + 0.1
            elif n >= 5:
                self.listaDisplays[n].place(relx=0.7,rely=j,relwidth=0.1,relheight=0.05)
                j = j + 0.1

    def tela03(self):

        self.root.title("RPG - Fila dos personagens")
        self.root.geometry('600x400')
        self.root.resizable(False, False)











