import os
from tkinter import *
from PIL import Image
from tkinter import messagebox
class App:
    def __init__(self,master):
            frame = Frame(master)
            frame.pack()
            self.button= Button(frame,text='X',fg='blue',command = frame.quit())
            self.button.pack(side=BOTTOM)

            self.easter_egg = Button(frame,text='JIJI',fg='pink',command = self.func_egg)
            self.easter_egg.pack(side= TOP)
    def func_egg(self):
        messagebox.showinfo('Easter Egg','EL JAJAS ESTUVO AQUI XD')

root= Tk()

app = App(root)

mainloop()
