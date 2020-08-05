from tkinter import *
from tkinter import ttk
from Funcoes import Funcoes
root = Tk()

class Application(Funcoes):
    def __init__(self):
        
        self.root = root
        self.tela()
        #self.frames_de_tela()
        self.criar_botoes()
        self.criar_labels()
        self.criar_display()
        self.cria_view_lista()
        self.cria_tabela()
        self.select_lista()
        root.mainloop()
        
    
    def tela(self):
        self.root.title('RPG - Lista de personagens')
        #self.root.configure(background='lightblue')
        self.root.geometry('800x600')
        self.root.resizable(False,False)
        self.root.maxsize(width=1800,height=700)
        self.root.minsize(width=400,height=100)
    
    def frames_de_tela(self):
        self.frame1 = Frame(self.root)

        self.frame1.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.96)

    def criar_botoes(self):
        self.bt_limpar = Button(text='Próximo>>>')
        self.bt_limpar.place(relx=0.7,rely=0.8,relwidth=0.2,relheight=0.1)

        self.bt_ok = Button(text='OK',command=self.add_personagem)
        self.bt_ok.place(relx=0.75,rely=0.2,relwidth=0.1,relheight=0.05)


    def criar_labels(self):
        self.label1 = Label(text="Personagens adicionados: ")
        self.label1.place(relx=0.05,rely=0.3,)

        self.label2 = Label(text="Adicionar personagem ao combate:")
        self.label2.place(relx=0.05,rely=0.15)
    
    def criar_display(self):
        self.addPersonagem = Entry()
        self.addPersonagem.place(relx=0.05,rely=0.2,relwidth=0.6,relheight=0.05)

    def cria_view_lista(self):
        self.listaPersonagem = ttk.Treeview(height=1, column=('col1', 'col2'))
        self.listaPersonagem.heading('#0', text='')
        self.listaPersonagem.heading('#1', text='Personagens:')

        self.listaPersonagem.column('#0', width=1)
        self.listaPersonagem.column('#1', width=150)

        self.listaPersonagem.place(relx=0.05,rely=0.35,relwidth=0.275,relheight=0.6)

        self.listaScroll = Scrollbar(orient='vertical')
        self.listaPersonagem.config(yscroll=self.listaScroll.set)
        self.listaScroll.place(relx=0.29,rely=0.35,relwidth=0.04,relheight=0.6)


Application()