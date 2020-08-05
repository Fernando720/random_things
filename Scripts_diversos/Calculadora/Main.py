from Funcoes import *
from Classes import *


def main():

    root = make_root()
    display = make_display(root)
    label = make_label(root)
    buttons = make_buttons(root)
    #root.mainloop()
    calculator = Calculator(root, label, display, buttons)
    calculator.start()

if __name__ == '__main__':
    main()