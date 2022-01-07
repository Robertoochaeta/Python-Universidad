print("Proporciona los siguientes datos del libro: ")
nombre =input("Proporciona el nombre: ")
id =int(input("Proporciona el ID del Libro: "))
precio=float(input("Proporciona el precio del libro: "))

envioGratuito = input("Indica si el envio es gratuito (True/False)")


if envioGratuito =="True":
    envioGratuito =True
    
elif envioGratuito=="False":
    envioGratuito =False
else:
    envioGratuito = "Valor Incorrecto Debe ser True O False"        

print("Nombre:", nombre)
print("Id:", id)
print("Precio: ", precio)
print("Envio Gratuito?: ", envioGratuito)    

print(type(envioGratuito))