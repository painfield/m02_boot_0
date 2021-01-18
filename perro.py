class Perro():
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def __str__(self):
        return 'perro: {}, {} años, {} kilos'.format(self.nombre,self.edad,self.peso)
        
    def ladrar(self):
        if self.peso >= 8:
            print('{}: GUAU, GUAU'.format(self.nombre))
        else:
            print('{}: guau, guau'.format(self.nombre))
        
tizon = Perro('Tizon',12,26.4)
chipi = Perro('Chipi',7,1.6)
lara = Perro('Lara',5,1.2)

print('{}, {} años, {} kilos'.format(tizon.nombre,tizon.edad,tizon.peso))
print(chipi)
print(lara)
tizon.ladrar()
chipi.ladrar()
lara.ladrar()