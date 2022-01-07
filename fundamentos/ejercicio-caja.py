class Caja:
    def __init__(self, alto,largo,ancho):
        self.alto=alto
        self.largo=largo
        self.ancho=ancho
    
    def Calcular_volumen(self):
        return self.alto * self.largo * self.ancho
        
alto = int(input("Ingrese la altura de la caja: "))
largo = int(input("Ingrese el largo de la caja: "))
ancho = int(input("Ingrese el ancho de la caja: "))


caja = Caja(alto,largo,ancho)
print(caja.Calcular_volumen())        
        
            