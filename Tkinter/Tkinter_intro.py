import tkinter as tk
# Para poder utilizar las funciones tengo que nombrar a la libreria
from tkinter import*

# Creamos un objeto llamado raiz
raiz = Tk()
# Atributos del objeto raiz
# titulo
raiz.title("Pantalla Inicio")
# Geometroia => geometry("dimHxdimV")
raiz.geometry("400x600")
# Dimensionable => rezisable(False, False)
raiz.resizable(False,False)

lbl_titulo = Label(raiz, text = "Bienvenido", fg = "red")
lbl_titulo.pack()
Entry(master) # Cajita de texto
Button(master, text = "") # Botones
Frame(maste) # Crear contenedores




# Mostrar la pantalla
raiz.mainloop()
