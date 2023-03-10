from time import sleep, time
from tkinter import * #importe le module turtle
from math import sqrt
h = 500
score = 0
l = 800
f = Tk()
f.title('Le débulator')
c = Canvas(f, height=h, width=l, bg='darkblue')
c.pack()
idsousmarin = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
id_sousmarin2 = c.create_oval(0, 0, 30, 30, outline='red')
R_SOUSMARIN = 15
X_MIL = l / 2
Y_MIL = h / 2
c.move(idsousmarin, X_MIL, Y_MIL)
c.move(id_sousmarin2, X_MIL, Y_MIL)
vit_sousmarin = 10
def move_sousmarin(eve):
    if eve.keysym == 'Up':
        c.move(idsousmarin, 0, -vit_sousmarin)
        c.move(id_sousmarin2, 0, -vit_sousmarin)
        
    if eve.keysym == 'Right':
        c.move(idsousmarin, vit_sousmarin, 0)
        c.move(id_sousmarin2, vit_sousmarin, 0)
    if eve.keysym == 'Left':
        c.move(idsousmarin, -vit_sousmarin, 0)
        c.move(id_sousmarin2, -vit_sousmarin, 0)
    if eve.keysym == 'Down':
        c.move(idsousmarin, 0, vit_sousmarin)
        c.move(id_sousmarin2, 0, vit_sousmarin)

c.bind_all('<Key>', move_sousmarin)
from random import randint
        
id_bulles = list()
r_bulles = list()
v_bulles = list()
r_bulles_min = 10
r_bulles_max = 30
ecart = 100
v_bulle_max = 10
def créer_bulles():
    x = l + ecart
    y = randint(0, h)
    r = randint(r_bulles_min, r_bulles_max)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white')
    id_bulles.append(id1)
    r_bulles.append(r)
    v_bulles.append(randint(1, v_bulle_max))
def deplacer_bulle():
    for i in range(len(id_bulles)):
        c.move(id_bulles[i], -v_bulles[i], 0)
bulle_hasard = 10  
def trouver_coords(num_id):
    pos = c.coords(num_id)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x, y
def suppr_bulle(i):
    del r_bulles[i]
    del v_bulles[i]
    c.delete(id_bulles[i])
    del id_bulles[i]
def effacer_bulles():
    for i in range(len(id_bulles)-1, -1, -1):
        x, y = trouver_coords(id_bulles[i])
        if x < -ecart:
            suppr_bulle(i)

def distance(id1, id2):
    x1, y1 = trouver_coords(id1)
    x2, y2 = trouver_coords(id2)
    return sqrt((x2 - x1)**2 + (y2-y1)**2)
def collision():
    points = 0
    for bulles in range(len(id_bulles)-1, -1, -1):
        if distance(id_sousmarin2, id_bulles[bulles]):
            points +=(r_bulles[bulles] + v_bulles[bulles])
            suppr_bulle(bulles)
    return points
c.create_text(100, 30, text='TEMPS RESTANT', fill='white')
c.create_text(200, 30, text='SCORE', fill='white')
texte_temps = c.create_text(100, 50, fill='white')
texte_score = c.create_text(200, 50, fill='white')
def afficher_score(score):
    c.itemconfig(texte_score, text=str(score))
def afficher_temps(temps_restant):
    c.itemconfig(texte_temps, text=str(temps_restant))
limite_temps = 30
score_bonus = 1000
bonus =0
fin = time() + limite_temps
while True:
    if randint(1, bulle_hasard) == 1:
        créer_bulles()
    deplacer_bulle()
    effacer_bulles()
    score+=collision()
    if(int(score / score_bonus)) > bonus:
        bonus += 1
        fin += limite_temps
    afficher_score(score)
    afficher_temps(int(fin - time()))
    print(score)
    f.update()
    sleep(0.01) 
