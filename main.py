from tkinter import *
from PIL import Image, ImageGrab
from tkinter import messagebox
from json import *
import diseñoSinRegistros
import diseñoListaPerfiles
import disenoAgregar

def json_read():
    """Leer datos de cada alumno."""
    first_read = ""
    with open('registro.json') as f:
        first_read = load(f)
        print(type(first_read))
        return len(first_read['alumnos'])


def windows_logic():
    """ Procesos y transiciones entre las ventanas."""
    if json_read() < 1:
        """AQUI VA LA VENTANA DE VACIO."""
        diseñoSinRegistros.root()
        disenoAgregar.Agregar()
    elif json_read() > 0:
        diseñoListaPerfiles.Lista()


windows_logic()
