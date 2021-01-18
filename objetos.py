import turtle
"""
def creaTortuga(nombre,color):
    object (nombre) = turtle.Turtle()
    nombre.shape('turtle')
    nombre.color(color)
    """
def recta(nombre,distancia,velocidad=3):
    nombre.speed(velocidad)
    for i in range(10):
        nombre.fd(distancia/5)
        if i%2 == 0:
            nombre.left(i*2)
        else:
            nombre.right(i*2)
    nombre.speed(3)
    
def curvaI(nombre,grados=45,distancia=90,velocidad=3):
    nombre.speed(velocidad)
    for i in range(grados):
        nombre.left(1)
        nombre.fd(distancia/grados)
    nombre.speed(3)

def curvaD(nombre,grados=45,distancia=90,velocidad=3):
    nombre.speed(velocidad)
    for i in range(grados):
        nombre.right(1)
        nombre.fd(distancia/grados)
    nombre.speed(3)

tortuga = {'leonardo':'blue','donatello':'purple','raphael':'red','michaelangelo':'orange'}
#for nombre,color in tortuga.index():
#    creaTortuga(nombre,color)


leonardo = turtle.Turtle()
leonardo.shape('turtle')
leonardo.color('blue')

print(leonardo.speed())

donatello = turtle.Turtle()
donatello.shape('turtle')
donatello.color('purple')

raphael = turtle.Turtle()
raphael.shape('turtle')
raphael.color('red')

michaelangelo = turtle.Turtle()
michaelangelo.shape('turtle')
michaelangelo.color('orange')

recta(leonardo,150,5)
recta(donatello,160,4)
recta(raphael,140)
recta(michaelangelo,145)
curvaI(leonardo,190,500,500)
curvaI(donatello,195,500,500)
curvaI(raphael,170,50,500)
recta(leonardo,80)
recta(donatello,80)
recta(raphael,130)
curvaI(leonardo,12,80)
curvaI(donatello,10,90)
recta(leonardo,120)
recta(donatello,120)
curvaI(leonardo,50,80)
curvaI(donatello,55,100)
recta(leonardo,120)
recta(donatello,120)
