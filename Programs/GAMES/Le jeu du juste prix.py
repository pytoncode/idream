from random import randint
import sys

banner = """   
      _              _          ____         _       
     | | _   _  ___ | |_  ___  |  _ \  _ __ (_)__  __
  _  | || | | |/ __|| __|/ _ \ | |_) || '__|| |\ \/ /
 | |_| || |_| |\__ \| |_|  __/ |  __/ | |   | | >  < 
  \___/  \__,_||___/ \__|\___| |_|    |_|   |_|/_/\_\ 
                                            by Div_YT"""

print(banner)

def play():
    mode = input("Select Your Mode to Play : \n - (H)ard (1000 numbers in 10) \n - (N)ormal (500 in 10) \n - (E)asy (100 in 10) \n - (Q)uit --->")
    dico = {"H": 1000, "N": 500, "E": 100}
    if mode in ["H", "N", "E", "h", "n", "e", "Q", "q"]:
        if mode == "Q" or mode == "q":
            sys.exit("Le Jeu Est Quitté. Fait par Div_YT")
        max = dico.get(mode)
        number = generate(max)
        print(f"Le Nombre est compris entre 0 et {max}")
        tours = 0
        while tours != 10:
            choice = int(input("What is Your Number(only numbers) --> "))
            if choice > number:
                print("Le nombre est Plus Petit")
            elif choice < number:
                print("Le Nombre est plus Grand")
            elif choice == number:
                bravo = f"Bravo tu as gagné le jeu en {tours}, Si tu veux rejouer, relance le programme ."
                input()
                print(bravo)
                return 0
            tours = tours + 1
    else:
        print("*** Incorrect Value ***")
        play()

def generate(max):
    return randint(0, max)

if __name__ == "__main__":
    play()
