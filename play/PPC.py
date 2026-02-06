# Jeu du pierre papier ciseau en python
import random

def main_pfc():
    print("Bienvenue dans le main")
    possibiliter = ["P", "F", "C"]
    nb_point = 0

    while nb_point == 0:
        rep_bot = random.choice(possibiliter)
        rep_user = str(input("Veuillez choisir entre P F C : ")).upper()
        if rep_user == "P" and rep_bot == "C":
            print("Vous avez gagner")
            nb_point += 1
        elif rep_user == "F" and rep_bot == "P":
            print("Vous avez gagenr")
            nb_point += 1
        elif rep_user == "C" and rep_bot == "F":
            print("vous avez gagner")
            nb_point += 1
        elif rep_bot == rep_user:
            print("égaliter")

        else:
            print("Vous avez perdu")

