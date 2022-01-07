import math
def CalculaRaiz(num1):
    if num1 <0: 
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)
op1=int(input("Introduce un Numero: ")) 
try:
    print(CalculaRaiz(op1))
    
except ValueError as Errordenumeronegativo:
    print(Errordenumeronegativo) 
print("Programa Terminado")          