class Persona():
    #Metodo Contructor
    def __init__(self, Nombre, Edad, LNacimiento,CURP):
        self.Nombre = Nombre
        self.Edad = Edad
        self.LNacimiento = LNacimiento
        self.__CURP = CURP

        self.Vivo = True
        self.Discapacidad = False

    def accidente(self):
        gravedad = input("El accidente fue mortal [si/no]: ")
        if gravedad == "si":
            self.Vivo = False
        elif gravedad == "no":
            self.Discapacidad = True
        else:
            print("Introduzca un valor correcto")

    def setCURP(self): #setCURP
        valor = input("Ingrese el nuevo CURP: ")
        self.__CURP = valor
    

    def estatus(self):
        print("Nombre:",self.Nombre)
        print("Edad:",self.Edad)
        print("CURP:",self.__CURP)

        if self.Vivo == True:
            print("%s esta vivo" %(self.Nombre))
        else:
            print("%s no esta vivo" %(self.Nombre))


class Trabajador(Persona):
    def __init__(self, Nombre, Edad, LNacimiento,CURP,salario, puesto):
        super().__init__(Nombre, Edad, LNacimiento,CURP)
        self.salario = salario
        self.puesto = puesto

    def estatus(self):
        print("Nombre:",self.Nombre)
        print("Edad:",self.Edad)
        print("Puesto:",self.puesto)
        print("Salario:",self.salario)
        print("CURP:",self.CURP)

        if self.Vivo == True:
            print("%s esta vivo" %(self.Nombre))
        else:
            print("%s no esta vivo" %(self.Nombre))

class TrabajorTemporal(Trabajador):
    def __init__(self, Nombre, Edad, LNacimiento,CURP,salario, puesto, Contrato):
        super().__init__(Nombre, Edad, LNacimiento,CURP,salario, puesto)
        self.Contrato = Contrato


class Alumno(Persona):
    pass

Manuel = Persona("Manuel Lopez",25, "Sonora", "LOHM960117HDCLS05") #LOHM970117HDCLS05
Manuel.estatus()
#Manuel.setCURP()
#Manuel.estatus()
print("--------------")

Pedro = Trabajador("Pedro Lopez", 30, "Sonora", "LOHP901223HDCLS05",10000,"IT")
Pedro.estatus()
print("--------------")
Angel = Alumno("Angel Mtez", 16, "Sonora", "MARA040518HDCLS05")
Angel.estatus()
print("--------------")
Adrian = TrabajorTemporal("Adrian",16,"Mexico","OUHL",1000,"IT","Temporal")
Adrian.estatus()
print(Adrian.Contrato)
