import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont

screenSize = {'width': 360, 'height': 640}



Perfil = tk.Tk()
Perfil.title('Perfil')
Perfil.minsize(screenSize['width'], screenSize['height'])
Perfil.resizable(False, False)
im = ImageTk.PhotoImage( Image.open('ic_arrow_back.png').resize((24,24)) )
im2 = ImageTk.PhotoImage( Image.open('Asset 1@2x.png').resize((118,128)) )

seccion1 = tk.Frame(master=Perfil, bg="green")
seccion1.place(relwidth=1.0, relheight=0.1, anchor=tk.NW)
seccion1.place_configure(relx=0, rely=0)

label1 = tk.Label(master=seccion1,
    bg="green",
    fg="white",
    text="Perfil",
    font=tkFont.Font(family='Roboto', size=20)
    )
label1.place(anchor=tk.NW, relx = 0.3, rely = 0.2)

back = tk.Button(master=seccion1, bg = 'green', image = im, height = 30, width = 30)
back.place(anchor = tk.NW, relx = 0.1, rely = 0.2)


seccion2 = tk.Frame(master=Perfil, bg="white")
seccion2.place(anchor=tk.NW, relwidth=1.0, relheight=0.9, relx=0, rely=0.1)

canvas1 = tk.Canvas(master=seccion2, width = 120, height = 130, bg = 'white', highlightbackground = 'white')
canvas1.place( anchor = tk.NW, relx = 0.05, rely = 0.05)
canvas1.create_image( 0,0, image = im2, anchor = tk.NW )

Nombre2 = tk.Label(master = seccion2, bg = 'white', fg = 'green', text = 'Moises Gana Obregon', font=tkFont.Font(family='Roboto', size=14))
Nombre2.place(anchor = tk.NW, relx = 0.4, rely = 0.1)
Fecha2 = tk.Label(master=seccion2, bg = 'white', fg = 'black', text = '17/02/1994', font = tkFont.Font(family='Roboto', size = 10))
Fecha2.place(anchor = tk.NW, relx = 0.4, rely = 0.15)

Descripcion = tk.Label(master=seccion2, bg = 'white', fg = 'green', text = 'Descripcion', font=tkFont.Font(family='Roboto', size=10))
Descripcion.place(anchor = tk.NW, relx = 0.05, rely = 0.35)
Descripcion2 = tk.Label(master=seccion2, bg = 'white', fg = 'black', text = 'Profesor de Cetys Universidad', font=tkFont.Font(family='Roboto', size=10))
Descripcion2.place(anchor = tk.NW, relx = 0.05, rely = 0.4)



Perfil.mainloop()