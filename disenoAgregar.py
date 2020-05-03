import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont
from json import *
screenSize = {'width': 360, 'height': 640}

Agregar = tk.Tk()

datos = ""
personales = {}


def get_data():
    """HACER LOS DATOS UN DICT."""
    global personales
    personales["Nombre"] = myEntry1.get()
    personales["Apellido Paterno"] = myEntry2.get()
    personales["Apellido Materno"] = myEntry3.get()
    personales["Dia"] = myEntry4.get()
    personales["Mes"] = myEntry5.get()
    personales["Anio"] = myEntry6.get()
    personales["Descripcion"] = myEntry7.get()
    print('AGREGADOS')


def json_read():
    """Leer datos de cada alumno."""
    global datos
    with open('registro.json') as f:
        datos = load(f)
    print(datos)
    print(type(datos['alumnos']))
    datos['alumnos'].append(personales)
    for alumno in datos['alumnos']:
        print(alumno.get('Nombre'))


def json_write():
    """Agrega alumnos al json."""
    global datos
    global personales
    with open('registro.json', "w") as f:
        dump(datos, f, indent=2)


def data_proccesses():
    """ Todas las otras funciones de I/O."""
    get_data()
    json_read()
    json_write()
    Agregar.destroy

""" _______________ """

Agregar.title('Agregar')
Agregar.minsize(screenSize['width'], screenSize['height'])
Agregar.resizable(False, False)
im = ImageTk.PhotoImage(Image.open('ic_arrow_back.png').resize((24, 24)))

seccion1 = tk.Frame(master=Agregar, bg="green")
seccion1.place(relwidth=1.0, relheight=0.1, anchor=tk.NW)
seccion1.place_configure(relx=0, rely=0)

label1 = tk.Label(master=seccion1,
                  bg="green",
                  fg="white",
                  text="Agregar",
                  font=tkFont.Font(family='Roboto', size=20)
                  )
label1.place(anchor=tk.NW, relx=0.3, rely=0.2)

back = tk.Button(master=seccion1, bg='green', image=im, height=30, width=30, command=    Agregar.destroy
)
back.place(anchor=tk.NW, relx=0.1, rely=0.2)


seccion2 = tk.Frame(master=Agregar, bg="white")
seccion2.place(anchor=tk.NW, relwidth=1.0, relheight=0.9, relx=0, rely=0.1)

# Nombre
label2 = tk.Label(master=seccion2,
                  bg='white',
                  fg='green',
                  text="Nombre, Apellido paterno y Apellido materno",
                  font=tkFont.Font(family='Roboto', size=12)
                  )
label2.place(anchor=tk.NW, relx=0.055, rely=0.015)
myEntry1 = tk.Entry(master=seccion2, borderwidth=3, width=50)
myEntry1.place(anchor=tk.NW, relx=0.055, rely=0.080)
myEntry2 = tk.Entry(master=seccion2, borderwidth=3, width=50)
myEntry2.place(anchor=tk.NW, relx=0.055, rely=0.14)
myEntry3 = tk.Entry(master=seccion2, borderwidth=3, width=50)
myEntry3.place(anchor=tk.NW, relx=0.055, rely=0.20)

# Fecha de nacimiento
label3 = tk.Label(master=seccion2,
                  bg='white',
                  fg='green',
                  text="Fecha de nacimiento (Dia, Mes(01-12), Año)",
                  font=tkFont.Font(family='Roboto', size=12)
                  )
label3.place(anchor=tk.NW, relx=0.055, rely=0.30)

myEntry4 = tk.Entry(master=seccion2, borderwidth=3, width=10)
myEntry4.place(anchor=tk.NW, relx=0.055, rely=0.37)
myEntry5 = tk.Entry(master=seccion2, borderwidth=3, width=10)
myEntry5.place(anchor=tk.NW, relx=0.35, rely=0.37)
myEntry6 = tk.Entry(master=seccion2, borderwidth=3, width=10)
myEntry6.place(anchor=tk.NW, relx=0.65, rely=0.37)


# Descripcion
label4 = tk.Label(master=seccion2,
                  bg='white',
                  fg='green',
                  text="Descripcion",
                  font=tkFont.Font(family='Roboto', size=12)
                  )
label4.place(anchor=tk.NW, relx=0.055, rely=0.45)
myEntry7 = tk.Entry(master=seccion2, borderwidth=3, width=50)
myEntry7.place(anchor=tk.NW, relx=0.055, rely=0.50, height=150)

# Agregar

botonAgregar = tk.Button(master=seccion2, text='Agregar', bg='green',
                         fg='white', font=tkFont.Font(family='Roboto', size=14), command=data_proccesses)
botonAgregar.place(anchor=tk.CENTER, relx=0.5,
                   rely=0.9)

Agregar.mainloop()

