#Un diccionario esta compuesto de valle, valor (key,value)
diccionario ={
    "IDE": "Integrated Development Enviroment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}
print(diccionario)
#Largo
print(len(diccionario))
#Accediendo a un elemento
print(diccionario["IDE"])
#Otra forma de acceder 
print(diccionario.get("IDE"))
#Modificando valores
diccionario["IDE"] ="Integrated development environment"
print(diccionario)
#iterar
for termino in diccionario:
    print(termino)
for termino in diccionario:
    print(diccionario[termino]) 
for valor in diccionario.values():
    print(valor)        
#comprobar si un elemento existe
print("IDE" in diccionario)
print(diccionario)    

#Agregar nuevos elementos
diccionario ["PK"] ="Primary Key"
print(diccionario)
#Remover Elementos
diccionario.pop("DBMS")
print(diccionario)
#Limpiar 
diccionario.clear()
print(diccionario)
#Eliminar diccionario
del diccionario
