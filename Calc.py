from tkinter import *

# Funções


def btnNumClick(number):
    main_input.insert(len(main_input.get()), str(number))
    return


def btnActionClick(action):
    if action == "C":
        main_input.delete(0, len(main_input.get()))
    if action == "+":
        print("")
    return


# Criar uma janela
window = Tk()

# Título para janela
window.title("Calculadora")

# Input Area
main_input = Entry(window)

# Butões Numéricos
i = 0
while i < 10:
    btn = Button(window,
                 text=str(i),
                 padx=21,
                 pady=7,
                 command=lambda k=i: btnNumClick(k))

    if (i == 0):
        btn.grid(row=5, column=1)
    elif (i <= 3):
        btn.grid(row=4, column=i-1)
    elif (i <= 6):
        btn.grid(row=3, column=i-4)
    else:
        btn.grid(row=2, column=i-7)

    i += 1

# Botões de Ação
btn_c = Button(window, text="C", padx=21, pady=7,
               command=lambda: btnActionClick("C"))


# Construir tela
main_input.grid(row=0, column=0, columnspan=4)
btn_c.grid(row=1, column=1)

# Rodar Tela
window.mainloop()
