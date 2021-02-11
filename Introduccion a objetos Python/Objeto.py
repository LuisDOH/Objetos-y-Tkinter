class Computadora():
    # Atributos
    Marca = "Dell"
    Memoria = 8 #GB
    Color = "Gris"
    Precio = 10000

    # Metodos
    def encender(self):
        print("El equipo se esta encendiendo")

    def reiniciar(self):
        print("El equipo se esta reiniciando")

    def apagarse(self):
        print("El equipo se esta apagando")

# Instanciar nuestra clase => Un objeto
computadora_1 = Computadora()
print("La marca de computadora_1 es:",computadora_1.Marca)
computadora_1.Marca = "Leonovo"
print("La marca de computadora_1 es:",computadora_1.Marca)
print("El color de computadora_1 es:",computadora_1.Color)

computadora_1.encender()

PCGamer       = Computadora()
print("La memoria de PCGamer es:",PCGamer.Memoria)
PCGamer.Memoria = 16
print("La memoria de PCGamer es:",PCGamer.Memoria)
print("El precio de PCGamer es:",PCGamer.Precio)
PCGamer.reiniciar()
