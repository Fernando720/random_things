import re
import tkinter as tk
import math
from typing import List

class Calculator:
    def __init__(
        self,
        root: tk.Tk,
        label: tk.Label, 
        display: tk.Entry,
        buttons: List[List[tk.Button]]
    ):
                
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons
    
    def start(self):
        self._config_buttons()
        self._config_display()
        self._config_display()
        self.root.mainloop()

    def _config_buttons(self):
        buttons = self.buttons
        for row_values in buttons:
            for button in row_values:
                button_text = button['text']
                
                if button_text == 'C':
                    button.bind('<Button-1>', self.clear)

                if button_text in '0123456789.+-/*()^':
                    button.bind('<Button-1>', self.add_text_to_display)

                if button_text == '=':
                    button.bind('<Button-1>', self.calculate)
    
    def _config_display(self):
        self.display.bind('<Return>', self.calculate)
        #self.display.bind('<KP_Enter>', self.calculate)

    def _fix_text(self, text):
        #substitui tudo que não for 012345679+-/*^ para nada
        text = re.sub(r'[^\d\.\/\*\-\+\(\)\^e]', r'', text, 0)
        #substitui sinais repetidos para apenas um sinal
        text = re.sub(r'([\.\+\*\^])\1+', r'\1', text, 0)
        #substitui () ou *() para nada
        text = re.sub(r'\*\?\(\)', '', text)

        return text

    def clear(self,event=None):
        self.display.delete(0,'end')

    def add_text_to_display(self, event=None):
        self.display.insert('end', event.widget['text'])
    
    def calculate(self, event=None):
        fixed_text = self._fix_text(self.display.get())
        equations = self._get_equations(fixed_text)
        #print(equations)

        try:
            if len(equations) == 1:
                result = eval(self._fix_text(equations[0]))

            else:
                result = eval(self._fix_text(equations[0]))
                for equation in equations[1:]:
                    result = math.pow(result.eval(self._fix_text(equation)))

            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.display.config(text=f'{fixed_text} = {result}')
            self.label.config(text='Conta realizada')

        except OverflowError:
            self.label.config(text="Não consegui realizar esta conta. Desculpe!")
        except Exception as error:
            print(error)
            self.label.config(text='conta inválida')

    def _get_equations(self,text):
        return re.split('\^', text, 0)

'''def make_root() -> tk.Tk:
    
    root =  tk.Tk()

    root.title('calculadora')
    root.config(padx=10,pady=10,background='#fff')
    root.resizable(False,False)

    return root

def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text='sem conta ainda',
        anchor = 'e', justify = 'right', background='#fff'
    )
    label.grid(row=0,column=0,columnspan=5,sticky='news')
    return label

def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1,column=0,columnspan=5,sticky='news',pady=(0,10))
    display.config(
        font=('Helvetica', 40, 'bold'),
        justify = 'right', bd = 1, relief = 'flat',
        highlightthickness=1, highlightcolor = '#ccc'
    )
    display.bind('<Control-a>', display_control_a)
    return display

def display_control_a(event):
    event.widget.select_range(0,'end')
    event.widget.icursor('end')
    return 'break'

def make_buttons(root) -> List[List[tk.Button]]:
    button_texts: List[list[str]] = [
        ['7', '8', '9', '+', 'C'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '='],
    ]

    buttons: List[List[tk.Button]] = []

    for row_index, row_value in enumerate(button_texts, start=2):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = tk.Button(root, text=col_value)
            btn.grid(row=row_index,column=col_index,sticky='news',padx=5,pady=5)
            btn.config(
                font = ('Helvetica',15,'normal'),
                pady = 40, width = 1, background = '#f1f2f3',bd=0,
                cursor='hand2',highlightthickness=0,
                highlightcolor = '#ccc', activebackground='#ccc',
                highlightbackground='#ccc',
            )
            button_row.append(btn)
        buttons.append(button_row)

    return buttons

def main():

    root = make_root()
    display = make_display(root)
    label = make_label(root)
    buttons = make_buttons(root)
    #root.mainloop()
    calculator = Calculator(root,label,display,buttons)
    calculator.start()

if __name__ == '__main__':
    main() '''



