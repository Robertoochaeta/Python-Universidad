condicion = False
print("Condicion verdadera ") if condicion else print("Condicion falsa")
if condicion:
    print("La condicón es vedadera")
  
else:
    print("Condicion es falsa")
 
numero = int(input("Proporciona un numero entre 1 y 3"))
if numero == 1:
    numerotexto= "numero uno"
    
elif numero == 2:
    numerotexto = "numero dos"
  
elif numero == 3:
    numerotexto = "numero tres"
else:
    numerotexto = "Valor fuera de rango"
print("Numero proporcionado: ", numerotexto)                