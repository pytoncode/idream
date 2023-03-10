#!/usr/bin/python3
# -*- coding: utf-8 -*-

############################################
#                                    	   #
# Nom du programme : DIGICODE			   #
#                                    	   #
# Auteur : ......... Bruno CLÉVENOT  	   #
#                                    	   #
# Créé le : ........ 27/09/2021      	   #
#                                    	   #
# Programmé en : ... Python 3          	   #
#                                    	   #
# Version : ........ 1.0             	   #
#                                    	   #
# Licence: ......... GPL3            	   #
#                                    	   #
############################################

## Importation des bibliothèques
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.simpledialog import *
from random import *
import sys
## Fin d'importation des bibliothèques

## Fonctions et procédures
def quitter_fen():
    ## Quitter le jeu
    reponse = tkinter.messagebox.askyesno("Terminer le jeu","Voulez-vous réellement quitter ? \n Cliquer « Oui » pour finir")
    if reponse :
        ## On quitte le programme
        fen.quit()
		
def place_chiffre(chiffre):
	global lstChiffre, lstATrouver, lstProposee, lstVerifATrouver,lstVerifPoposee, partieEnCours,placeChoix,placeVerif, nombreEssai, perdu, gagne, vert, rouge, bouton
	lstProposee.append(chiffre) # On ajoute le chiffre
	nbreChiffre=len(lstProposee)
	if nbreChiffre==4:
		# Si 4 chiffres placés
		# On rend tous les boutons non accessibles
		for i in range(10):
			bouton[i].configure(state="disabled")
	else:
		# Si proposition non valider
		# On ne rend invalide que le bouton sélectionné
		bouton[chiffre].configure(state="disabled")
	# On affiche le choix
	affichage_choix(nbreChiffre)

def verif():
	global lstChiffre, lstATrouver, lstProposee, lstVerifATrouver,lstVerifPoposee, partieEnCours,placeChoix,placeVerif, nombreEssai, perdu, gagne, vert, rouge,nombreEssai,  perdu, gagne
	# On remet les valeurs à 0 pour rouge et vert
	rouge=0
	vert=0
	# On remet les vérification à false
	lstVerifATrouver[:]=[]
	lstVerifATrouver=[False,False,False,False]
	lstVerifPoposee[:]=[]
	lstVerifPoposee=[False,False,False,False]
	# On vérifie les chiffres à la bonne place
	for i in range(4):
		if lstProposee[i]==lstATrouver[i]:
			# On rajoute 1 au vert
			vert += 1
			# On marque comme vérifier
			lstVerifATrouver[i]=True
			lstVerifPoposee[i]=True
	# Si vert=4, partie gagnée
	if vert==4:
		# On met comme partie gagnée et finie
		gagne=True
		partieEnCours=False
		# On bloque les boutons 'Valider' et 'Annuler'
		btAnnuler.configure(state='disabled')
		btValider.configure(state='disabled')
		# On met la vérification
		placeVerif[10-nombreEssai]="V4R0"
		affichage_jeu()
		# On affiche le résultat
		affichage_resultat()
		# On prévient le joueur
		rep=messagebox.showinfo("Partie Gagnée !","FÉLICITATIONS !\n\nVous avez trouvé le code.")
	else :
		# On vérifie si chiffre mal placé
		for j in range(4): # Liste des propositions
			for k in range(4): # Liste des du nombre à trouver
				# Il faut que les 2 valeurs à comparer ne soient pas à la même place
				if j != k :
					# Il faut que les 2 valeurs à comparer ne soient pas vérifiées
					if lstVerifPoposee[j]== False and lstVerifATrouver[k]==False:
						if lstProposee[j]==lstATrouver[k]:
							rouge +=1
							lstVerifATrouver[k]=True
							lstVerifPoposee[j]=True	
		if vert==0 and rouge==1:
			placeVerif[10-nombreEssai]="V0R1"
		elif vert==0 and rouge==2:
			placeVerif[10-nombreEssai]="V0R2"
		elif vert==0 and rouge==3:
			placeVerif[10-nombreEssai]="V0R3"
		elif vert==0 and rouge==4:
			placeVerif[10-nombreEssai]="V0R4"
		elif vert==1 and rouge==0:
			placeVerif[10-nombreEssai]="V1R0"
		elif vert==1 and rouge==1:
			placeVerif[10-nombreEssai]="V1R1"
		elif vert==1 and rouge==2:
			placeVerif[10-nombreEssai]="V1R2"
		elif vert==1 and rouge==3:
			placeVerif[10-nombreEssai]="V1R3"
		elif vert==2 and rouge==0:
			placeVerif[10-nombreEssai]="V2R0"
		elif vert==2 and rouge==1:
			placeVerif[10-nombreEssai]="V2R1"
		elif vert==2 and rouge==2:
			placeVerif[10-nombreEssai]="V2R2"
		elif vert==3 and rouge==0:
			placeVerif[10-nombreEssai]="V3R0"
		# On affiche le tout
		affichage_jeu()
		# On diminue le nombre d'essais
		nombreEssai -=1
		if nombreEssai>0:
			# On remet les boutons de chiffres actifs
			for i in range(10):
				bouton[i].configure(state='normal')
			# On efface le canvas de choix et la liste de propositions
			lstProposee[:]=[]
			affichage_choix(-1)
		else:
			# Nombre d'essais épuisé
			# On met la partie perdue et terminée
			perdu=True
			partieEnCours=False
			# On bloque les boutons 'Valider' et 'Annuler'
			btAnnuler.configure(state='disabled')
			btValider.configure(state='disabled')
			# On affiche le résultat
			affichage_resultat()
			# On informe le joueur
			rep=messagebox.showinfo("Partie Terminée !","DÉSOLÉ !\n\nVous n'avez pas réuusi à trouver le code.")
	
def valider():
	global lstChiffre, lstATrouver, lstProposee, lstVerifATrouver,lstVerifPoposee, partieEnCours,placeChoix,placeVerif, nombreEssai, perdu, gagne, vert, rouge, nombreEssai
	# Vérifier qu'il y a bien 4 chiffres
	if len(lstProposee)<4:
		rep=messagebox.showinfo("Erreur de choix","La proposition doit contenir 4 chiffres")
		return
	else:
		# On met la proposition dans le jeu
		for a in range (4):
			placeChoix[10-nombreEssai][a]= lstProposee[a]
		# On vérifie la proposition
		verif()
		# On vide la liste de propositions
		lstProposee[:]=[]
	
def annuler():
	global lstChiffre, lstATrouver, lstProposee, lstVerifATrouver,lstVerifPoposee, partieEnCours,placeChoix,placeVerif, nombreEssai, perdu, gagne, vert, rouge, bouton
	## Vider le canvas de choix (canvChoix)
	lstProposee[:]=[]# On vide la liste des propositions
	canvChoix.delete(ALL) # On vide le canvas de choix (canvChoix)
	## On remet tous les boutons de chiffres en enabled
	for i in range(10):
		bouton[i].configure(state='normal')
	
def nouvellePartie():
	global lstChiffre, lstATrouver, lstProposee, lstVerifATrouver,lstVerifPoposee, partieEnCours,placeChoix,placeVerif, nombreEssai, perdu, gagne, vert, rouge
	# On vérifie si une partie est en cours
	if partieEnCours==True:
		rep=messagebox.askyesno('PARTIE EN COURS',"Une partie est en cours.\n\nVoulez-vous l'abondonner ?")
		# Si oui
		if rep:
			# On indique qu'il n'y a plus de partie en cours
			partieEnCours=False
		# Si non, on passe les modif
		else:
			return
	# On indique q'une nouvelle partie est en cours
	partieEnCours=True
	# Celle-ci n'est ni gagnée ni perdue
	gagne=False
	perdu=False
	# On vide la liste des propositions
	lstProposee[:]=[]
	# On pace les vérification à false
	lstVerifATrouver[:]=[]
	lstVerifATrouver=[False,False,False,False]
	lstVerifPoposee[:]=[]
	lstVerifPoposee=[False,False,False,False]
	# On vide les cartes de place
	placeChoix[:]=[]
	for y in range(10):
		placeChoix.append([10,10,10,10])
	placeVerif[:]=[]
	for i in range(10):
		placeVerif.append("VR")
	# on remet le nombre d'essais à 10
	nombreEssai=10
	# On met le nombre de chiffres trouvés à 0
	rouge=0
	vert=0
	# On efface la solution si existante
	canvSolution.delete(ALL)
	# On affiche le jeu
	affichage_jeu()
	# On efface le choix en cours et on rend les chiffre accessibles
	annuler()
	# On procède au tirage du nombre à trouver
	tirage()
	# On rens accessibles les boutons 'Valider' et 'Annuler'
	btAnnuler.configure(state='normal')
	btValider.configure(state='normal')

def tirage():
	global lstATrouver
	# On vide la liste
	lstATrouver[:]=[]
	# On fait le tirage
	lstATrouver=sample(lstChiffre,4)
	
def affichage_jeu():
	global lstChiffre, lstATrouver, lstProposee, lstVerifATrouver,lstVerifPoposee, partieEnCours,placeChoix,placeVerif, nombreEssai, perdu, gagne, vert, rouge
	#On vide le jeu et les vérifications
	canvJeu.delete(ALL)
	canvVerif.delete(ALL)
    # On remplit
	for y in range(10):
		for x in range(4):
			if placeChoix[y][x]==0:
				canvJeu.create_image(x*50,y*50,image=img0,anchor='nw')
			elif placeChoix[y][x]==1:
				canvJeu.create_image(x*50,y*50,image=img1,anchor='nw')
			elif placeChoix[y][x]==2:
				canvJeu.create_image(x*50,y*50,image=img2,anchor='nw')
			elif placeChoix[y][x]==3:
				canvJeu.create_image(x*50,y*50,image=img3,anchor='nw')
			elif placeChoix[y][x]==4:
				canvJeu.create_image(x*50,y*50,image=img4,anchor='nw')
			elif placeChoix[y][x]==5:
				canvJeu.create_image(x*50,y*50,image=img5,anchor='nw')
			elif placeChoix[y][x]==6:
				canvJeu.create_image(x*50,y*50,image=img6,anchor='nw')
			elif placeChoix[y][x]==7:
				canvJeu.create_image(x*50,y*50,image=img7,anchor='nw')
			elif placeChoix[y][x]==8:
				canvJeu.create_image(x*50,y*50,image=img8,anchor='nw')
			elif placeChoix[y][x]==9:
				canvJeu.create_image(x*50,y*50,image=img9,anchor='nw')
	for y in range(10):
		if placeVerif[y]=="V0R1":
			canvVerif.create_image(0,y*50,image=imgV0R1,anchor='nw')
		elif placeVerif[y]=="V0R2":
			canvVerif.create_image(0,y*50,image=imgV0R2,anchor='nw')
		elif placeVerif[y]=="V0R3":
			canvVerif.create_image(0,y*50,image=imgV0R3,anchor='nw')
		elif placeVerif[y]=="V0R4":
			canvVerif.create_image(0,y*50,image=imgV0R4,anchor='nw')
		elif placeVerif[y]=="V1R0":
			canvVerif.create_image(0,y*50,image=imgV1R0,anchor='nw')
		elif placeVerif[y]=="V1R1":
			canvVerif.create_image(0,y*50,image=imgV1R1,anchor='nw')
		elif placeVerif[y]=="V1R2":
			canvVerif.create_image(0,y*50,image=imgV1R2,anchor='nw')
		elif placeVerif[y]=="V1R3":
			canvVerif.create_image(0,y*50,image=imgV1R3,anchor='nw')
		elif placeVerif[y]=="V2R0":
			canvVerif.create_image(0,y*50,image=imgV2R0,anchor='nw')
		elif placeVerif[y]=="V2R1":
			canvVerif.create_image(0,y*50,image=imgV2R1,anchor='nw')
		elif placeVerif[y]=="V2R2":
			canvVerif.create_image(0,y*50,image=imgV2R2,anchor='nw')
		elif placeVerif[y]=="V3R0":
			canvVerif.create_image(0,y*50,image=imgV3R0,anchor='nw')
		elif placeVerif[y]=="V4R0":
			canvVerif.create_image(0,y*50,image=imgV4R0,anchor='nw')
			
def affichage_choix(nbreChiffre):
	global lstChiffre, lstATrouver, lstProposee, lstVerifATrouver,lstVerifPoposee, partieEnCours,placeChoix,placeVerif, nombreEssai, perdu, gagne, vert, rouge
	if nbreChiffre>=0:
		for i in range(nbreChiffre):
			if lstProposee[i]==0:
				canvChoix.create_image(i*50,0,image=img0,anchor='nw')
			elif lstProposee[i]==1:
				canvChoix.create_image(i*50,0,image=img1,anchor='nw')
			elif lstProposee[i]==2:
				canvChoix.create_image(i*50,0,image=img2,anchor='nw')
			elif lstProposee[i]==3:
				canvChoix.create_image(i*50,0,image=img3,anchor='nw')
			elif lstProposee[i]==4:
				canvChoix.create_image(i*50,0,image=img4,anchor='nw')
			elif lstProposee[i]==5:
				canvChoix.create_image(i*50,0,image=img5,anchor='nw')
			elif lstProposee[i]==6:
				canvChoix.create_image(i*50,0,image=img6,anchor='nw')
			elif lstProposee[i]==7:
				canvChoix.create_image(i*50,0,image=img7,anchor='nw')
			elif lstProposee[i]==8:
				canvChoix.create_image(i*50,0,image=img8,anchor='nw')
			elif lstProposee[i]==9:
				canvChoix.create_image(i*50,0,image=img9,anchor='nw')
	else:
		canvChoix.delete(ALL)
		
def affichage_resultat():
	global lstChiffre, lstATrouver, lstProposee, lstVerifATrouver,lstVerifPoposee, partieEnCours,placeChoix,placeVerif, nombreEssai, perdu, gagne, vert, rouge
	for b in range (4) :
		if lstATrouver[b]==0:
			canvSolution.create_image(b*50,0,image=img0,anchor='nw')
		elif lstATrouver[b]==1:
			canvSolution.create_image(b*50,0,image=img1,anchor='nw')
		elif lstATrouver[b]==2:
			canvSolution.create_image(b*50,0,image=img2,anchor='nw')
		elif lstATrouver[b]==3:
			canvSolution.create_image(b*50,0,image=img3,anchor='nw')
		elif lstATrouver[b]==4:
			canvSolution.create_image(b*50,0,image=img4,anchor='nw')
		elif lstATrouver[b]==5:
			canvSolution.create_image(b*50,0,image=img5,anchor='nw')
		elif lstATrouver[b]==6:
			canvSolution.create_image(b*50,0,image=img6,anchor='nw')
		elif lstATrouver[b]==7:
			canvSolution.create_image(b*50,0,image=img7,anchor='nw')
		elif lstATrouver[b]==8:
			canvSolution.create_image(b*50,0,image=img8,anchor='nw')
		elif lstATrouver[b]==9:
			canvSolution.create_image(b*50,0,image=img9,anchor='nw')
				
def aide():
	global ws, hs
	waide=564
	haide=585
	aaide=(ws-waide)//2
	baide=(hs-haide)//2
	fenaide=Toplevel(fen)
	fenaide.geometry("%dx%d+%d+%d" % (waide, haide, aaide, baide))	
	fenaide.resizable(height=False,width=False)
	fenaide.focus()
	fenaide.title("LE DIGICODE - AIDE")
	fenaide.configure(bg='#9f7c33')
	lbaide2=ttk.Label(fenaide,style='BW.TLabel',width=60)
	txtlbaide='\nLE DIGICODE.\n\n'
	txtlbaide=txtlbaide+"BUT DU JEU :\n\n"
	txtlbaide=txtlbaide+"Découvrir le code à 4 chiffres.\n\n"
	txtlbaide=txtlbaide+'CONTRAINTES :\n\n'
	txtlbaide=txtlbaide+"Les 4 chiffres du codes sont tous différents les uns des autres.\n\n"
	txtlbaide=txtlbaide+"Vous avez 10 essais.\n\n"
	txtlbaide=txtlbaide+"COMMENT JOUER : \n\n"
	txtlbaide=txtlbaide+"Pour proposer un code, taper sur les chiffres blancs.\n"
	txtlbaide=txtlbaide+"Celui-ci apparait dans le cadre noir au dessus des chiffres.\n"
	txtlbaide=txtlbaide+"Si le code vous convient, appuyer sur Valider.\n"
	txtlbaide=txtlbaide+"Sinon, appuyer sur Annuler et recommencer.\n\n"
	txtlbaide=txtlbaide+"Une fois valider, votre code apparaitra dans le grand cadre noir.\n"
	txtlbaide=txtlbaide+"à gauche suivi d'indice(s).\n\n"
	txtlbaide=txtlbaide+"Une boule verte indique un chiffre bien placé.\n"
	txtlbaide=txtlbaide+"Une boule rouge indique un chiffre mal placé.\n"
	lbaide2.configure(text=txtlbaide)
	lbaide2.grid(row=0,column=0,padx=10,pady=10)
	btaidequit=ttk.Button(fenaide,style='BW.TButton',text='Quitter',command=fenaide.destroy)
	btaidequit.grid(row=2,column=0,pady=10)
	fenaide.grab_set() # Rend le toplevel maître
	
def AP():
	global ws, hs
	wap=564
	hap=300
	aap=(ws-wap)//2
	bap=(hs-hap)//2
	fenap=Toplevel(fen)
	fenap.geometry("%dx%d+%d+%d" % (wap, hap, aap, bap))
	fenap.resizable(height=False,width=False)
	fenap.focus()
	fenap.title("LE DIGICODE - À propos de ...")
	fenap.configure(bg='#9f7c33')
	lbap=ttk.Label(fenap,style='BW.TLabel',width=60)
	txtlbap='\nLE DIGICODE\n\n'
	txtlbap=txtlbap+'© copyleft Bruno CLÉVENOT Octobre 2021\n\n'
	txtlbap=txtlbap+'Jeu programmé en Python 3 par Bruno CLÉVENOT.\n\n'
	txtlbap=txtlbap+'Graphismes par Bruno CLÉVENOT sous licence GPL Version 3. \n\n'
	txtlbap=txtlbap+'Code distribués sous licence GPL Version 3.\n\n'
	lbap.configure(text=txtlbap)
	lbap.grid(row=0,column=0,padx=10,pady=10)
	btapquit=ttk.Button(fenap,style='BW.TButton',text='Quitter',command=fenap.destroy)
	btapquit.grid(row=1,column=0,pady=10)
	fenap.grab_set() # Rend le toplevel maître
## Fin fonctions et procédures

# Création fenêtre principale
fen=Tk()
## Fin création fenêtre principale

# Images et variables
fonte=('Arial',12,'bold')
fonte2=('Arial',20,'bold')
img0=PhotoImage(file='0.png')
img1=PhotoImage(file='1.png')
img2=PhotoImage(file='2.png')
img3=PhotoImage(file='3.png')
img4=PhotoImage(file='4.png')
img5=PhotoImage(file='5.png')
img6=PhotoImage(file='6.png')
img7=PhotoImage(file='7.png')
img8=PhotoImage(file='8.png')
img9=PhotoImage(file='9.png')
imgV0R1=PhotoImage(file='V0R1.png')
imgV0R2=PhotoImage(file='V0R2.png')
imgV0R3=PhotoImage(file='V0R3.png')
imgV0R4=PhotoImage(file='V0R4.png')
imgV1R0=PhotoImage(file='V1R0.png')
imgV1R1=PhotoImage(file='V1R1.png')
imgV1R2=PhotoImage(file='V1R2.png')
imgV1R3=PhotoImage(file='V1R3.png')
imgV2R0=PhotoImage(file='V2R0.png')
imgV2R1=PhotoImage(file='V2R1.png')
imgV2R2=PhotoImage(file='V2R2.png')
imgV3R0=PhotoImage(file='V3R0.png')
imgV4R0=PhotoImage(file='V4R0.png')
imgRouge=PhotoImage(file='ROUGE2.png')
imgVert=PhotoImage(file='VERT2.png')
lstChiffre=[i for i in range(10)]#Liste de tous les chiffres
lstATrouver=[]
lstVerifATrouver=[False,False,False,False]
lstProposee=[]
lstVerifPoposee=[False,False,False,False]
perdu=False
gagne=False
partieEnCours=True
placeChoix=[] #Carte du jeu
for y in range(10):
	placeChoix.append([10,10,10,10])
placeVerif=[] # Carte des vérification 
for i in range(10):
	placeVerif.append("VR")
nombreEssai=10
rouge=0 # Nombre de chiffres mal placés
vert=0 # Nombre de chiffre bien placés
# Fin images et variables

## Styles
s=ttk.Style()
s.theme_use()
s.map("BW.TButton",background=[('pressed', '!disabled', 'black'), ('active', 'cyan')])
s.configure("BW.TButton",font=fonte,foreground='black',borderwidht=4,background='lime')
s.configure("BW.TLabel",font=fonte,background='#9f7c33',foreground='white',justify='left',highlightthickness=0,anchor='left')
## Fin styles

## Intérieur fenêtre
fen.title('LE DIGICODE')
fen.resizable(height=False,width=False)
fen.configure(bg='#9f7c33')
if sys.platform.startswith('linux') :
	fen.iconphoto(True, PhotoImage(file='chouette.xbm'))
elif sys.platform.startswith('win32') :
	fen.iconphoto(True, PhotoImage(file='chouette.png'))
frmJeu=Frame(fen,bg='#9f7c33')
frmJeu.grid(row=0,column=0,padx=5,pady=5,rowspan=3)
canvSolution=Canvas(frmJeu,width=200, height=50,bg='black',bd=0,highlightthickness=0)
canvSolution.grid(row=0,column=0)
canvJeu=Canvas(frmJeu,width=200, height=500,bg='black',bd=0,highlightthickness=0)
canvJeu.grid(row=1,column=0,pady=5)
canvVerif=Canvas(frmJeu,width=50, height=500,bg='black',bd=0,highlightthickness=0)
canvVerif.grid(row=1,column=1,pady=5)
frmChoix=Frame(fen,bg='#9f7c33',relief=RIDGE,bd=4)
frmChoix.grid(row=0,column=1,padx=5,pady=5)
canvChoix=Canvas(frmChoix,width=200, height=50,bg='black',bd=0,highlightthickness=0)
canvChoix.grid(row=0,column=0,padx=5,pady=5,columnspan=5)
bouton=[0]*10
for i in range(10):
	bouton[i] = Button(frmChoix,relief=FLAT,bd=0,font=fonte2,width=2,background='#9f7c33',foreground='white',disabledforeground='gray',text=str(i),command=lambda x=i:place_chiffre(x))
	bouton[i].grid(row=1+i//5, column=i%5,padx=5)
btValider=ttk.Button(frmChoix,style="BW.TButton",text="Valider",width=9, command=valider)
btValider.grid(row=3,column=1,pady=5)
btAnnuler=ttk.Button(frmChoix,style="BW.TButton",text="Annuler",width=9, command=annuler)
btAnnuler.grid(row=3,column=3,pady=5)
frmInfo=Frame(fen,bg='#9f7c33',relief=RIDGE,bd=4)
frmInfo.grid(row=1,column=1,padx=5,pady=5)
lbinfo1=ttk.Label(frmInfo,style='BW.TLabel',image=imgVert, text="1 chiffre bien placé", compound='left', width=24)
lbinfo1.grid(row=0,column=0,padx=10,pady=5)
lbinfo2=ttk.Label(frmInfo,style='BW.TLabel', image=imgRouge, text="1 chiffre mal placé ", compound='left', width=24)
lbinfo2	.grid(row=1,column=0,padx=10,pady=5)
frmCommandes=Frame(fen,bg='#9f7c33',relief=RIDGE,bd=4)
frmCommandes.grid(row=2,column=1,padx=5,pady=5)
btNouvellepartie=ttk.Button(frmCommandes,style="BW.TButton",text="Nouvelle partie",width=16, command=nouvellePartie)
btNouvellepartie.grid(row=0,column=0,padx=5,pady=5)
btQuitter=ttk.Button(frmCommandes,style="BW.TButton",text="Quitter",width=16, command=quitter_fen)
btQuitter.grid(row=0,column=1,padx=5,pady=5)
btAide=ttk.Button(frmCommandes,style="BW.TButton",text="Aide",width=16, command=aide)
btAide.grid(row=1,column=0,padx=5,pady=5)
btAP=ttk.Button(frmCommandes,style="BW.TButton",text="À propos de ...",width=16, command=AP)
btAP.grid(row=1,column=1,padx=5,pady=5)
tirage()
## Fin intérieur fenêtre

## Placement de la fenêtre
fen.update()
w=610
h=570
ws = fen.winfo_screenwidth()
hs = fen.winfo_screenheight()
a=(ws-w)//2
b=(hs-h)//2
fen.geometry("%dx%d+%d+%d" % (w, h, a, b))
## Fin placement de la fenêtre

## Fonction de fermeture de la fenêtre
fen.protocol("WM_DELETE_WINDOW",quitter_fen)
## Fin fonction fermeture de fenêtre

fen.mainloop()