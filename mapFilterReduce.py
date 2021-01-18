from functools import reduce

def sumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor
        
    return resultado

def sumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor*2
        
    return resultado

def productoTotal(l):
    resultado = 0
    for valor in l:
        resultado *= valor
    return resultado

def doble(x):
    return x+x

lista = [1,3,-1,15,8]

listaDobles = list(map(lambda x: x*2,lista))
listaDobles1 = list(map(doble,lista))

def esPar(x):
    return x%2 == 0

listaPares = list(filter(lambda x: x%2 == 0,lista))
listaPares1 = list(filter(esPar,lista))
sumatorio = reduce(lambda x,y:x+y,lista)

lis=lista[:] #creo copia de la lista
lis.insert(0,0) #añado el neutro para la suma en la posición cero, con esto corrijo el reduce sumatorioDobles

sumatorioDobles = reduce(lambda x,y:x+y*2,lis)
multiplicatorio = reduce(lambda x,y:x*y,lista)
suma100 = reduce(lambda x,y: x+y, range(101))

print('lista:',lista)
print('mapeado *2=',list(listaDobles))
print('filtrado %2=',list(listaPares))
print('mapeado *3 y filtrado %2=',list(filter(lambda x: x%2 == 0,list(map(lambda x: x*3,lista)))))
print('reducido(sumado)=',sumatorio)
print('reducido(*2 y sumado)=',sumatorioDobles)
print('sumatorio doble clásico:',sumatorioDobleClasico(lista))
print('reducido(multiplicado)=',multiplicatorio)
print('suma100:',suma100)