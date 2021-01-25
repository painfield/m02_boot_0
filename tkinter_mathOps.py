from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title('Calculón')
        self.geometry('200x130')
        self.configure(bg='#f0f0f0')
        #self.configure(bg='#000')
        self.resizable(0,0)
        
        self.valor1 = StringVar(name='valor1',value='')
        self.valor2 = StringVar(name='valor2',value='')
        self.valores = {'valor1':self.valor1,'valor2':self.valor2}
        self.__valorAnterior = {'valor1':'','valor2':''}
        self.valor1.trace('w',self.validateEntry)
        self.valor2.trace('w',self.validateEntry)
        self.valor1.trace('w',self.calculate)
        self.valor2.trace('w',self.calculate)
        self.suma = StringVar(name='suma',value=0)
        self.rest = StringVar(name='resta',value=0)
        self.prod = StringVar(name='producto',value=0)
        self.divi = StringVar(name='division',value=0)
        self.createLayout()
        
    def createLayout(self):
        self.entrada1 = ttk.Entry(self,textvariable=self.valor1,width=14).place(x=10,y=10)
        self.entrada2 = ttk.Entry(self,textvariable=self.valor2,width=14).place(x=100,y=10)
        ttk.Label(self,text='suma').place(x=10,y=40)
        ttk.Label(self,textvariable=self.suma).place(x=10,y=60)
        ttk.Label(self,text='resta').place(x=10,y=80)
        ttk.Label(self,textvariable=self.rest).place(x=10,y=100)
        ttk.Label(self,text='producto').place(x=100,y=40)
        ttk.Label(self,textvariable=self.prod).place(x=100,y=60)
        ttk.Label(self,text='división').place(x=100,y=80)
        ttk.Label(self,textvariable=self.divi).place(x=100,y=100)

    def validateEntry(self,*args):
        valor = self.valores[args[0]]
        valorNuevo = valor.get()
        #print('valorAnterior =',self.__valorAnterior[args[0]])
        #print('nombre = {} | valor = {}'.format(valor,valor.get()))    
        #print('valor anterior = {} | valor nuevo = {}\n'.format(self.__valorAnterior[args[0]],valorNuevo))
        try:
            float(valorNuevo)
            if valorNuevo.find(' ') > 0 or valorNuevo[:1] == ' ':
                valor.set(self.__valorAnterior[args[0]])
            else:
                self.__valorAnterior[args[0]] = valorNuevo
        except:
            if valorNuevo == '' or valorNuevo == '-':
                self.__valorAnterior[args[0]] = valorNuevo
            else:
                valor.set(self.__valorAnterior[args[0]])
                
    def calculate(self,*args):
        if self.valor1.get() != '' and self.valor2.get() != '':
            #print('self.valor1.get() =',self.valor1.get())
            #print('self.valor2.get() =',self.valor2.get())
            val1 = float(self.valor1.get())
            val2 = float(self.valor2.get())
            #print('val1 =',val1)
            #print('val2 =',val2)
            self.suma.set(round(val1 + val2,2))
            self.rest.set(round(val1 - val2,2))
            self.prod.set(round(val1 * val2,2))
            self.divi.set(round(val1 / val2,2))
        
    def start(self):
        while True:
            self.mainloop()
    
if __name__ == '__main__':
    app = mainApp()
    app.start()