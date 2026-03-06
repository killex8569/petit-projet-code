# Le pc choisit un nombre aléatoire, puis le joueur doit proposer un nombre de taille équivalent (si code = 4 chiffres --> 1234, Alors le joueur = 4 --> 2345)
# Si un ou plusieurs nombre est présent dans la liste, le bot indique le nombre de chiffre présent dans la suite, si un ou plusieurs chiffre sont bien placer, alors il lui indique aussi
#  

import random
import time

def generate_code(lenght: int) -> str:
    code = ""
    for _ in range(lenght):
        nombre = str(random.randint(0, 9))
        code += nombre
    return code


def correct_placement(nb):
    pass

def code_breaker(nb):
    secret_code = generate_code(nb)
    player_rep = []
    for i in range(1, nb, 1):
        random.randint(1, len(nb))

    while True:
        try:
            player_rep = str(input("Inséré votre nombre : "))
        except ValueError:
            print("Entrée invalide.")
            continue
        if len(player_rep) > nb:
            print("Votre nombre contient trop de chiffre, nb de chiffres : ", len(nb))
            continue
        elif len(player_rep) < nb:
            print("Votre nombre contient trop de chiffre, nb de chiffres : ", len(nb))
            continue


def main():
    print("Bienvenue dans le jeux du code breaker\nQu'elle mode de jeux ovulez vous faire : ")
    while True:
        try:
            user_rep = int(input("1 - \n2 - \n3 - "))
        except ValueError:
            print("Entrer interdite")
            continue
        if user_rep == 1:
            nb = int(input("Combiens de lettre voulez vous : "))
            generate_code(nb)
            
        elif user_rep == 2:
            pass
        else:
            print("Veuillez re-essayer")
            continue

main()

