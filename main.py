import os
from tkinter import *
from PIL import Image
from tkinter import messagebox
from logica_registro import *
class App:
    def __init__(self,master):
            frame = Frame(master)
            frame.pack()

    def func_egg(self):
        messagebox.showinfo('Easter Egg','EL JAJAS ESTUVO AQUI XD')
    def register_window(self):
        main_frame = Frame()


root= Tk()

app = App(root)

mainloop()
