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
    

    def func_egg(self):
        """PEQUENO EASTER EGG DE PRUEBA."""
        return messagebox.showinfo('Easter Egg', 'EL JAJAS ESTUVO AQUI XD')


app = App(root)
app.initial_window()


mainloop()
