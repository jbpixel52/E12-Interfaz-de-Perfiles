import os
from tkinter import *
from PIL import Image
from tkinter import messagebox
from logica_registro import *
class App:
    def __init__(self,master):
        self.frame = Frame(master, width = 1600, height = 900, bg='red')
        self.frame.pack()

        #self.register_window()
    def initial_window(self):
        top_frame = Frame(self.frame, bg='red')
        top_frame.pack(side=TOP)
        titulo = Label(top_frame,text='Alumnos', width=X, height=Y)
        titulo.pack(side=LEFT)

        quit_button = Button(top_frame, text = 'X',bg='red',command= self.frame.quit())
        quit_button.pack()
    def func_egg(self):
       return  messagebox.showinfo('Easter Egg','EL JAJAS ESTUVO AQUI XD')

    def fetch_text(self,arg):#funcion para leer el texto de los entry boxes de nombre
        return arg.get()
    def register_window(self):

        input_nombre =  Entry()
        input_nombre.pack()
        confirm_button = Button(state=DISABLED, Text='Haz click para confirmar nombre', command = self.func_egg())
        confirm_button.pack()


root= Tk()

app = App(root)
app.initial_window()


mainloop()
