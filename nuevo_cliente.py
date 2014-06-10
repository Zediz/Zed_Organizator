#! /usr/bin/python
# -*- coding: utf-8 -*-

import ttk
import time, os
from Tkinter import *
from xlrd import *
from xlutils.copy import copy
from dateutil import *
from datetime import *

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

		self.fenganchelabel = Label (self, text = "Fecha del Enganche ",font="Times 15 italic bold" )
		self.fenganchelabel.place(x= 300, y=365)

		self.fproxlabel = Label (self, text = "Fecha del Proximo pago ",font="Times 15 italic bold" )
		self.fproxlabel.place(x= 600, y=365)

		self.enganche = Label (self, text = "Enganche: ",font="Times 15 italic bold" )
		self.enganche.place(x= 30, y=395)
		self.enganchecuadro = Entry (self, width=10)
		self.enganchecuadro.place(x=130, y = 395)
		self.contenidoenganche = StringVar()
		self.enganchecuadro.config(textvariable = self.contenidoenganche)

		self.formadepago = Label (self, text = "Forma de Pago: ",font="Times 15 italic bold" )
		self.formadepago.place(x= 30, y=425)
		self.fpagocontenido = StringVar()
		self.fpago = OptionMenu(self,self.fpagocontenido,'Semanal','Quincenal','Mensual')
		self.fpago.config( width = 11)
		self.fpago.place(x=140,y=425)

		self.f2pago = Label (self, text = "Forma de Pago: ",font="Times 15 italic bold" )
		self.f2pago.place(x= 30, y=425)
		self.fpagocontenido = StringVar()
		self.fpago = OptionMenu(self,self.fpagocontenido,'Semanal','Quincenal','Mensual')
		self.fpago.config( width = 11)
		self.fpagocontenido.set('Semanal')
		self.fpago.place(x=140,y=425)

		self.diadepago = Label (self, text = "Dia de Pago: ",font="Times 15 italic bold" )
		self.diadepago.place(x= 30, y=455)
		self.dpagocontenido = StringVar()
		self.dpago = OptionMenu(self,self.dpagocontenido,'Domingo','Lunes','Martes','Miercoles','Jueves','Viernes', 'Sabado')
		self.dpagocontenido.set('Lunes')
		self.dpago.config( width = 11)
		self.dpago.place(x=140,y=455)

		#FECHA DEL ENGANCHE!!!!!!! 

		self.fechaenganche = Label (self, text = "Fecha: ",font="Times 15 italic bold" )
		self.fechaenganche.place(x= 230, y=395)

		#DIA

		self.dia = Entry (self, width=3)
		self.dia.place(x=285, y = 395)
		self.contenidodia = StringVar()
		self.dia.config(textvariable = self.contenidodia)

		#Mes
		self.contenidomes = StringVar()
		self.mes = OptionMenu(self,self.contenidomes,'Enero','Febrero','Marzo', 'Abril', 'Mayo','Junio', 'Julio','Agosto','Septiembre', 'Octubre', 'Noviembre','Diciembre')
		self.contenidomes.set('Enero')
		self.mes.config( width = 13)
		self.mes.place(x=320,y=395)

		#Año
		self.contenidoyear = StringVar()
		self.year = OptionMenu(self,self.contenidoyear,'2014','2015','2016', '2017', '2018','2019', '2020','2021','2022','2023')
		self.contenidoyear.set('2014')
		self.year.config( width = 7)
		self.year.place(x=450,y=395)

		#PROXIMO PAGOOOOO!!!!!

		self.diaprox = Entry (self, width=3)
		
		self.contenidodiaprox = StringVar()
		self.diaprox.config(textvariable = self.contenidodiaprox)
		self.diaprox.place(x=550, y = 395)

		#Mes
		self.contenidomesprox = StringVar()
		self.mesprox = OptionMenu(self,self.contenidomesprox,'Enero','Febrero','Marzo', 'Abril', 'Mayo','Junio', 'Julio','Agosto','Septiembre', 'Octubre', 'Noviembre','Diciembre')
		self.contenidomesprox.set('Enero')
		self.mesprox.config( width = 13)
		self.mesprox.place(x=585,y=395)
		

		#Año
		self.contenidoyearprox = StringVar()
		self.yearprox = OptionMenu(self,self.contenidoyearprox,'2014','2015','2016', '2017', '2018','2019', '2020','2021','2022','2023')
		self.contenidoyearprox.set('2014')
		self.yearprox.config( width = 7)
		self.yearprox.place(x=715,y=395)


		



		#Check Botton

		self.CheckVar1 = IntVar()
		self.C1 = Checkbutton(self, text = "Automatico", variable = self.CheckVar1,onvalue = 1, offvalue = 0,command=lambda : self.calendario())
		self.C1.place(x=550,y=425)


		

	def calendario(self):
		paloma = self.CheckVar1.get()

		if paloma == 1:
			self.diaprox.place_forget()
			self.mesprox.place_forget()
			self.yearprox.place_forget()
			self.yearprox.place_forget()
			self.C1.place(x=550,y=395)
			
			print self.CheckVar1.get()
		if paloma == 0:
			self.diaprox.place(x=550, y = 395)
			self.mesprox.place(x=585,y=395)
			self.yearprox.place(x=715,y=395)
			self.C1.place(x=550,y=425)
			
			print self.CheckVar1.get()


	def crear_fecha(self):
		mes = 0

		if self.contenidomes.get() == "Enero":
			mes = 1
		elif self.contenidomes.get() == "Febrero":
			mes = 2	
		elif self.contenidomes.get() == "Marzo":
			mes = 3	
		elif self.contenidomes.get() == "Abril":
			mes = 4	
		elif self.contenidomes.get() == "Mayo":
			mes = 5	
		elif self.contenidomes.get() == "Junio":
			mes = 6	
		elif self.contenidomes.get() == "Julio":
			mes = 7	
		elif self.contenidomes.get() == "Agosto":
			mes = 8	
		elif self.contenidomes.get() == "Septiembre":
			mes = 9	
		elif self.contenidomes.get() == "Octubre":
			mes = 10	
		elif self.contenidomes.get() == "Noviembre":
			mes = 11	
		elif self.contenidomes.get() == "Diciembre":
			mes = 12	

		#**********CREANDO FECHA!!!*************

		fechadada = date(int(self.contenidoyear.get()),mes,int(self.contenidodia.get()))

		return fechadada

	def crear_fechaprox(self):
		mes = 0

		if self.contenidomesprox.get() == "Enero":
			mes = 1
		elif self.contenidomesprox.get() == "Febrero":
			mes = 2	
		elif self.contenidomesprox.get() == "Marzo":
			mes = 3	
		elif self.contenidomesprox.get() == "Abril":
			mes = 4	
		elif self.contenidomesprox.get() == "Mayo":
			mes = 5	
		elif self.contenidomesprox.get() == "Junio":
			mes = 6	
		elif self.contenidomesprox.get() == "Julio":
			mes = 7	
		elif self.contenidomesprox.get() == "Agosto":
			mes = 8	
		elif self.contenidomeprox.get() == "Septiembre":
			mes = 9	
		elif self.contenidomesprox.get() == "Octubre":
			mes = 10	
		elif self.contenidomesprox.get() == "Noviembre":
			mes = 11	
		elif self.contenidomesprox.get() == "Diciembre":
			mes = 12	

		#**********CREANDO FECHA!!!*************

		fechadada = date(int(self.contenidoyearprox.get()),mes,int(self.contenidodiaprox.get()))

		return fechadada	


	def prox_pago(self):
		proxp = date(2014,10,11)
		fehcad= int(str(self.crear_fecha())[5:6])
		if self.fpagocontenido.get() == "Semanal":
			proxp = self.crear_fecha() + timedelta(days=7)
		elif self.fpagocontenido.get() == "Quincenal":
			if fehcad < 15:
				proxp = self.crear_fecha() + timedelta(days=(15 - fehcad))
			if fehcad >15:
				proxp = self.crear_fecha() + timedelta(days=(30 -fehcad))
		#elif self.fpagocontenido.get() == "Mensual"

		return proxp




	def guardar_nuevo (self):

		self.rb = open_workbook('data_new.xls')
		self.sh = self.rb.sheet_by_index(0)

		self.wb = copy(self.rb)
		self.resp = self.wb.save('data_ant.xls')

		self.ws = self.wb.get_sheet(0)

		print self.contenidovendedor.get()
		print str(self.sh.nrows)

		self.fila = self.sh.nrows

		

		


		
		#Escritura de los datos en la Hoja Data_new
		conta = 0
		while conta < 25:
			
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
				self.ws.write(self.fila,conta,self.contenidovendedor.get()) #FALTA EL 14 que es un espacio
			elif conta == 15:
				self.ws.write(self.fila,conta,self.contenidosaldooriginal.get())
			elif conta == 16:
				self.ws.write(self.fila,conta,self.contenidoenganche.get())
			elif conta == 17:
				self.ws.write(self.fila,conta,self.fpagocontenido.get()) # FALTA EL 18 Fecha del Segundo PAGO
			elif conta == 19:
				self.ws.write(self.fila,conta,self.dpagocontenido.get())
			elif conta == 20:
				self.ws.write(self.fila,conta,int(self.contenidosaldooriginal.get()) - int(self.contenidoenganche.get()))
			elif conta == 21:
				self.ws.write(self.fila, conta,str(self.crear_fecha()))
			elif conta == 23:
				if self.CheckVar1.get() == 1:
					self.ws.write(self.fila, conta, str(self.crear_fechaprox()))
				elif self.CheckVar1.get() == 0:
					self.ws.write(self.fila,conta,str(self.prox_pago()))
			

			conta = conta + 1


		print self.prox_pago()
		self.wb.save('data_new.xls')

		self.nombrecuadro.delete (0, END )
		self.celularcuadro.delete(0,END)
		self.telefonocuadro.delete (0, END )
		self.callecuadro.delete (0, END )
		self.numerocuadro.delete (0, END )
		self.coloniacuadro.delete (0, END )
		self.entrecallescuadro.delete (0, END )
		self.ciudadcuadro.delete (0, END )
		self.estadocuadro.delete (0, END )
		self.observcuadro.delete (0, END )
		self.ocupacioncuadro.delete (0, END )
		self.optometristacuadro.delete (0, END )
		self.vendedorcuadro.delete (0, END )
		self.saldooriginalcuadro.delete (0, END )
		self.enganchecuadro.delete (0, END )
		self.dia.delete (0, END )
		self.diaprox.delete (0, END )

		self.done = Label (self, text= "El cliente se guardo satisfactoriamente con el numero:")
		self.done.place(x=230,y=500)

		self.numcliente = Label (self,text = str(self.sh.nrows+1))
		self.numcliente.place(x=250,y=530)








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


