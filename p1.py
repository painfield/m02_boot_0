def sumatodos(limitTo):
    resultado = 0
    for i in range(0,limitTo+1):
        resultado += i
        
    return resultado

print(sumatodos(100))