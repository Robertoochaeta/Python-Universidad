frutas = ("Naranja", "Plátano", "Guayaba")
print(frutas)
#Largo de la tupla
print(len(frutas))
#Accediendo a un elemento
print(frutas[0])
#Navegacion inversa
print(frutas[-1])
#Rango
print(frutas[0:2])#Excluye el indice 2
frutasLista= list(frutas)
frutasLista[1]="Platanito"
frutas= tuple(frutasLista)
print(frutas) 

for fruta in frutas:
    print(fruta,end=" ")
f