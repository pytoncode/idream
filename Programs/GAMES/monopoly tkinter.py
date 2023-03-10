import time
import random
carte_com = ["Frais de scolarité : payez 50€",
             "Votre assurance vie vous rapporte 100€",
             "commission d'expert immobilier. Recevez 25€",
             "Les impôts vous rembourse 20€",
             "Erreur de la banque en votre faveur. Recevez 200€",
             "Vous héritez de 100€",
             "Vous avez gagné le deuxième prix de beauté, recevez 10€",
             "C'est votre anniversaire, l'adversaire doit vous donner 20€",
             "Avancez jusqu'à la case départ (recevez 200€)",
             "Frais d'hospitalisation, payez 100€"]

carte_chance = ['Avancez au boulevard de la villette en passant par la case départ (et en recevant 200€)',
                "Vous avez été élu Président du Conseil d'Administration, versez 50€ à l'adversaire.",
                "Rendez-vous à l'avenue Henri-Martin.",
                "Amende pour excès de vitesse : payez 15€ au parc gratuit",
                "Votre immeuble et votre prêt vous rapporte !! Vous devez toucher 150€.",
                "La banque vous verse un dividende de 50€",
                "Avancez à la case départ (recevez 200€).",
                "Avancez vers la compagnie de distribution des eaux",
                "Allez à la Gare de Lyon en passant par la case départ (et en recevant 200€)",
                "Relancez le dé"]


global caseJ1
global caseJ2
caseJ1 = 0
caseJ2 = 0













from tkinter import*
f = Tk()
f.title('Dés')
global text
déé_text = Text(f, width=1, height=1)
class plateau:
    def timer():
        global parti_time
        parti_time = time.time()
    def dé(J):
        global caseJ1
        global caseJ2
        déé_text.delete(0.0, END)
        a = random.randint(1, 12)
        déé_text.insert(END, str(a))
        déé_text.pack()

        if J=='J1':
            caseJ1 +=a
        elif J=='J2':
            caseJ2 +=a
        else:
            print('Erreur ce joueur n\'est pas spécifié')
    def start():
        f1 = Tk()
        c = Canvas(f1, width = 1000, height = 1000)
        départ = c.create_rectangle(0, 0, 100, 100, outline='black', fill='white')
        départtxt = c.create_text(50, 20, fil='black', text='''Départ
recevez $200''')
        paix = c.create_rectangle(0, 200, 100, 100, outline='black', fill='red')
        paixtxt = c.create_text(50, 150, fil='white', text='''Rue de la paix
prix $400''')
        champs = c.create_rectangle(0, 300, 100, 200, outline='black', fill='red')
        champstxt = c.create_text(50, 250, fil='white', text='''Champs-Elysées
prix $300''')
        chance = c.create_rectangle(0, 400, 100, 300, outline='black', fill='black')
        chancetxt = c.create_text(50, 350, fil='white', text='''CHANCE''')
        
        f = c.create_rectangle(0, 500, 100, 400, outline='black', fill='green')
        ftxt = c.create_text(50, 450, fil='white', text='''Avenu Foch
prix $350''')
        
        p = c.create_rectangle(0, 600, 100, 500, outline='black', fill='green')
        ptxt = c.create_text(50, 550, fil='white', text='''Avenue Pointcarré
prix $350''')
        
        g = c.create_rectangle(0, 700, 100, 600, outline='black', fill='green')
        gtxt = c.create_text(50, 650, fil='white', text='''Avenue de Gaule
prix 350''')




        
        r = c.create_rectangle(100, 100, 200, 0, outline='black', fill='red')
        rtxt = c.create_text(150, 50, fil='white', text='''rue Renault lepetit
prix $400''')
        d = c.create_rectangle(200, 100, 300, 0, outline='black', fill='red')
        dtxt = c.create_text(250, 50, fil='white', text='''rue Martin lesapin
prix $400''')




























        
        c.pack()
plateau.start()
f.bind_all('<d>', plateau.dé)
for i in range(0, 100):
    plateau.start()

            
