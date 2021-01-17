from funciones1nivel import sumaTodos

doble = lambda x: x*2
triple = lambda x: x*3
cubo = lambda x: x**3
print('funciones lambda como variable sumaTodos x*2:',sumaTodos(3, doble))
print('funciones lambda como variable sumaTodos x*3:',sumaTodos(3, triple))
print('\n')

for i in range(1,101):
    print('funciones lambda sumaTodos limite='+str(i)+' x*'+str(i*2)+':',sumaTodos(i,lambda x: x*i*2))