#a = int(input("Proporciona un valor: "))
#a=3
#valorMinimo=0
#valorMaximo=5
#dentroRango= (a >= valorMinimo and a <=valorMaximo)
#print(dentroRango)
#if(dentroRango):
 #   print("Dentro de rango")
#else:
 #   print("Fuera de rango")    
    
#vacaciones = False
#diaDescanso = False

#if(vacaciones or diaDescanso):
 #   print("Puedes ir al parque")
#else:
 #   print("No puedes salir")
    
#print(not (vacaciones))
#vacaciones = True
#diaDescanso = False

#if(not(vacaciones or diaDescanso)):
#    print("No puedes salir")
#else:
 #   print("Puedes ir al parque")
 
 
alto=int(input("Proporciona un valor: "))
ancho=int(input("Proporciona el ancho: " ))
area = alto * ancho          
perimetro=  alto **2 + ancho **2

print("El area del cuadrado es: ", area , "Y el perimetro es: " , perimetro)        

num1 =int(input("Introduce el numero 1 "))
num2 = int(input("Introduce el numero 2"))
if(num1 > num2):
    print(" El numero 1 es el mayor")
else:
    print("El numero 2 es mayor ")        
