#! /usr/bin/python
# -*- coding: utf-8 -*-

import ttk
import xlrd
import time, os
from Tkinter import *
from expdiente import *

v0 = Tk()
v0.config(bg = "white")
v0.title('Administracion de Ventas')
v0.geometry('860x650+220+80')

notebook = ttk.Notebook(v0)
notebook.pack(fill='both', expand='yes')

antig = Frame(notebook) #FRAME ANTIGUEDAD DE DOCUMENTOS
notebook.add(antig, text='Antiguedad de Documentos')
titulo = Label(antig,   text="Esta es la antiguedad de documentos", fg= "black")
titulo.pack()

newc = Frame(notebook) # FRAME NUEVO CLIENTE
notebook.add(newc, text= 'Nuevo Cliente')

#************* FRAME EXPEDIENTE DE CLIENTE
ola = expediente(notebook) #CREACION DE FRAME
notebook.add(ola, text='Expediente del Cliente')#AÑADIMOS FRAME AL NOTEBOOK

entrythingy = Entry (ola, width=10)
entrythingy.place(x=100,y=35)
contenido = StringVar()
entrythingy.config(textvariable = contenido)

boton = Button(ola,  text="Buscar" , command = lambda : buscar(contenido.get()) )
print contenido.get()
boton.place(x=210, y = 35) 







v0.mainloop()