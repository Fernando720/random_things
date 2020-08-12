from tkinter import *
from tkinter.ttk import *
#tkinter window
base = Tk()

#This button can close the window
button_1 = Button(base, text ="I close the Window", command = base.destroy)
#Exteral paddign for the buttons
button_1.pack(pady = 40)

#This button closes the first button
button_2 = Button(base, text ="I close the first button", command = button_1.destroy)
button_2.pack(pady = 40)

#This button closes the second button
button_3 = Button(base, text ="I close the second button", command = button_2.destroy)
button_3.pack(pady = 40)
mainloop()
