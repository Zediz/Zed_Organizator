
import ttk
from Tkinter import *

v0 = Tk()
v0.config(bg = "white")
v0.title('Administracion de Ventas')
v0.geometry('700x500+290+150')

notebook = ttk.Notebook(v0)
notebook.pack(fill='both', expand='yes')
expec = ttk.Frame(notebook)
antig = ttk.Frame(notebook)
newc = ttk.Frame(notebook)

notebook.add(expec, text='Expediente del Cliente')
titulo = Label(expec,   text="Este es el expediente del cliente")
titulo.pack()

busqueda = Label(expec, text = "Busqueda de Cliente")
busqueda.pack()

entrythingy = Entry(expec,width=24)
entrythingy.pack()
contenido = StringVar()
entrythingy.config(textvariable = contenido)

expec1 = ttk.Frame(expec)


def imprimir ():
	print(contenido.get())

boton = Button(expec,  text="Buscar" ,command = lambda : imprimir() ) # El boton que lo situo en el frame de cambio de alarma y ejecuta 
boton.pack() # el metodo de cambio de la alarma


notebook.add(antig, text='Antiguedad de Documentos')
titulo = Label(antig,   text="Esta es la antiguedad de documentos", fg= "black")
titulo.pack()

notebook.add(newc, text= 'Nuevo Cliente')


v0.mainloop()