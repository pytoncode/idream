# I-DREAM écrit entre 2020-2021 2021-2022 2022-2023

# Définition des espaces:
# 5 espace entre les fonctions
# 10 espace entre les bloc spéciaux des fonction
# Un écrant blanc entre les Groupes
# Rubant blanc et rouge "A ne surtout pas manqué
# Une ligne rouge puis du texte entr 5 ou 10 # puis une ligne rouge "Début de groupe"
# Changement, ajout, supression:
# Ligne jaune un problème

# Tout doit entre noté


# 13/12/2022 :
# Résolution du problème de fin (dans python.exe):
#       Le shell python.exe se refermais après l'entrer du mot de passe
#       Résolution:
#               c.mainloop()
# Notation des problèmes
# Commentaire sur le code ajouté
# 13/12/2022 17:12:
# I-Dream arrive a la 1 500 ligne
# 14/12/2022 :
# Ajout de la création des fichiers(Bureau, Font-D'écrant, Fichier)
# Le breakpoint de idmath a été résolu :
#       Le shell affichait une erreur de fichier pas trouver
#       Résolution:
#               ctrl + c sur le fichier et ctrl + v dans le champ de texte en changeant le nom du fichier
# Problème font d'écrant:
#11/01/2023:
#résolution problème ligne 1346 et 529 sur b64 decode et encode
#



















































































####################################################################################################################################
#        Début du code        #
################################################################################################################################

















































# Importation des modules



# Utilisation de >>>import [...]





import os               #importe le module os
import time             #importe le module time
import datetime         # importe le module datetime
import random           #importe le module random





# Utilisation de >>>from [...] import*
from turtle import *         #importe le module turtle
from tkinter import*   #importe le module tkinter e
from pyshutdown.myfunctions import * #importe les fonctions de myfonctions du module pyshutdown


















































##################################################################################################################################
##### Initialisation du Début #####
################################################################################################################################



































f = Tk() # créé une fenetre tkinter nomé f
c = Canvas(f, height=0.0000000000001, width=000000000.1) # créé un canvas












































def stop(evenement):
    # Définition de la fonction stop qui éteinds l'ordinateur si la touche préssé est "Prior" ou " Page Up"
    if test.keysym == 'Prior' :
        shutdown(0)
    if test.keysym == 'Next' :
        restart(0)




        
c.bind_all('<Key>', stop)













































#####################################################################################################################################
##### Début du font d'écrant d'accueil #####
############################################################################################################################





def main():
    peacecolors = ("red3",  "orange", "yellow",
                   "seagreen4", "orchid4",
                   "royalblue1", "dodgerblue4")

    reset()
    Screen()
    up()
    goto(-320,-195)
    width(70)










    
    for pcolor in peacecolors:
        speed(100)
        color(pcolor)
        down()
        forward(640)
        up()
        backward(640)
        left(90)
        forward(66)
        right(90)

    width(25)
    color("white")
    goto(0,-170)
    down()

    circle(170)
    left(90)
    forward(340)
    up()
    left(180)
    forward(170)
    right(45)
    down()
    forward(170)
    up()
    backward(170)
    left(90)
    down()
    forward(170)
    up()
    time.sleep(2)
    clear()

    goto(0,300) # vanish if hideturtle() is not available ;-)
    return "Done!"


    


main()















































################################################################################################################################
########## Définition des principal fonction d'I-DREAM##########
############################################################################################################################





def creeeruncompte():
    try:
        a = ''' Taper le nom d'utilisateur pour le nouveau compte'''
        screen = getscreen()
        nomutilisateurcreer = ''
        nomutilisateurcreer = screen.textinput('nouvel utilisateur', a)
        os.chdir('F:/#data-data')
        os.mkdir(nomutilisateurcreer)
        truc = 'F:/#data-data/' + nomutilisateurcreer
        print(truc)
        os.chdir(truc)
        os.mkdir('BUREAU')
        os.mkdir('FICHIER')
        os.mkdir('FONT-D\'écrant')
        print('hello')
        pasword = screen.textinput('pasword', 'pasword')
        os.chdir('F:/Programs/Paswords data')
        if nomutilisateurcreer!='NoneType':
            import base64
            f = open(nomutilisateurcreer, "w")
            sample_string_bytes = pasword.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            pasword2 = base64_bytes.decode("ascii")
            f.write(str(pasword2))
            f.close()
    except FileExistsError:
        import tkinter.messagebox
        tkinter.messagebox.showwarning('Erreur ACEE001','''ACEE001
ACEE001 : ACount Exist Error n°001''')




        
def stop():
    shutdown(0)




    
def execute(program):
    import os
    os.chdir(r'C:\Users\louis\OneDrive\Programs\PROGRAMS')
    file = open(program).read()
    exec(float(program))





def Openap():
    global program
    from tkinter import filedialog
    filename = filedialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
    filename2 = filename.split('/')
    filenamelen = len(filename2)
    program = filename2[filenamelen-1]
    import copy
    import os
    filename4 = copy.deepcopy(filename2)
    del filename4[filenamelen-1]
    filename5 = "/".join(filename4)
    os.chdir(filename5)
    print(os.getcwd)
    print(program)
    exec(complex(program)) # affiche une erreur ( écrire la date ou cela sera résolut





def Autorisation_admin():
    admin = Canvas(tk, height=500, width=500)
    btn = Button(admin, text = 'Click me !', bd = '5',command = admin.destroy)
    btn.pack(side = 'top')
















































##################################################################################################################################
##########Fin des définition des fonctions D' I-DREAM ##########
################################################################################################################################













































        
##########################################################################################################################
########## Définition de l'ouverture des application I-DREAM ##########
#############################################################################################################################




















































def idtxt2():
    import os
    import os
    os.chdir(r'C:\Users\louis\OneDrive\Programs\PROGRAMS')
    file = open('I-DREAM TEXT 3.2.py').read()
    exec(file)




    
def idmath():
    import os
    import os
    os.chdir(r'C:\Users\louis\OneDrive\Programs\PROGRAMS')
    file = open('I-DREAM MATH 1.py').read()
    exec(file) # Erreur "No file like that found"





def net():

    import os
    import os
    os.chdir(r'C:\Users\louis\OneDrive\Programs\PROGRAMS')
    file = open('I-DREAM INTERNET 3.0.py').read()
    exec(file)





















































##################################################################################################################################
########## Fin des deffinition des ouverture des apps I-DREAM ##########
################################################################################################################################










































    
##################################################################################################################################
##########Définition de l'horloge d'I-DREAM ##########
################################################################################################################################













































def clock():
    def jump(distanz, winkel=0):
        penup()
        right(winkel)
        forward(distanz)
        left(winkel)
        pendown()

    def hand(laenge, spitze):
        fd(laenge*1.15)
        rt(90)
        fd(spitze/2.0)
        lt(120)
        fd(spitze)
        lt(120)
        fd(spitze)
        lt(120)
        fd(spitze/2.0)

    def make_hand_shape(name, laenge, spitze):
        reset()
        jump(-laenge*0.15)
        begin_poly()
        hand(laenge, spitze)
        end_poly()
        hand_form = get_poly()
        register_shape(name, hand_form)

    def clockface(radius):
        reset()
        pensize(7)
        for i in range(60):
            jump(radius)
            if i % 5 == 0:
                fd(25)
                jump(-radius-25)
            else:
                dot(3)
                jump(-radius)
            rt(6)

    def setup():
        global second_hand, minute_hand, hour_hand, writer
        mode("logo")
        make_hand_shape("second_hand", 125, 25)
        make_hand_shape("minute_hand",  130, 25)
        make_hand_shape("hour_hand", 90, 25)
        clockface(160)
        second_hand = Turtle()
        second_hand.shape("second_hand")
        second_hand.color("gray20", "gray80")
        minute_hand = Turtle()
        minute_hand.shape("minute_hand")
        minute_hand.color("blue1", "red1")
        hour_hand = Turtle()
        hour_hand.shape("hour_hand")
        hour_hand.color("blue3", "red3")
        for hand in second_hand, minute_hand, hour_hand:
            hand.resizemode("user")
            hand.shapesize(1, 1, 3)
            hand.speed(0)
        ht()
        writer = Turtle()
        #writer.mode("logo")
        writer.ht()
        writer.pu()
        writer.bk(85)

    def wochentag(t):
        wochentag = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
        return wochentag[t.weekday()]

    def datum(z):
        monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
             "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
        j = z.year
        m = monat[z.month - 1]
        t = z.day
        return "%s %d %d" % (m, t, j)

    def tick():
        t = datetime.today()
        sekunde = t.second + t.microsecond*0.000001
        minute = t.minute + sekunde/60.0
        stunde = t.hour + minute/60.0
        try:
            tracer(False)  # Terminator can occur here
            writer.clear()
            writer.home()
            writer.forward(65)
            writer.write(wochentag(t),
                         align="center", font=("Courier", 14, "bold"))
            writer.back(150)
            writer.write(datum(t),
                         align="center", font=("Courier", 14, "bold"))
            writer.forward(85)
            tracer(True)
            second_hand.setheading(6*sekunde)  # or here
            minute_hand.setheading(6*minute)
            hour_hand.setheading(30*stunde)
            tracer(True)
            ontimer(tick, 100)
        except Terminator:
            pass  # turtledemo user pressed STOP

    def main():
        tracer(False)
        setup()
        tracer(True)
        tick()
        return "EVENTLOOP"

    if __name__ == "__main__":
        mode("logo")
        msg = main()
        print(msg)
        mainloop()

















































####################################################################################################################################
########## Fin de la définition de l'horloge d'I-Dream##########
########################################################################################################################################




        
    












































###############################################################################################################################################################################################
########## Startup I-Dream #########
#########################################################################################################################













































    
        
try:
    os.chdir('F:/')
    a = open('Admin.clé', mode='r')
    b = a.read()
    if b=='IDML':
        utilisateur = 'Admin'
        pasword = 'Admin 01'
except:
    ########## Récupération de l'utilisateur d' I-DREAM ##########
    a = ''
    screen = getscreen()
    utilisateur = screen.textinput('Utilisateur', a)





    ########## Récupération du mot de passe de l'utilisateur d' I-DREAM ##########
    b = 'Tape ton mot de passe'
    pasword = screen.textinput(utilisateur, b)










































########## Cherche dans les noms d'utilisateur pré-écrit un utilisateur puis en vérifi le mot de passe#########











import tkinter as tk
os.chdir(r'C:\Users\louis\OneDrive\Programs\Paswords data')
utilisateurtrouvé = os.listdir()
if utilisateur=='Marin' and pasword=='HARRYPOTERS31' :
    f = tk.Tk()# creer une fenetre tkinter
    idtxt = tk.Button(f, text='I-DREAM Text', command=idtxt2 )
    idmath = tk.Button(f, text='I-DREAM MATH', command=idmath )
    boutona = tk.Button(f, text='creer un compte', command=creeeruncompte )# creer un bouton tkinter
    idinternet = tk.Button(f, text='I-DREAM SAFE INTERNET', command=net )
    stop = tk.Button(f, text='ETEINDRE', command=stop )
    idtxt.pack()
    idmath.pack()
    idinternet.pack()
    boutona.pack()# affiche le bouton  tkinter
    stop.pack()




    




    
if utilisateur=='Havetquillivic.louis' and pasword=='1' :
    f = tk.Tk()# creer une fenetre tkinter
    c = Canvas(f, width=500, height=500)
    #os.chdir('D:/data-data/LOUIS/FONT-D\'écrant')
    #fonécrant = PhotoImage(file='écrant.gif')
    #c.create_image(0, 0, anchor=NW, image=fonécrant)
    #c.pack()
    idtxt = tk.Button(f, text='I-DREAM Text', command=idtxt2 )
    idmath = tk.Button(f, text='I-DREAM MATH', command=idmath )
    boutona = tk.Button(f, text='creer un compte', command=creeeruncompte )# creer un bouton tkinter
    idinternet = tk.Button(f, text='I-DREAM SAFE INTERNET', command=net )
    stop = tk.Button(f, text='ETEINDRE', command=stop )
    prog = tk.Button(f, text='Open an application', command=Openap)
    idtxt.pack()
    prog.pack()
    boutona.pack()# affiche le bouton  tkinter
    idmath.pack()
    idinternet.pack()
    stop.pack()





    




    
if utilisateur=='Admin' and pasword=='Admin 01' :
    f = tk.Tk()# creer une fenetre tkinter
    idtxt = tk.Button(f, text='I-DREAM Text', command=idtxt2 )
    idmath = tk.Button(f, text='I-DREAM MATH', command=idmath )
    boutona = tk.Button(f, text='creer un compte', command=creeeruncompte )# creer un bouton tkinter
    idinternet = tk.Button(f, text='I-DREAM SAFE INTERNET', command=net )
    stop = tk.Button(f, text='ETEINDRE', command=stop )
    prog = tk.Button(f, text='Open an application', command=Openap)
    idtxt.pack()
    prog.pack()
    boutona.pack()# affiche le bouton  tkinter
    idmath.pack()
    idinternet.pack()
    stop.pack()









    
########## Si aucunt utilisateur pré écrit est trouvé alors il herche dans l'I-Dream un nom d'utilisateur ###########










try:
    file = open(utilisateur, mode='r')
    global todecode
    import base64
    todecode = file.read()
    base64_string = todecode
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    password2 = sample_string_bytes.decode("ascii")
    if password2==pasword:
        from tkinter import*
        from os import*
        os.chdir(r'#data-data/' + utilisateur + '/BUREAU')
        a = listdir()
        print(a)
        f = Tk()
        c = Canvas(f)
        for i in range(0, len(a)):
            print('longeur :', len(a))
            print('est:', i)
            print('name:', a[i])
            b = Button(c , text=a[i])
            print(b)
            b.pack()
            print('fait')
            c.pack()











    else :
        print('password incorect :', password2)
except FileNotFoundError:
    print(FileNotFoundError)
    import tkinter.messagebox
    tkinter.messagebox.showwarning('Erreur OSRC001NAF ','''Erreur OSRC001NAF





OSRC001NAF = "On Start Root error 001 No Acount Found
OSRC001NAF signification :

Aucun compte trouvé correspondant a votre compte


Votre compte est surrement caché
''')













##################################################################################################################################
##########  Fin du startup d' I-DREAM ##########
###########################################################################################################################









































    
##################################################################################################################################
    
##################################################################################################################################
    
##################################################################################################################################
    
##################################################################################################################################
    
##################################################################################################################################










###   Fait tourner l' I-DREAM   ###

c.mainloop()
###   Fin de la ligne faisant tourner I-DREAM










#########################################################################################################################
    
##################################################################################################################################
    
##################################################################################################################################
    
##################################################################################################################################
    
##################################################################################################################################










































# Et voici I-DREAM taper "F5" pour la metre en marche dans IDLE #
