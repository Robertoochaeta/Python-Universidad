class Aritmetica:   
    def __init__(self, operando1, operando2):
        self.operando1 =operando1
        self.operando2 =operando2
        
    def sumar(self):
       return self.operando1 + self.operando2
    def resta(self):
        return self.operando1 - self.operando2
#Creamos un nuevo objeto
aritmetica = Aritmetica(2,4)  
aritmetica = Aritmetica(6,6)   
print("RESULTADO DE LA SUMA" ,aritmetica.sumar())
print("Resultado De la resta: " , aritmetica.resta())

