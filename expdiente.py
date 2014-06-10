
import ttk
import xlrd
import time, os
from Tkinter import *
from dateutil.relativedelta import *
from dateutil.rrule import *
from datetime import *

class expediente(Frame):
	def __init__(self, master):
			Frame.__init__(self, master)
			self.pack()

			self.logo = Canvas (self,height = 120, width =230, bg="white")
			self.logo.place(x=550,y=10)

			self.file_logo = PhotoImage(file="logo_optica.gif")
			self.logo.create_image(115,60, image =self.file_logo)

			"""self.tabla = Canvas (self,height = 120, width =740, bg="white")
			self.tabla.place(x=30,y=370)

			self.file = PhotoImage(file="tabla_img.gif")
			self.tabla.create_image(370,60, image =self.file)"""

			#Variables y lectura de archivo
			self.cuent = 0
			self.nom = 1
			self.cel =2
			self.tel =3
			self.call =4 
			self.nume = 5
			self.colo = 6
			self.entreca=7
			self.ciud = 8
			self.esta = 9
			self.obser = 10
			self.ocupa =11
			self.opto = 12
			self.vende =13
			self.saldoor =15 
			self.engan = 16
			self.formpag =17
			self.fech2pag=18
			self.diadepag=19
			self.deb=20
			self.atras=22
			self.ultabo=21
			self.promes =23
			self.cobra=24

			self.book = xlrd.open_workbook("data_new.xls") # Abrimos el archivo de excel
			self.sh = self.book.sheet_by_index(0) # Nos situamos en la primer hoja

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


			self.telefono = Label(self, text = "Telefono de casa: ",font="Times 15 italic bold" )
			self.telefono.place(x=215,y=95)
			self.telefonores = Label (self, text = "")
			self.telefonores.place(x = 330, y =97)


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

			self.optometrista = Label (self, text = "Optometrista: ",font="Times 15 italic bold" )
			self.optometrista.place(x= 30, y=305)
			self.optometristares = Label (self, text = "")
			self.optometristares.place(x=120, y = 307)

			self.vendedor = Label (self, text = "Vendedor: ",font="Times 15 italic bold" )
			self.vendedor.place(x= 350, y=305)
			self.vendedorres = Label (self, text = "")
			self.vendedorres.place(x=420, y = 307)

			# DATOS DE PAGOS

			self.saldooriginal = Label (self, text = "Saldo \nOriginal: ",font="Times 15 italic bold" )
			self.saldooriginal.place(x= 30, y=370)
			self.saldooriginalres = Label (self, text = "")
			self.saldooriginalres.place(x=33, y = 415)

			self.enganche = Label (self, text = "Enganche: ",font="Times 15 italic bold" )
			self.enganche.place(x= 115, y=370)
			self.engancheres = Label (self, text = "")
			self.engancheres.place(x=120, y = 415)

			self.formapago = Label (self, text = "Forma de \nPago: ",font="Times 15 italic bold" )
			self.formapago.place(x= 205, y=370)
			self.formapagores = Label (self, text = "")
			self.formapagores.place(x=205, y = 415)

			self.diadepago = Label (self, text = "Dia de Pago: ",font="Times 15 italic bold" )
			self.diadepago.place(x= 300, y=370)
			self.diadepagores = Label (self, text = "")
			self.diadepagores.place(x=325, y = 415)

			self.debe = Label (self, text = "Debe: ",font="Times 15 italic bold" )
			self.debe.place(x= 400, y=370)
			self.deberes = Label (self, text = "")
			self.deberes.place(x=390, y = 415)

			self.atraso = Label (self, text = "Atraso: ",font="Times 15 italic bold" )
			self.atraso.place(x= 460, y=370)
			self.atrasores = Label (self, text = "")
			self.atrasores.place(x=465, y = 415)

			self.ultimoabono = Label (self, text = "Ultimo \nabono: ",font="Times 15 italic bold" )
			self.ultimoabono.place(x= 560, y=370)
			self.ultimoabonores = Label (self, text = "")
			self.ultimoabonores.place(x=565, y = 415)

			self.promesapago = Label (self, text = "Promesa de \npago: ",font="Times 15 italic bold" )
			self.promesapago.place(x= 695, y=370)
			self.promesapagores = Label (self, text = "")
			self.promesapagores.place(x=700, y = 415)




	def buscar(self,contentry):

		self.book = xlrd.open_workbook("data_new.xls") # Abrimos el archivo de excel
		self.sh = self.book.sheet_by_index(0)

		dado=contentry
		#print "Esto es lo que se escribio en el cuadro " + dado	
				
		leido = "0" # Creamos una variable donde guardaremos lo que se lea en cada celda
		contador = 1

		while contador < int(self.sh.nrows):
			leido = self.sh.cell_value(colx=self.cuent , rowx = contador)
			leidoint = int(leido)

			if str(contentry) == str(leidoint):
				break
			else:
				contador = contador + 1

				
		#print contador

		self.leer_todo(contador)

		contador = 0

	def atrasos(self,numerodecuenta):

		fechastr = self.sh.cell_value(colx=self.ultabo, rowx = numerodecuenta)
		fechaobj = date(int(fechastr[0:4]),int(fechastr[5:7]), int(fechastr[8:10]))
		now =date.today()
		formadepago=self.sh.cell_value(colx=17, rowx = numerodecuenta)
		atraso = self.time_between(fechaobj,now,self.sh.cell_value(colx=17, rowx = numerodecuenta))
		print "Esta es la forma de pago" , formadepago
		if self.sh.cell_value(colx=17, rowx = numerodecuenta) == "Quincenal":
			atraso = atraso * 2
		
		return atraso

	def time_between(self,start,end,fpago):
		atraso = ""

		if fpago == "Semanal":	
			atraso = rrule(WEEKLY,dtstart=start,until =end)
			print "fue semanal"
		elif fpago == "Quincenal":
			atraso = rrule(MONTHLY,dtstart=start,until =end)
		elif fpago == "Mensual":
			atraso = rrule(MONTHLY,dtstart=start,until =end)

		print "Este es el atraso de time between" ,atraso
		return atraso.count()


	def leer_todo(self,numerodecuenta):
		self.book = xlrd.open_workbook("data_new.xls") # Abrimos el archivo de excel
		self.sh = self.book.sheet_by_index(0)

		conta = 0
		while conta < 25 :

			#print "Estos son todos los datos del cliente: "
			##print conta, numerodecuenta
			#print self.sh.cell_value(colx=conta, rowx = numerodecuenta)
			
			if conta == self.nom:
				self.nombreres.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.cel:
				celif = int(self.sh.cell_value(colx=conta, rowx = numerodecuenta))
				self.celularres.config(text = str(celif))
			elif conta == self.tel:
				telif = int(self.sh.cell_value(colx=conta, rowx = numerodecuenta))
				self.telefonores.config(text = str(telif))
			elif conta == self.call:
				self.calleres.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta ==self.nume:
				numif = int(self.sh.cell_value(colx=conta, rowx = numerodecuenta))
				self.numerores.config(text = str(numif))
			elif conta == self.colo:
				self.coloniares.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.entreca:
				self.entrecallesres.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.ciud:
				self.ciudadres.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.esta:
				self.estadores.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.obser:
				self.observres.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.ocupa:
				self.ocupacionres.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.opto:
				self.optometristares.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.vende:
				self.vendedorres.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
		#******DATOS DE COMPRA********
			elif conta == self.saldoor:
				self.saldooriginalres.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.engan:
				self.engancheres.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.formpag:
				self.formapagores.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.diadepag:
				self.diadepagores.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.deb:
				self.deberes.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.atras:
				##print numerodecuenta
				self.atrasores.config(text = self.atrasos(numerodecuenta))
			elif conta == self.ultabo:
				self.ultimoabonores.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))
			elif conta == self.promes:
				self.promesapagores.config(text = self.sh.cell_value(colx=conta, rowx = numerodecuenta))

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
