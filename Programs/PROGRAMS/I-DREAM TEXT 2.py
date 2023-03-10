import os 
from tkinter import *

#INITIALISATION FENETRE













#initialisation variable
#MENU PRINCIPALE
def suite(a):
    
    while True:
        fichier = open(a, 'r+')
        contenu = fichier.read()
        screen = tl.getscreen()
        a2 = screen.textinput(' TXT', contenu)
        if a2=='END' or a2=='SAVE' :
             break
        a3 = '\n' + a2
        try:
            import os

            fichier = open(a, 'r+')
            contenu = fichier.read()
            try:
                fichier.write(a3)
            except:
                print()
            text.insert(INSERT, a3)
            text.pack()
            fichier.close()
        finally :
            continue
    
import turtle as tl
import os
a = '''
>>>  TEXT <<<
   chose a file


  text 2022
 all rights reserved

>>> TEXT<<<
'''
#initialisation visible
root = Tk()
root.title(a)
c = Canvas(root, height=5000, width=5000)
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
save = Menu(menu)
menu.add_cascade(label='SAVE', menu=save)
save.add_command(label='SAVE')
helpmenu = Menu(menu)
menu.add_cascade(label='HELP', menu=helpmenu)
helpmenu.add_command(label='HELP by email')
helpmenu.add_command(label='HELP by docs')
coulleur = Menu(menu)
menu.add_cascade(label='Coulleur', menu=coulleur)
coulleur.add_command(label='ROUGE')
coulleur.add_command(label='BLEU')
coulleur.add_command(label='VERT', command=print('hello'))
from tkinter import *
text = Text(root, height=10, width=50)
text.pack()
screen = tl.getscreen()
a1 = screen.textinput(' text ', a)
with open(a1, "w") as fichier:
    fichier.write('')
    suite(a1)


os.chdir('C:/Users/louis/OneDrive/Programs/STARTIMG MENU = PROGRAMS/I-DREAM TEXT 2')
print('')
fichier = open('open.txt', 'r')
contenu = fichier.read()
c.create_text(50, 50, text=contenu)
c.pack()

