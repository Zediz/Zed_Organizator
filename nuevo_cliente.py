#! /usr/bin/python
# -*- coding: utf-8 -*-

import ttk
import time, os
from Tkinter import *
from xlrd import *
from xlutils.copy import copy

class nuevoc(Frame):
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.pack()

		self.logo = Canvas (self,height = 120, width =230, bg="white")
		self.logo.place(x=550,y=10)

		self.file_logo = PhotoImage(file="logo_optica.gif")
		self.logo.create_image(115,60, image =self.file_logo)

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
		self.diadepag=18
		self.deb=19
		self.atras=20
		self.ultabo=21
		self.promes =22
		self.cobra=23

		# Abrimos y hacemos una copia del archivo



		

		#***************************************************

		self.titulo = Label (self, text = "Agregar Nuevo Cliente")
		self.titulo.place(x=1,y=1)

			# CUADRO DE BUSQUEDA

		self.busqueda = Label (self, text = "Busqueda: ",font="Times 15 italic bold" )
		self.busqueda.place(x=30,y=35)


			# NOMBRE

		self.nombre = Label(self, text = "Nombre: ",font="Times 15 italic bold" )
		self.nombre.place(x=30,y=65)
		self.nombrecuadro = Entry (self, width=10)
		self.nombrecuadro.place(x = 90, y =67)
		self.contenidonombre = StringVar()
		self.nombrecuadro.config(textvariable = self.contenidonombre)
 
			# CELULAR

		self.celular = Label(self, text = "Celular: ",font="Times 15 italic bold" )
		self.celular.place(x=30,y=95)
		self.celularcuadro = Entry (self, width=10)
		self.celularcuadro.place(x = 85, y =97)
		self.contenidocelular = StringVar()
		self.celularcuadro.config(textvariable = self.contenidocelular)


		self.telefono = Label(self, text = "Telefono de casa: ",font="Times 15 italic bold" )
		self.telefono.place(x=215,y=95)
		self.telefonocuadro = Entry (self, width=10)
		self.telefonocuadro.place(x = 330, y =97)
		self.contenidotelefono = StringVar()
		self.telefonocuadro.config(textvariable = self.contenidotelefono)


			#DIRECCION

		self.direccion = Label(self, text = "Direccion",font="Times 15 italic bold" )
		self.direccion.place(x=30,y=125)

		self.calle = Label(self, text = "Calle: ",font="Times 15 italic bold" )
		self.calle.place(x=30,y=155)
		self.callecuadro = Entry (self, width=10)
		self.callecuadro.place(x=75,y=157)
		self.contenidocalle = StringVar()
		self.callecuadro.config(textvariable = self.contenidocalle)

		self.numero = Label (self, text = "No.: ",font="Times 15 italic bold" )
		self.numero.place(x= 385, y=155)
		self.numerocuadro = Entry (self, width=10)
		self.numerocuadro.place(x=415, y = 157)
		self.contenidonumero= StringVar()
		self.numerocuadro.config(textvariable = self.contenidonumero)

		self.colonia = Label (self, text = "Colonia: ",font="Times 15 italic bold" )
		self.colonia.place(x= 30, y=185)
		self.coloniacuadro = Entry (self, width=10)
		self.coloniacuadro.place(x=90, y = 187)
		self.contenidocolonia = StringVar()
		self.coloniacuadro.config(textvariable = self.contenidocolonia)

		self.ciudad = Label (self, text = "Ciudad: ",font="Times 15 italic bold" )
		self.ciudad.place(x= 350, y=185)
		self.ciudadcuadro = Entry (self, width=10)
		self.ciudadcuadro.place(x=405, y = 187)
		self.contenidociudad = StringVar()
		self.ciudadcuadro.config(textvariable = self.contenidociudad)

		self.estado = Label (self, text = "Estado: ",font="Times 15 italic bold" )
		self.estado.place(x= 550, y=185)
		self.estadocuadro = Entry (self, width=10)
		self.estadocuadro.place(x=610, y = 187)
		self.contenidoestado = StringVar()
		self.estadocuadro.config(textvariable = self.contenidoestado)

		self.entrecalles = Label (self, text = "Entre Calles: ",font="Times 15 italic bold" )
		self.entrecalles.place(x= 30, y=215)
		self.entrecallescuadro = Entry (self, width=10)
		self.entrecallescuadro.place(x=120, y = 217)
		self.contenidoentrecalles = StringVar()
		self.entrecallescuadro.config(textvariable = self.contenidoentrecalles)

		self.observ = Label (self, text = "Observaciones: ",font="Times 15 italic bold" )
		self.observ.place(x= 30, y=245)
		self.observcuadro = Entry (self, width=10)
		self.observcuadro.place(x=130, y = 247)
		self.contenidoobserv = StringVar()
		self.observcuadro.config(textvariable = self.contenidoobserv)

		self.ocupacion = Label (self, text = "Ocupacion: ",font="Times 15 italic bold" )
		self.ocupacion.place(x= 30, y=275)
		self.ocupacioncuadro = Entry (self, width=10)
		self.ocupacioncuadro.place(x=110, y = 277)
		self.contenidoocupacion = StringVar()
		self.ocupacioncuadro.config(textvariable = self.contenidoocupacion)

		self.optometrista = Label (self, text = "Optometrista: ",font="Times 15 italic bold" )
		self.optometrista.place(x= 30, y=305)
		self.optometristacuadro = Entry (self, width=10)
		self.optometristacuadro.place(x=120, y = 307)
		self.contenidooptometrista = StringVar()
		self.optometristacuadro.config(textvariable = self.contenidooptometrista)

		self.vendedor = Label (self, text = "Vendedor: ",font="Times 15 italic bold" )
		self.vendedor.place(x= 350, y=305)
		self.vendedorcuadro = Entry (self, width=10)
		self.vendedorcuadro.place(x=420, y = 307)
		self.contenidovendedor = StringVar()
		self.vendedorcuadro.config(textvariable = self.contenidovendedor)

		self.saldooriginal = Label (self, text = "Saldo Original: ",font="Times 15 italic bold" )
		self.saldooriginal.place(x= 30, y=365)
		self.saldooriginalcuadro = Entry (self, width=10)
		self.saldooriginalcuadro.place(x=130, y = 365)
		self.contenidosaldooriginal = StringVar()
		self.saldooriginalcuadro.config(textvariable = self.contenidosaldooriginal)

		self.enganche = Label (self, text = "Enganche: ",font="Times 15 italic bold" )
		self.enganche.place(x= 30, y=395)
		self.enganchecuadro = Entry (self, width=10)
		self.enganchecuadro.place(x=130, y = 395)
		self.contenidoenganche = StringVar()
		self.enganchecuadro.config(textvariable = self.contenidoenganche)

		self.formadepago = Label (self, text = "Forma de Pago: ",font="Times 15 italic bold" )
		self.formadepago.place(x= 30, y=395)
		self.enganchecuadro = Entry (self, width=10)
		self.enganchecuadro.place(x=130, y = 395)
		self.contenidoenganche = StringVar()
		self.enganchecuadro.config(textvariable = self.contenidoenganche)

	def guardar_nuevo (self):

		self.rb = open_workbook('data_new.xls')
		self.sh = self.rb.sheet_by_index(0)

		self.wb = copy(self.rb)
		self.resp = self.wb.save('data_ant.xls')

		self.ws = self.wb.get_sheet(0)

		print self.contenidovendedor.get()
		print str(self.sh.nrows)

		self.fila = self.sh.nrows

		conta = 0
		while conta < 24:
			
			if conta == 0:
				self.ws.write(self.fila,conta,self.fila)
			elif conta == 1:
				self.ws.write(self.fila,conta,self.contenidonombre.get())
			elif conta == 2:
				self.ws.write(self.fila,conta,self.contenidocelular.get())
			elif conta == 3:
				self.ws.write(self.fila,conta,self.contenidotelefono.get())
			elif conta == 4:
				self.ws.write(self.fila,conta,self.contenidocalle.get())
			elif conta == 5:
				self.ws.write(self.fila,conta,self.contenidonumero.get())
			elif conta == 6:
				self.ws.write(self.fila,conta,self.contenidocolonia.get())
			elif conta == 7:
				self.ws.write(self.fila,conta,self.contenidoentrecalles.get())
			elif conta == 8:
				self.ws.write(self.fila,conta,self.contenidociudad.get())
			elif conta == 9:
				self.ws.write(self.fila,conta,self.contenidoestado.get())
			elif conta == 10:
				self.ws.write(self.fila,conta,self.contenidoobserv.get())
			elif conta == 11:
				self.ws.write(self.fila,conta,self.contenidoocupacion.get())
			elif conta == 12:
				self.ws.write(self.fila,conta,self.contenidooptometrista.get())
			elif conta == 13:
				self.ws.write(self.fila,conta,self.contenidovendedor.get())

			conta = conta + 1



		self.wb.save('data_new.xls')







v0 = Tk()
v0.config(bg = "white")
v0.title('Administracion de Ventas')
v0.geometry('860x650+220+80')

notebook = ttk.Notebook(v0)
notebook.pack(fill='both', expand='yes')



antig = Frame(notebook)
newc = Frame(notebook)



ola = nuevoc(notebook)

boton = Button(ola,  text="Buscar" , command = lambda : ola.guardar_nuevo() )
boton.place(x=210, y = 35) 

notebook.add(ola, text='Expediente del Cliente')

notebook.add(antig, text='Antiguedad de Documentos')
titulo = Label(antig,   text="Esta es la antiguedad de documentos", fg= "black")
titulo.pack()

notebook.add(newc, text= 'Nuevo Cliente')



v0.mainloop()


