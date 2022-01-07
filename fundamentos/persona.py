class Persona:
    
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad

#Modificar valores
Persona.nombre = "Roberto"
Persona.edad= 20
#Acceder a los valores
print(Persona.nombre)
print(Persona.edad)

#Creacion de nuevo objeto
persona = Persona("Karla",30)
print(persona.nombre)
print(persona.edad)

#Segundo Objeto
persona2= Persona("Lupita",21)
print(persona2.nombre)
print(persona2.edad)