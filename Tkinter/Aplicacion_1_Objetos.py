from tkinter import*

class Pantalla(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(width = 500, height = 700)


        self.btn_salir = Button(self, text = "Cerrar", font = ("Arial", 20))
        self.btn_salir.config(command = lambda:self.cerrar_aplicacion(master))
        self.btn_salir.place(relx = 0.80, rely = 0.9)

        self.lbl_titulo = Label(self, text = "Titulo",font = ("Arial", 30))
        self.lbl_titulo.place(relx = 0.4, rely = 0.1)

        self.pack()

    # Metodo de la super clase para cerrar
    def cerrar_aplicacion(self, padre):
        padre.destroy()



class pantalla_inicio(Pantalla):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg = "#d5d5db")

        self.btn_login = Button(self, text="Ingresar", bg="gold", command = lambda:self.cambio_a_ingreso(master))
        self.btn_login.config(font = ("arial",16))
        self.btn_login.place(relx = 0.25, rely = 0.5)

        self.btn_registrar = Button(self, text="Registrar", bg="gold", command = lambda:self.cambio_a_registro(master))
        self.btn_registrar.config(font = ("arial",16))
        self.btn_registrar.place(relx = 0.75, rely = 0.5)

    def cambio_a_ingreso(self, padre):
        self.destroy()
        login = pantalla_ingreso(padre)

    def cambio_a_registro(self, padre):
        self.destroy()
        registro = pantalla_registro(padre)

class pantalla_ingreso(Pantalla):
    def __init__(self, master):
        super().__init__(master)

        self.mensaje = Label(self, text = "Esta es la pantalla de Login", font = ("Corbel",16))
        self.mensaje.place(relx = 0.4, rely = 0.5)


class pantalla_registro(Pantalla):
    def __init__(self,master):
        super().__init__(master)

        self.mensaje = Label(self, text = "Registrate", font = ("Corbel",16))
        self.mensaje.place(relx = 0.4, rely = 0.1)

        self.nombre = Label(self, text="Nombre").place(relx = 0.25, rely = 0.4)
        self.edad = Label(self, text="Edad").place(relx = 0.25, rely = 0.5)
        self.CURP = Label(self, text="CURP").place(relx = 0.25, rely = 0.6)

        self.txt_nombre = Entry(self)
        self.txt_nombre.place(relx = 0.5, rely = 0.4)
        self.txt_edad = Entry(self)
        self.txt_edad.place(relx = 0.5, rely = 0.5)
        self.txt_CURP = Entry(self)
        self.txt_CURP.place(relx = 0.5, rely = 0.6)

        self.btn_registro = Button(self, text="Crear registro", command = self.registrar)
        self.btn_registro.place(relx = 0.4, rely = 0.8)

    def registrar(self):
        pass




root = Tk()
root.title("Primera Aplicacion")
root.geometry("600x800")
# Instancial mi clase pantalla para rear la pantalla de inicio de mi aplicacion
aplicacion = pantalla_inicio(root)
aplicacion.mainloop()
