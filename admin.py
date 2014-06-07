#! /usr/bin/python
# -*- coding: utf-8 -*-

import ttk
import xlrd
import time, os
from Tkinter import *
from expdiente import *
from nuevo_cliente import *

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

newc = nuevoc(notebook) # FRAME NUEVO CLIENTE
notebook.add(newc, text= 'Nuevo Cliente')

#************* FRAME EXPEDIENTE DE CLIENTE
expe = expediente(notebook) #CREACION DE FRAME
notebook.add(expe, text='Expediente del Cliente')#AÑADIMOS FRAME AL NOTEBOOK

entrythingy = Entry (expe, width=10)
entrythingy.place(x=100,y=35)
contenido = StringVar()
entrythingy.config(textvariable = contenido)

botonsearch = Button(expe,  text="Buscar" , command = lambda : expe.buscar(contenido.get()) )
print contenido.get()
botonsearch.place(x=210, y = 35)

botonsave = Button(newc,  text="Guardar" , command = lambda : newc.guardar_nuevo() )
botonsave.place(x=210, y = 35)  







v0.mainloop()