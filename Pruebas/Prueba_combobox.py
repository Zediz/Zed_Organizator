#! /usr/bin/python
# -*- coding: utf-8 -*

from Tkinter import *
#import tkMessageBox
import Tkinter

top = Tk()

fpagocontenido = StringVar()
fpago = OptionMenu(top,fpagocontenido,'Semanal','Quincenal','Mensual')
fpago.config( width = 11)
fpagocontenido.set('Semanal')

fpago.pack()

def imprimir():
	 print (fpagocontenido.get())

botonsearch = Button(top,  text="Buscar" , command = lambda : imprimir() )
botonsearch.pack()


	 


top.mainloop()