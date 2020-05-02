from tkinter import *
from PIL import Image, ImageGrab
from tkinter import messagebox
from logica_registro import *

root = Tk()
root.resizable(False, False)
root.geometry("360x640")
root.title('REGISTRO DE ALUMNOS')


def remove_title_bar():
    """Remueve la barra de titulo de Windows y la hace snap."""
    root.overrideredirect(True)  # removes title bar


class App:
    """CLASE donde se inicializa el programa."""

    def __init__(self, master):
        """INICIALIZACION DEL APP."""
        titulo = Label(master,text='USUARIOS',width=20,bg="lawn green").grid(
            row=0, column=0, columnspan=3, sticky=NW)

        label_fill_name = Label(master, text='NOMBRE:').grid(
            row=1, column=0, columnspan=1, sticky=W)
        fill_name = Entry(master, bg='salmon').grid(
            row=1, column=2, columnspan=2)
        

    def initial_window(self):
        """INICIALIZACION DEL MAIN VIEW O INITIAL VIEW."""

        """
        quit_button = Button(self.frame, text='X', bg='tomato',
                             command=root.destroy)  # ESTE BOTON DESTRUYE/CIERRA EL PROGRAMA
        quit_button.pack(side=RIGHT)"""

    def func_egg(self):
        """PEQUENO EASTER EGG DE PRUEBA."""
        return messagebox.showinfo('Easter Egg', 'EL JAJAS ESTUVO AQUI XD')


app = App(root)
app.initial_window()


mainloop()
