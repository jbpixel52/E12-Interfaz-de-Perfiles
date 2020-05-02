import os
from tkinter import *
from PIL import Image, ImageGrab
from tkinter import messagebox
from logica_registro import *


root = Tk()
root.overrideredirect(True) # removes title bar

img = ImageGrab.grab()


def get_screen_size():
    temp = str(img.size)
    return temp.split('x')
user_w = get_screen_size()
user_h = get_screen_size()

get_screen_size()


class App:
    def __init__(self, master):
        self.frame = Frame(master, width=1600, height=900, bg="red")
        self.frame.pack(fill=X,expand=True)
        self.background = Canvas(master, bg='blue')
        self.background.pack(fill=X)


        # self.register_window()
    def initial_window(self):
        top_frame = Frame(self.frame, bg='green')
        top_frame.pack(side=TOP,fill=X,expand=True)
        titulo = Label(top_frame, text='Alumnos',bg='green')
        titulo.pack(side=LEFT)

        quit_button = Button(top_frame, text='X', bg='red',
                             command=root.destroy)
        quit_button.pack(side=RIGHT)

    def func_egg(self):
        return messagebox.showinfo('Easter Egg', 'EL JAJAS ESTUVO AQUI XD')

    def fetch_text(self, arg):  # funcion para leer el texto de los entry boxes de nombre
        return arg.get()

    def register_window(self):

        input_nombre = Entry()
        input_nombre.pack()
        confirm_button = Button(
            state=DISABLED, Text='Haz click para confirmar nombre', command=self.func_egg())
        confirm_button.pack()


app = App(root)
app.initial_window()


mainloop()
