class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self): 
        return self.base * self.altura
    
base = int(input("Proporciona la base: ")) 
altura = int(input("Proporciobna la altura: "))

rectangulo = Rectangulo(base, altura)
print(rectangulo.calcular_area())

rectangulo1 = Rectangulo(4,2)
print(rectangulo1.calcular_area())