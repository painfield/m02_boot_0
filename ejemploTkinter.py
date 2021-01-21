from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    
    def __init__(self,size='640x480',title='default',fondo='white'):
        Tk.__init__(self)
        
        self.geometry(size)
        self.title(title)
        self.configure(bg=fondo)
    
    def start(self):
        while True:
            self.mainloop()
            
    def __on_close(self):
        sys.exit()
    
if __name__ == '__main__':
    app = mainApp('1024x768','Mi ventana','lightblue')
    app.start()
    
ttk.Button
ttk.Radiobutton
ttk.Entry
