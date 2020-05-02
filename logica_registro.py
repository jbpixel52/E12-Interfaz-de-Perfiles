from json import *

dias = []
meses = []
anios = []
user_inputs = {'Nombre', 'Apellido Paterno',
               'Apellido Materno', 'Dia', 'Mes', 'Anio', 'Descripcion'}


def fill_lists():
    """Rellana las listas de opciones."""
    for dia in range(31):
        dias.append(dia)
    for mes in range(12):
        meses.append(mes)
    for anio in range(1990, 2020):
        anios.append(anio)

def fetch_text(arg):
        """

        Funcion para leer el texto de los entry boxes de nombre.

        PARAMETRO:
        arg: este argumento es cualquier Entry widget
        regresa lo que este dentro.

        """
        return arg.get()

def get_data():
    """ HACER LOS DATOS UN DICT."""
    nombre =  fetch_text()


def json_read():
    """Descripcion."""
    with open('registro.json', "r") as write_file:
        datos = dumps('alumnos')

fill_lists()
