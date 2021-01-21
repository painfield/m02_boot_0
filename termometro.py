class termometro():
    def __init__(self):
        self.__temperatura = 0
        self.__sistema = 'C'
        
    def __str__(self):
        return '{}º{}'.format(self.__temperatura,self.__sistema)
            
    def temperatura(self, temp=None):
        if temp == None:
            return self.__temperatura
        else:
            self.__temperatura = round(float(temp),1)
            return self.__temperatura
    
    def sistema(self, sist=None):
        if sist == None:
            return self.__sistema
        else:
            self.__sistema = sist.upper()
            return self.__sistema
            
    def __convertir(self,temp=None,sist=None):
        if sist == None:
            sist = self.__sistema
            if temp == None:
                temp = self.__temperatura
        if sist == 'F':
            self.__temperatura = round((temp-32)*5/9,1)
            self.__sistema = 'C'
            return (temp-32)*5/9
        else:
            return (temp*9/5)+32

def solicitar(objeto):
    objeto.temperatura(input('Temperatura: '))
    objeto.sistema(input('Sistema (C/F): '))
    
def unificar(objeto):
    if objeto.sistema() == 'F':
        print('{} = '.format(objeto),end='')
        objeto.__convertir()
        print(objeto)
    
def imprimir(temp,tempB):
    if temp >= tempB or temp < 0:
        diferencia = temp - tempB
    else:
        diferencia = -(tempB - temp)
    print('{:.1f}ºC - {:.1f}ºC = {:.1f}ºC con respecto al standard. '.format(temp,tempB,diferencia))
    if diferencia == 0:
        print('Temperatura perfecta')
            
termometroPaciente = termometro()
termometroExterior = termometro()
termometroSaludable = termometro()
termometroAgradable = termometro()

solicitar(termometroPaciente)
solicitar(termometroExterior)
termometroSaludable.temperatura(38)
termometroAgradable.temperatura(24)

unificar(termometroPaciente)
unificar(termometroExterior)
imprimir(termometroPaciente.temperatura(),termometroSaludable.temperatura())
imprimir(termometroExterior.temperatura(),termometroAgradable.temperatura())