from json import *
import diseñoAgregar as DA
dias = []
meses = []
anios = []
user_inputs = {'Nombre', 'Apellido Paterno',
               'Apellido Materno', 'Dia', 'Mes', 'Anio', 'Descripcion'}

datos = ""
personales = {}


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
    global personales
    personales["Nombre"] = fetch_text(DA.myEntry1)
    personales["Apellido Paterno"] = fetch_text(DA.myEntry2)
    personales["Apellido Materno"] = fetch_text(DA.myEntry3)
    personales["Dia"] = fetch_text(DA.myEntry4)
    personales["Mes"] = fetch_text(DA.myEntry5)
    personales["Año"] = fetch_text(DA.myEntry6)
    personales["Descripcion"]= fetch_text(DA.myEntry7)



def json_read():
    """Leer datos de cada alumno."""
    global datos
    with open('registro.json') as f:
        datos= load(f)
    print(datos)
    print(type(datos['alumnos']))
    datos['alumnos'].append(personales)
    for alumno in datos['alumnos']:
        print(alumno.get('Nombre'))


def json_write(arg):
    """Agrega alumnos al json."""
    global datos
    global personales
    datos['alumnos'].append(personales)
    with open('registro.json', "w") as f:
        dump(datos, f, indent=2)



fill_lists()

def data_proccesses():
    """ Todas las otras funciones de I/O."""
    get_data()
    json_read()
    json_write()
