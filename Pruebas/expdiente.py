
import ttk
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

			boton = Button(self,  text="Buscar" ,)#command = lambda : ) # El boton que lo situo en el frame de cambio de alarma y ejecuta 
			boton.place(x=210, y = 35) # el metodo de cambio de la alarma

			self.entrythingy = Entry (self, width=10)
			self.entrythingy.place(x=100,y=35)
			self.contenido = StringVar()
			self.entrythingy.config(textvariable = self.contenido)

			# NOMBRE

			self.nombre = Label(self, text = "Nombre: ",font="Times 15 italic bold" )
			self.nombre.place(x=30,y=65)
			self.nombreres = Label (self, text = "Panfilo Filomeno Gerardo Martinez Rodriguez")
			self.nombreres.place(x = 90, y =67)

			# CELULAR

			self.celular = Label(self, text = "Celular: ",font="Times 15 italic bold" )
			self.celular.place(x=30,y=95)
			self.celularres = Label (self, text = "8333188723")
			self.celularres.place(x = 85, y =97)


			self.tel = Label(self, text = "Telefono de casa: ",font="Times 15 italic bold" )
			self.tel.place(x=215,y=95)
			self.telres = Label (self, text = "8333188723")
			self.telres.place(x = 330, y =97)


			#DIRECCION

			self.direccion = Label(self, text = "Direccion",font="Times 15 italic bold" )
			self.direccion.place(x=30,y=125)

			self.calle = Label(self, text = "Calle: ",font="Times 15 italic bold" )
			self.calle.place(x=30,y=155)
			self.calleres = Label(self, text = "Avenida Revolucion de las americas ixtapalapa")
			self.calleres.place(x=75,y=157)

			self.numero = Label (self, text = "No.: ",font="Times 15 italic bold" )
			self.numero.place(x= 385, y=155)
			self.numerores = Label (self, text = "4004")
			self.numerores.place(x=415, y = 157)

			self.colonia = Label (self, text = "Colonia: ",font="Times 15 italic bold" )
			self.colonia.place(x= 30, y=185)
			self.coloniares = Label (self, text = "Revolucion Mexicana de San lorenzo")
			self.coloniares.place(x=90, y = 187)

			self.ciudad = Label (self, text = "Ciudad: ",font="Times 15 italic bold" )
			self.ciudad.place(x= 350, y=185)
			self.ciudadres = Label (self, text = "Tampico")
			self.ciudadres.place(x=405, y = 187)

			self.estado = Label (self, text = "Estado: ",font="Times 15 italic bold" )
			self.estado.place(x= 550, y=185)
			self.estadores = Label (self, text = "Baja California Norte")
			self.estadores.place(x=610, y = 187)

			self.entrecalles = Label (self, text = "Entre Calles: ",font="Times 15 italic bold" )
			self.entrecalles.place(x= 30, y=215)
			self.entrecallesres = Label (self, text = "Baja California Norte")
			self.entrecallesres.place(x=120, y = 217)

			self.observ = Label (self, text = "Observaciones: ",font="Times 15 italic bold" )
			self.observ.place(x= 30, y=245)
			self.observres = Label (self, text = "Esta a dos cuadras del la colonia militar, entre un puesto de pollos y un puesto de barbacoa")
			self.observres.place(x=130, y = 247)

			self.ocupacion = Label (self, text = "Ocupacion: ",font="Times 15 italic bold" )
			self.ocupacion.place(x= 30, y=275)
			self.ocupacionres = Label (self, text = "Trabajador de HAcienda")
			self.ocupacionres.place(x=110, y = 277)

			self.ocupacion = Label (self, text = "Optometrista: ",font="Times 15 italic bold" )
			self.ocupacion.place(x= 30, y=305)
			self.ocupacionres = Label (self, text = "Gerardo Martinez Antonio Lopez")
			self.ocupacionres.place(x=120, y = 307)

			self.ocupacion = Label (self, text = "Vendedor: ",font="Times 15 italic bold" )
			self.ocupacion.place(x= 350, y=305)
			self.ocupacionres = Label (self, text = "Gerardo Martinez Antonio Lopez")
			self.ocupacionres.place(x=420, y = 307)

















v0 = Tk()
v0.config(bg = "white")
v0.title('Administracion de Ventas')
v0.geometry('860x650+220+80')

notebook = ttk.Notebook(v0)
notebook.pack(fill='both', expand='yes')

antig = Frame(notebook)
newc = Frame(notebook)

ola = expediente(notebook)

notebook.add(ola, text='Expediente del Cliente')

notebook.add(antig, text='Antiguedad de Documentos')
titulo = Label(antig,   text="Esta es la antiguedad de documentos", fg= "black")
titulo.pack()

notebook.add(newc, text= 'Nuevo Cliente')



v0.mainloop()
#""""
