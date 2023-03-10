import os 
from tkinter import *
os.chdir('C:/Users/louis/Desktop')

#INITIALISATION FENETRE
class save():
    def _open_():
        from tkinter import Tk
        import tkinter.filedialog

        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = tkFileDialog.asksaveasfile(mode='r+', defaultextension=".idtxt") # show an "Open" dialog box and return the path to the selected file
        print(filename)
        a = filename.split('/')
        b = len(a)       
        file = open(a[b-1], mode='r')
        return file.read()
        print(file.read)
        file.close

class coulleur():
    def bleu():
        global couleur
        couleur = 'blue'
    def rouge():
        global couleur
        couleur = 'red'
    def vert():
        global couleur
        couleur = 'green'
    def violet():
        global couleur
        couleur = 'magenta'
    def rose():
        global couleur
        couleur = 'pink'
    def jaune():
        global couleur
        couleur = 'yellow'
    def orange():
        global couleur
        couleur = 'orange'
    def noir():
        global couleur
        couleur = 'black'
    def gris():
        global couleur
        couleur = 'grey'
class taillef():
    def taille8():
        global taile
        taile = 8
    def taille16():
        global taile
        taile = 16
    def taille24():
        global taile
        taile = 24
    def taille32():
        global taile
        taile = 32
    def taille40():
        global taile
        taile = 40
    def taille48():
        global taile
        taile = 48
    def taille56():
        global taile
        taile = 56
class Police():
    def Arial():
        global police
        police = 'Arial'
    def Verdana():
        global police
        police = 'Verdana'
    def Helvetica():
        global police
        police = 'Helvetica'
        
    def Courier():
        global police
        police = 'Courier'
    def MS_Serif():
        global police
        police = 'MS Serif'
    def MS_Sans_Serif():
        global police
        police = 'MS Sans Serif'
    def Calibri_Light():
        global police
        police = 'Calibri Light'
    def Cambria_Math():
        global police
        police = 'Cambria Math'
    def Consolas():
        global police
        police = 'Consolas'
    def Courier_New():
        global police
        police = 'Courier New'
    def Courier_New_Baltic():
        global police
        police = 'Courier New Baltic'
# Variables
global police
global taile
global couleur
police = 'Arial'
taile = '16'
couleur = 'black'
# Ouverture menu des classes
saveclass = save
coullleur = coulleur
tailllef = taillef
Police2 = Police













#initialisation variable
couleur = 'black'
#MENU PRINCIPALE
def suite(a):
    
    while True:
        import turtle as tl
        
        fichier = open(a, 'r+')
        contenu = fichier.read()
        screen = tl.getscreen()
        a2 = screen.textinput(' TXT', contenu)
        if a2=='QUIT':
            exit()
        try:
            a3 = a2 + '\n'
        except TypeError:
            print()
        try:
            import os

            fichier = open(a, 'r+')
            contenu = fichier.read()
            try:
                fichier.write(a3)
            except:
                print()
            text.config(fg=couleur)
            text.config(font=(police, taile))
            text.insert(INSERT, a3)
            text.pack()
            fichier.close()
        finally :
            continue
    
import turtle as tl
import os

#initialisation visible
root = Tk()
root.title('<<<I-DREAM text 3.2>>> UNSAVED*')
c = Canvas(root, height=5000, width=5000)
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...', command=saveclass._open_)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
coulllleur = Menu(menu)
menu.add_cascade(label='Coulleur', menu=coulllleur)
coulllleur.add_command(label='ROUGE', command=coullleur.rouge)
coulllleur.add_command(label='BLEU', command=coullleur.bleu)
coulllleur.add_command(label='VERT', command=coullleur.vert)
coulllleur.add_command(label='Rose', command=coullleur.rose)
coulllleur.add_command(label='Jaune', command=coullleur.jaune)
coulllleur.add_command(label='Noir', command=coullleur.noir)
coulllleur.add_command(label='Gris', command=coullleur.gris)
coulllleur.add_command(label='Violet', command=coullleur.violet)
coulllleur.add_command(label='Orange', command=coullleur.orange)


tailllle1 = Menu(menu)
menu.add_cascade(label='Taille de la fenètre', menu=tailllle1)
tailllle1.add_command(label='8', command=tailllef.taille8)
tailllle1.add_command(label='16', command=tailllef.taille16)
tailllle1.add_command(label='24', command=tailllef.taille24)
tailllle1.add_command(label='32', command=tailllef.taille32)
tailllle1.add_command(label='40', command=tailllef.taille40)
tailllle1.add_command(label='48', command=tailllef.taille48)
tailllle1.add_command(label='56', command=tailllef.taille56)


Police1 = Menu(menu)
menu.add_cascade(label='Police', menu=Police1)
Police1.add_command(label='Arial', command=Police2.Arial)
Police1.add_command(label='Verdana', command=Police2.Verdana)
Police1.add_command(label='Helvetica', command=Police2.Helvetica)
Police1.add_command(label='Courier', command=Police2.Courier)

Police1.add_command(label='MS Serif', command=Police2.MS_Serif)
Police1.add_command(label='MS Sans Serif', command=Police2.MS_Sans_Serif)
Police1.add_command(label='Calibri Light', command=Police2.Calibri_Light)
Police1.add_command(label='Cambria Math', command=Police2.Cambria_Math)
Police1.add_command(label='Consolas', command=Police2.Consolas)
Police1.add_command(label='Courier New', command=Police2.Courier_New)
Police1.add_command(label='Courier New Baltic', command=Police2.Courier_New_Baltic)



text = Text(root, height=10, width=50)
from tkinter import *
from tkinter import Tk
import tkinter.filedialog as tkFileDialog

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = tkFileDialog.asksaveasfile(mode='r+', defaultextension=".idtxt") # show an "Open" dialog box and return the path to the selected file
print(filename)
filename2 = filename.split('/')
filenamelen = len(filename2)
a1 = filename2[filenamelen-1]
import copy
filename4 = copy.deepcopy(filename2)
del filename4[filenamelen-1]
filename5 = "/".join(filename4)
os.chdir(filename5)
with open(a1, "w") as fichier:
    fichier.write('')
    suite(a1)




