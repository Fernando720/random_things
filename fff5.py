import numpy as np
import pandas as pd
import openpyxl
import time
import schedule
from tkinter import *
from PIL import ImageTk,Image
from threading import Thread


global dadot,dadotemp,dadopress,dadoden



class Tela:
    def __init__(self,dono):
        self.dono = dono
        width_value = self.dono.winfo_screenwidth()*0.3
        height_value = self.dono.winfo_screenheight()*0.5
        self.dono.geometry("%dx%d+0+0" % (width_value, height_value))
        self.frame = Frame(self.dono, bg='white', borderwidth=0.05)
        self.frame.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1)

        self.frame2 = Frame(self.dono, bg='#d1e0e0', borderwidth=0.05)
        self.frame2.place(relx=0.5, rely=0.0, relwidth=1, relheight=1)

        self.dono.title("Gerar dados de aquisição ")
        #self.dono.wm_iconbitmap('setas.ico')


    def inserir_imagem(self):
        
        
        imagem = ImageTk.PhotoImage(Image.open('fermenter.png'))
        w = Label(self.frame, image=imagem)
        # w.grid(row=1, column=1)
        w.imagem = imagem
        w.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)

def gerar_pontos():
    # gerar tempertaura, pressao, densidade
    temp = 100 * np.random.rand() + 350
    press = 10 * np.random.rand() + 2
    densidade = 0.2 * temp + np.sin(press)

    # obter data e hora local
    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    tempo = time_string

    print(tempo, temp,press,densidade)
    return [tempo,temp,press,densidade]

def tarefa_pontos():
    global dadot,dadotemp,dadopress,dadoden
    [tempo,temp,press,densidade ]= gerar_pontos()
    dadot.append(tempo)
    dadotemp.append(temp)
    dadopress.append(press)
    dadoden.append(densidade)
    print( dadot,dadotemp)



def tarefa_gravar():
    global dadot, dadotemp, dadopress, dadoden
    #df = pd.DataFrame({'tempo': dadot, 'temperatura': dadotemp[0, :], 'pressao': dadopress[0, :], 'densidade': dadoden[0, :]})
    df = pd.DataFrame({'tempo': dadot,'temperatura': dadotemp, 'pressao': dadopress, 'densidade': dadoden})
    df.to_excel("exemplo.xlsx")
    pass


def schedule_thread():
    schedule.every(5).seconds.do(tarefa_pontos)
    schedule.every(120).seconds.do(tarefa_gravar)
    while True:
        schedule.run_pending()
        time.sleep(1)

def tkinter_thread():
    janela = Tk()
    Tela(janela).inserir_imagem()
    janela.mainloop()
    
if __name__ == '__main__':

    dadot=[]
    dadotemp=[]
    dadopress=[]
    dadoden=[]

    Thread(target=schedule_thread).start()
    Thread(target=tkinter_thread).start()

    
    
    

    

