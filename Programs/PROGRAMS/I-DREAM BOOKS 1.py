from turtle import * #importe le module turtle
from tkinter import *
from time import*

f = Tk()
f.title('I-DREAM BOOKS')
t = Text(f, width=1000, height= 100)
t.insert(END, '''I-DREAM BOOKS


on
I-DREAM 1''')
t.pack()
try:
    import Tkinter as tk
except:
    import tkinter as tk
    

class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.root.geometry('1000x500')
       button = tk.Button(self.root, 
                          text = 'Click and Quit', 
                          command=self.quit)
       button.pack()
       self.root.mainloop()

   def quit(self):
       self.root.destroy()
        
app = Test()


