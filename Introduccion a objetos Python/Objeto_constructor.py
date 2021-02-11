class PC():
    # Atributos que se pueden definir al crear el objeto
    # Metodo Contructor
    def __init__(self, Marca, Modelo, Memoria):
        self.__Marca = Marca
        self.Modelo = Modelo
        self.Memoria = Memoria

        # Atributos que contienen valores por defecto
        self.Encendido = False
        self.Temperatura = 25
        self.__SO = "Windows"
        self.Funcional = False

    def encender(self):
        self.__revisar()
        if self.Encendido == True:
            print("Esta PC ya esta encendida")

        elif self.Encendido == False and self.Funcional == True:
            self.Encendido = True

    def apagar(self):
        if self.Encendido == False:
            print("Esta PC ya esta apagada!!")
        else:
            self.Encendido = False

    def __revisar(self):
        self.Funcional = True
        print("El equipo esta listo para usarse")


    def estatus(self):
        print("La marca de esta PC es:", self.__Marca)
        print("La Modelo de esta PC es:", self.Modelo)
        print("La Memoria de esta PC es:", self.Memoria)
        print("La Temperatura de esta PC es:", self.Temperatura)
        print("El sistema operativo de esta PC es: ", self.__SO)
        if self.Encendido: # if self.Encendido == True:
            print("La PC esta encendida")
        else:
            print("La PC esta apagada")

    # Metodos get y set
    #Modificar el valor del atributo privado SO
    def setSO_Marca(self, SisOp, NMarca):
        self.__SO = SisOp
        self.__Marca = NMarca

    #Retorna el valor del atributo privado SO
    def getSO(self):
        return self.__SO

# Crear nuestros objetos
PCEscritorio = PC("Toshiba", "Satellite", 16)
#print(PCEscritorio.Marca)
print(PCEscritorio.Temperatura)
PCEscritorio.Temperatura = 30
print(PCEscritorio.Temperatura)
#PCEscritorio.Marca = "Samsung"
#print(PCEscritorio.Marca)

PCEscritorio.setSO_Marca("MACOS","Apple")
PCEscritorio.estatus()

PCEscritorio.encender()
print(PCEscritorio.Encendido)
#PCEscritorio.__revisar()
