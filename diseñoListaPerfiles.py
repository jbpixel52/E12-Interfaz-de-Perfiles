import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont

screenSize = {'width': 360, 'height': 640}



Lista = tk.Tk()
Lista.title('Registrados')
Lista.minsize(screenSize['width'], screenSize['height'])
Lista.resizable(False, False)
im2 = ImageTk.PhotoImage( Image.open('Asset 1@2x.png').resize((44,48)) )

seccion1 = tk.Frame(master=Lista, bg="green")
seccion1.place(relwidth=1.0, relheight=0.1, anchor=tk.NW)
seccion1.place_configure(relx=0, rely=0)

label1 = tk.Label(master=seccion1,
    bg="green",
    fg="white",
    text="Alumnos",
    font=tkFont.Font(family='Roboto', size=20)
    )
label1.place(anchor=tk.NW, relx = 0.2, rely = 0.2)

seccion2 = tk.Frame(master=Lista, bg="white")
seccion2.place(anchor=tk.NW, relwidth=1.0, relheight=0.9, relx=0, rely=0.1)

label2 = tk.Label(master=seccion2,
    bg = 'white',
    fg = 'green',
    text= "Personas",
    font = tkFont.Font(family='Roboto', size = 14)
    )
label2.place(anchor=tk.NW, relx = 0.055, rely = 0.015)

foto1 = tk.Button(master=seccion2, image = im2)
foto1.place(anchor = tk.NW, relx = 0.055, rely = 0.1)
Nombre1 = tk.Label(master=seccion2, bg = 'white', fg = 'black', text = 'Moises Gana Obregon', font = tkFont.Font(family='Roboto', size = 10))
Nombre1.place(anchor = tk.NW, relx = 0.22, rely = 0.1)
Fecha1 = tk.Label(master=seccion2, bg = 'white', fg = 'gray', text = '17/02/1994', font = tkFont.Font(family='Roboto', size = 8))
Fecha1.place(anchor = tk.NW, relx = 0.22, rely = 0.15)

foto2 = tk.Button(master=seccion2, image = im2)
foto2.place(anchor = tk.NW, relx = 0.055, rely = 0.23)
Nombre2 = tk.Label(master=seccion2, bg = 'white', fg = 'black', text = 'Moises Gana Obregon', font = tkFont.Font(family='Roboto', size = 10))
Nombre2.place(anchor = tk.NW, relx = 0.22, rely = 0.23)
Fecha2 = tk.Label(master=seccion2, bg = 'white', fg = 'gray', text = '17/02/1994', font = tkFont.Font(family='Roboto', size = 8))
Fecha2.place(anchor = tk.NW, relx = 0.22, rely = 0.28)



foto3 = tk.Button(master=seccion2, image = im2)
foto3.place(anchor = tk.NW, relx = 0.055, rely = 0.36)
Nombre3 = tk.Label(master=seccion2, bg = 'white', fg = 'black', text = 'Moises Gana Obregon', font = tkFont.Font(family='Roboto', size = 10))
Nombre3.place(anchor = tk.NW, relx = 0.22, rely = 0.36)
Fecha3 = tk.Label(master=seccion2, bg = 'white', fg = 'gray', text = '17/02/1994', font = tkFont.Font(family='Roboto', size = 8))
Fecha3.place(anchor = tk.NW, relx = 0.22, rely = 0.41)




botonMas = tk.Button(master=seccion2,
    bg = 'green',
    fg = 'white',
    text = '+',
    font = tkFont.Font(family = 'Roboto', size = 15),
    width = 5)
botonMas.place(anchor = tk.SE, relx =0.99, rely = 0.99)


Lista.mainloop()