class Persona:
    def __init__(this, n,e):
        this.nombre = n
        this.edad = e
    def Desplegar(self):
        print("Nombre: ", self.nombre )    
        print("Edad: ", self.edad)
p1 = Persona('Roberto',29)
print(p1.nombre)
print(p1.edad)  

p1.Desplegar()      