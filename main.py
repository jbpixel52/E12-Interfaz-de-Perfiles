from tkinter import *
from PIL import Image, ImageGrab
from tkinter import messagebox
from logica_registro import *

root = Tk()


def remove_title_bar():
    """Remueve la barra de titulo de Windows y la hace snap."""
    root.overrideredirect(True)  # removes title bar



class App:
    """CLASE donde se inicializa el programa."""

    def __init__(self, master):
        """INICIALIZACION DEL APP."""
        self.frame = Frame(master, width=1600, height=900, bg="red")
        self.frame.pack(fill=X, expand=True)
        self.background = Canvas(master, bg='blue')
        self.background.pack(fill=X)

    def initial_window(self):
        """INICIALIZACION DEL MAIN VIEW O INITIAL VIEW."""
        top_frame = Frame(self.frame, bg='green')
        top_frame.pack(side=TOP, fill=X, expand=True)
        titulo = Label(top_frame, text='Alumnos', bg='green')
        titulo.pack(side=LEFT)

        quit_button = Button(top_frame, text='X', bg='red',
                             command=root.destroy)  # ESTE BOTON DESTRUYE/CIERRA EL PROGRAMA
        quit_button.pack(side=RIGHT)
        confirm_button = Button(
            state=DISABLED, Text='Haz click para confirmar nombre',
            command=self.func_egg())
        confirm_button.pack(side=RIGHT)

    def func_egg(self):
        """PEQUENO EASTER EGG DE PRUEBA."""
        return messagebox.showinfo('Easter Egg', 'EL JAJAS ESTUVO AQUI XD')

    


app = App(root)
app.initial_window()


mainloop()
