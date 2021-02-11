from tkinter import*

root = Tk()
root.title("Aplicacion")
root.geometry("500x600")
#root.resizable(False,False)

lbl_Titulo = Label(root,text = "Bienvenido a mi aplicacion")
lbl_Titulo.pack()
lbl_Titulo.config(font = ('Times New Roman',20))

lbl_subtitulo = Label(root, text = "Elige una opcion", font = ("arial",15))
lbl_subtitulo.place(x=30, y=50)

lbl_h3 = Label(root, text = "Sub Subtitulo", font = ("Consolas", 12))
lbl_h3.place(relx = 0.4, rely = 0.5)

txt_Titulo = Entry(root, font = ("Corbel", 12), fg = "#05A346") #show = "*"
txt_Titulo.insert(0,"Coloca nombre")
print(txt_Titulo.get()) # Obtener el texto que esta capturado en el Entry
txt_Titulo.delete(0,END)
txt_Titulo.place(relx = 0.35, rely = 0.55)


contenedor = Frame(root, bg = "blue", width = 400, height = 250)
contenedor.pack()

contenedor1 = Frame(root, bg = "red", width = 400, height = 250)
contenedor1.pack()

txt_text1 = Label(contenedor, text="Texto en contenedor 1 ", bg = "blue", fg = "white",font=("Arial",20))
txt_text1.place(x = 10, y = 20)

txt_text2 = Label(contenedor1, text="Texto en contenedor 2 ", bg = "red", font=("Arial",20))
txt_text2.place(x = 10, y = 20)


def saludar():
    print("Hola")

# Crear un boton
btn_prueba = Button(contenedor, text="Presioname", command = saludar)
btn_prueba.place(x = 20, y = 50)


root.mainloop()
