
import ttk
import xlrd
import time, os
from Tkinter import *

class expediente(Frame):

	def __init__(self, master):
			Frame.__init__(self, master)
			self.pack()

			self.titulo = Label (self, text = "Expediente del Cliente")
			self.titulo.place(x=1,y=1)

			# CUADRO DE BUSQUEDA

			self.busqueda = Label (self, text = "Busqueda: ",font="Times 15 italic bold" )
			self.busqueda.place(x=30,y=35)


			# NOMBRE

			self.nombre = Label(self, text = "Nombre: ",font="Times 15 italic bold" )
			self.nombre.place(x=30,y=65)
			self.nombreres = Label (self, text = "")
			self.nombreres.place(x = 90, y =67)
 
			# CELULAR

			self.celular = Label(self, text = "Celular: ",font="Times 15 italic bold" )
			self.celular.place(x=30,y=95)
			self.celularres = Label (self, text = "")
			self.celularres.place(x = 85, y =97)


			self.tel = Label(self, text = "Telefono de casa: ",font="Times 15 italic bold" )
			self.tel.place(x=215,y=95)
			self.telres = Label (self, text = "")
			self.telres.place(x = 330, y =97)


			#DIRECCION

			self.direccion = Label(self, text = "Direccion",font="Times 15 italic bold" )
			self.direccion.place(x=30,y=125)

			self.calle = Label(self, text = "Calle: ",font="Times 15 italic bold" )
			self.calle.place(x=30,y=155)
			self.calleres = Label(self, text = "")
			self.calleres.place(x=75,y=157)

			self.numero = Label (self, text = "No.: ",font="Times 15 italic bold" )
			self.numero.place(x= 385, y=155)
			self.numerores = Label (self, text = "")
			self.numerores.place(x=415, y = 157)

			self.colonia = Label (self, text = "Colonia: ",font="Times 15 italic bold" )
			self.colonia.place(x= 30, y=185)
			self.coloniares = Label (self, text = "")
			self.coloniares.place(x=90, y = 187)

			self.ciudad = Label (self, text = "Ciudad: ",font="Times 15 italic bold" )
			self.ciudad.place(x= 350, y=185)
			self.ciudadres = Label (self, text = "")
			self.ciudadres.place(x=405, y = 187)

			self.estado = Label (self, text = "Estado: ",font="Times 15 italic bold" )
			self.estado.place(x= 550, y=185)
			self.estadores = Label (self, text = "")
			self.estadores.place(x=610, y = 187)

			self.entrecalles = Label (self, text = "Entre Calles: ",font="Times 15 italic bold" )
			self.entrecalles.place(x= 30, y=215)
			self.entrecallesres = Label (self, text = "")
			self.entrecallesres.place(x=120, y = 217)

			self.observ = Label (self, text = "Observaciones: ",font="Times 15 italic bold" )
			self.observ.place(x= 30, y=245)
			self.observres = Label (self, text = "")
			self.observres.place(x=130, y = 247)

			self.ocupacion = Label (self, text = "Ocupacion: ",font="Times 15 italic bold" )
			self.ocupacion.place(x= 30, y=275)
			self.ocupacionres = Label (self, text = "")
			self.ocupacionres.place(x=110, y = 277)

			self.ocupacion = Label (self, text = "Optometrista: ",font="Times 15 italic bold" )
			self.ocupacion.place(x= 30, y=305)
			self.ocupacionres = Label (self, text = "")
			self.ocupacionres.place(x=120, y = 307)

			self.ocupacion = Label (self, text = "Vendedor: ",font="Times 15 italic bold" )
			self.ocupacion.place(x= 350, y=305)
			self.ocupacionres = Label (self, text = "")
			self.ocupacionres.place(x=420, y = 307)

cuent = 0
nom = 1
cel =2
tel =3
call =4 
nume = 5
colo = 6
entreca=7
ciud = 8
esta = 9
obser = 10
ocupa =11
opto = 12
vende =13
saldoor =15 
engan = 16
formpag =17
diadepag=18
deb=19
atras=20
ultabo=21
promes =22
cobra=23

book = xlrd.open_workbook("hello.xlsx") # Abrimos el archivo de excel
sh = book.sheet_by_index(0) # Nos situamos en la primer hoja

def buscar(contentry):
	dado=contentry
	print "Esto es lo que se escribio en el cuadro " + dado
	
	
	leido = "0" # Creamos una variable donde guardaremos lo que se lea en cada celda
	contador = 1

	while contador < int(sh.nrows):
		leido = sh.cell_value(colx=cuent , rowx = contador)
		leidoint = int(leido)

		if str(contentry) == str(leidoint):
			break
		else:
			contador = contador + 1

	
	print contador

	leer_todo(contador)

	contador = 0



def leer_todo(numerodecuenta):

	conta = 0
	while conta < 24 :

		print "Estos son todos los datos del cliente: "
		print conta, numerodecuenta
		print sh.cell_value(colx=conta, rowx = numerodecuenta)
		
		if conta == nom:
			ola.nombreres.config(text = sh.cell_value(colx=conta, rowx = numerodecuenta))
		elif conta == cel:
			ola.celularres.config(text = sh.cell_value(colx=conta, rowx = numerodecuenta))
		elif conta == tel:
			ola.telres.config(text = sh.cell_value(colx=conta, rowx = numerodecuenta))
		elif conta == call:
			ola.calleres.config(text = sh.cell_value(colx=conta, rowx = numerodecuenta))
		elif conta ==nume:
			ola.numerores.config(text = sh.cell_value(colx=conta, rowx = numerodecuenta))
		elif conta == colo:
			ola.coloniares.config(text = sh.cell_value(colx=conta, rowx = numerodecuenta))
		elif conta == entreca:
			ola.entrecallesres.config(text = sh.cell_value(colx=conta, rowx = numerodecuenta))
		elif conta == ciud:
			ola.ciudadres.config(text = sh.cell_value(colx=conta, rowx = numerodecuenta))
		elif conta == esta:
			ola.estadores.config(text = sh.cell_value(colx=conta, rowx = numerodecuenta))
		elif conta == obser:
			ola.observres.config(text = sh.cell_value(colx=conta, rowx = numerodecuenta))
		elif conta == ocupa:
			ola.ocupacionres.config(text = sh.cell_value(colx=conta, rowx = numerodecuenta))
		conta = conta + 1

	conta = 0	
















v0 = Tk()
v0.config(bg = "white")
v0.title('Administracion de Ventas')
v0.geometry('860x650+220+80')

notebook = ttk.Notebook(v0)
notebook.pack(fill='both', expand='yes')



antig = Frame(notebook)
newc = Frame(notebook)



ola = expediente(notebook)

boton = Button(ola,  text="Buscar" , command = lambda : buscar() )
boton.place(x=210, y = 35) 

notebook.add(ola, text='Expediente del Cliente')

notebook.add(antig, text='Antiguedad de Documentos')
titulo = Label(antig,   text="Esta es la antiguedad de documentos", fg= "black")
titulo.pack()

notebook.add(newc, text= 'Nuevo Cliente')



v0.mainloop()
#""""
