import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont

screenSize = {'width': 360, 'height': 640}


root = tk.Tk()
root.title('Registro')
root.minsize(screenSize['width'], screenSize['height'])
root.resizable(False, False)
im = ImageTk.PhotoImage(Image.open('not_found.png').resize((200, 200)))

seccion1 = tk.Frame(master=root, bg="green")
seccion1.place(relwidth=1.0, relheight=0.1, anchor=tk.NW)
seccion1.place_configure(relx=0, rely=0)



label1 = tk.Label(master=seccion1,
                  bg="green",
                  fg="white",
                  text="Alumnos",
                  font=tkFont.Font(family='Roboto', size=20)
                  )
label1.place(anchor=tk.NW, relx=0.2, rely=0.2)

seccion2 = tk.Frame(master=root, bg="white")
seccion2.place(anchor=tk.NW, relwidth=1.0, relheight=0.9, relx=0, rely=0.1)

label2 = tk.Label(master=seccion2,
                  bg='white',
                  fg='green',
                  text="Personas",
                  font=tkFont.Font(family='Roboto', size=14)
                  )
label2.place(anchor=tk.NW, relx=0.055, rely=0.015)

canvas = tk.Canvas(master=seccion2,
                   bd=2,
                   bg='white',
                   height=300,
                   width=300,
                   highlightbackground='white'
                   )
canvas.place(anchor=tk.CENTER, relx=0.5, rely=0.5)
canvas.create_image(60, 40, image=im, anchor=tk.NW)
label3 = tk.Label(master=canvas,
                  text="Sin registros",
                  bg='white',
                  fg='gray',
                  font=tkFont.Font(family='Roboto', size=15)
                  )
label3.place(anchor=tk.CENTER, relx=0.5, rely=0.8)

boton = tk.Button(master=seccion2,
                  bg='green',
                  fg='white',
                  text='+',
                  font=tkFont.Font(family='Roboto', size=15),
                  width=5, command = root.destroy)
boton.place(anchor=tk.SE, relx=0.99, rely=0.99)

root.mainloop()
