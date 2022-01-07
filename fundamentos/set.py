#Set es una coleccion sin Orden y tampoco tienen indices ni valores repetidos
#Y los elementos no se pueden modificar pero si agregar nuevos o eliminar

planetas = {"Marte", "Júpiter","Venus"}
print(planetas)
print(len(planetas))
#Revisar si un elemento está presente
print("Marte" in planetas)
#agregar
planetas.add("Tierra")
print(planetas)
#Eliminar elementos
planetas.remove("Tierra")
print(planetas)
planetas.discard("Júpiter")
print(planetas)
#Limpiar el set
planetas.clear()
print(planetas)
#Eliminar el set
del planetas
print(planetas)