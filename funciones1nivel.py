def normal(x):
    return x

def cuadrado(x):
    return x*x

def cubo(x):
    return x**3

def sumaTodos(limitTo,f):
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
    return resultado

if __name__ == '__main__':
    print ('suma todos de 1 a 100:',sumaTodos(100, normal))
    print ('suma cuadrados de todos de 1 a 100:',sumaTodos(100, cuadrado))