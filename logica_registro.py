from json import *

dias = []
meses = []
anios = []
user_inputs = {'Nombre', 'Apellido Paterno',
               'Apellido Materno', 'Dia', 'Mes', 'Anio', 'Descripcion'}


def fill_lists():
    for dia in range(31):
        dias.append(dia)
    for mes in range(12):
        meses.append(mes)
    for anio in range(1990, 2020):
        anios.append(anio)


fill_lists()
