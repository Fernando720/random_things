import PySimpleGUI as sg

class TelaPython:

    def __init__ (self):

        layout = [
            [sg.Text('Nome'), sg.Input()],
            [sg.Text('idade'), sg.Input()],
            [sg.Button('Enviar Dados')]
        ]

        janela = sg.Window('Dados do usuário').layout(layout)

        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)


tela = TelaPython()

tela.Iniciar()
