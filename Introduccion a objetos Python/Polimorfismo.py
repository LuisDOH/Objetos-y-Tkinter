class Persona():
    def descripcion(self):
        print("Soy una persona y vivo en sociedad")

class Trabajador(Persona):
    def descripcion(self):
        print("Soy un trabajador y me desarrollo en una empresa")

class Empleado(Trabajador):
    def descripcion(self):
        print("Soy un empleado y estoy a su servicio")

class Alumno(Persona):
    def descripcion(self):
        print("Soy un alumno y mi rol es estudiar")


entidad1 = Persona()
entidad2 = Trabajador()
entidad3 = Alumno()
entidad4 = Empleado()

entidad1.descripcion()
entidad2.descripcion()
entidad3.descripcion()
entidad4.descripcion()

print("---------------------")

def obtenerDescripcion(objeto):
    objeto.descripcion()


obtenerDescripcion(entidad4)
