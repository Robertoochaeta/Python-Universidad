nombres = ["Roberto", "Anita", "Ronald", "Anabella"]
print(nombres) 
#Largo de la lista
print(len(nombres))
#Elemento 0
print(nombres[0])
print(nombres[1])
#navegación inversa
print(nombres [-1])
print(nombres[-2])

#Imprimir Rango
print(nombres[0:2]) #Sin incluir el indice 2
#Imprimir los elementos de inicio hasta el indice proporcionado
print(nombres[:3])#Sin incluir el indice 3 
#Imprimir elementos hasta el final
print(nombres[1:])
#Cambiar elementos
nombres[3]="Ivone"
print(nombres)
#iteracion
for nombre in nombres:
    print(nombre)
#Revisar un elemento 
if "Anita" in nombres:
    print("Anita si existe")    
else:
    print("El elemento buscado no existe en la lista")    
    
#Agregar un nuevo elemento
nombres.append("Lorenzo")
print(nombres)    
#Agregar un nuevo elemento en la parte especifica que querramos
nombres.insert(1,"Lili")
print(nombres)
#Remover un elemento
nombres.remove("Lili")
print(nombres)
#Remover el ultimo elemento de nuestra lista
nombres.pop()
print(nombres)
#Remover el indice indicado
del nombres[0]
print(nombres)
#Limpiar todos los elenetos
nombres.clear()
print(nombres)
del nombres
print(nombres)

numeros = [0,1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    if numero %3 ==0:
        print(numero)