import turtle

class Circuito():
    corredores = []
    __turtleColor = ('blue','purple','red','orange')
    #pista
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width,height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -(width/2)+(2*(width/100))
        self.__finishLine = (width/2)-(2*(width/100))
        
        self.__crearTortugas(height/5)
        
    def __crearTortugas(self,posY):
        for i in range(4):
            newTurtle = turtle.Turtle()
            newTurtle.shape('turtle')
            newTurtle.color(self.__turtleColor[i])
            newTurtle.penup()
            newTurtle.setpos(self.__startLine,posY*(i+1)-(posY*2.5))
            newTurtle.pendown()
            self.corredores.append(newTurtle)

if __name__ == '__main__':
    circuito = Circuito(640,480)
    #barajas = Circuito(800,300)

    circuito.corredores[0].fd(50)
    circuito.corredores[1].fd(50)
    circuito.corredores[2].fd(50)
    circuito.corredores[3].fd(50)
