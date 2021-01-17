def maxim(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1, len(l)):
        if l[ix] > m:
            m = l[ix]
    return m

def minim(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1, len(l)):
        if l[ix] < m:
            m = l[ix]
    return m

def media(*l):
    if len(l) == 0:
        return 0
    suma = 0
    for valor in l:
        suma += valor
    return suma/len(l)

funciones = {
    'max':maxim,
    'min':minim,
    'med':media
    }

def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    return None

print('función en dirección de memoria:',returnF('max'))
print('máximo:',returnF('max')(1,3,-1,15,9))
print('función en dirección de memoria:',returnF('min'))
print('mínimo:',returnF('min')(1,3,-1,15,9))
print('función en dirección de memoria:',returnF('med'))
print('media:',returnF('med')(1,3,-1,15,9))