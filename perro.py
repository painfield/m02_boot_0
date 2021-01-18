class Dog():
    def __init__(self):
        self.nombre = ''
        self.edad = None
        self.peso = None
        
    def ladrar(self):
        if self.peso == None:
            print('Soy un fantasma')
        elif self.peso >= 8:
            print('{}: GUAU, GUAU'.format(self.nombre))
        else:
            print('{}: guau, guau'.format(self.nombre))

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

class PerroAsistencia(Perro):
    def __init__(self,nombre,edad,peso,amo):
        Perro.__init__(self,nombre,edad,peso)
        self.amo = amo
        self.__trabajando = False
    
    def __str__(self):
        return 'perro as. de {}: {}, {} años, {} kilos'.format(self.amo,self.nombre,self.edad,self.peso)
    
    def pasear(self):
        self.__trabajando = True
        print('{}: ayudo a mi dueño {} a pasear'.format(self.nombre,self.amo))
        
    def volver(self):
        self.__trabajando = False
        print('{}: vuelvo con {} de pasear'.format(self.nombre,self.amo))
        
    def ladrar(self):
        if self.__trabajando:
            print('Estoy de servicio')
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
        
chipi = Perro('Chipi',7,1.6)
lara = Perro('Lara',5,1.2)
rantamplan = PerroAsistencia('Rantamplan',4,21.3,'Lucky Luke')

print('{}, {} años, {} kilos'.format(chipi.nombre,chipi.edad,chipi.peso))
print(chipi)
print(lara)
print(rantamplan)

chipi.ladrar()
lara.ladrar()
rantamplan.ladrar()
rantamplan.pasear()
rantamplan.ladrar()
rantamplan.volver()
print(rantamplan.trabajando())
rantamplan.ladrar()
rantamplan.trabajando(True)
print(rantamplan.trabajando())
rantamplan.ladrar()

miko = Dog()
miko.nombre = 'Miko'
miko.ladrar()
miko.peso = 3
miko.ladrar()
