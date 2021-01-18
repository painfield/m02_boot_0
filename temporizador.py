import time

def retrocontador(tiempo):
    if t != 0:
        print('{}, '.format(tiempo),end='')
        time.sleep(1) # Sleep for 1 second
        if tiempo > 0:
            retrocontador (tiempo-1)
        else:
            retrocontador (tiempo+1)
    else:
        print('¡¡¡BOOM!!!')
        
def sumatorio(numero):
    if numero != 0:
        return numero + sumatorio(numero-1)
    else:
        return 0
    
def factorial(numero):
    if numero != 0:
        return numero * factorial(numero-1)
    else:
        return 1

tipo = input('Elige el programa recursivo, sumatorio(s), factorial(f) o temporizador(t): ')
valor = input('Introduce el valor: ')
valor = int(valor)
if tipo == 't':
    retrocontador(valor)
if tipo == 's':
    print('Total: {}'.format(sumatorio(valor)))
if tipo == 'f':
    print('Factorial: {}'.format(factorial(valor)))