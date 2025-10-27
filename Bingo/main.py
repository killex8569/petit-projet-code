import random

taille_grille = 15

bingo_1_j = []
bingo_2_j = []

bingo_1_o = []
bingo_2_o = []

nb_tirer = []

# Tirage de la manière suivante : 
# 15 nombre entre 1 et 89

def create_grille(list_tableau):
    i = 0
    while i <= taille_grille:
        nb = random.randrange(90)
        list_tableau.append(nb)
        i = i + 1


def main_menu():
    print("Bienvenue dans le Bingo en python. Séléctionner votre mode de jeu : ")
    print("1 - 1 seul grille\n2 - 2 Grilles\n3 - JcJ\n4 - Ordi1 vs Ordi2")
    rep = int(input("Veuillez choisir votre mode de jeu : "))
    if rep == 1:
        create_grille(bingo_1_j)
        create_grille(bingo_1_o)
        print("Votre ligne de bingo : ", bingo_1_j)
        print("Ligne de bingo de l'ordi : ", bingo_1_o)
    elif rep == 2:
        create_grille(bingo_1_j)
        create_grille(bingo_2_j)

        create_grille(bingo_1_o)
        create_grille(bingo_2_o)
        print("Votre grille 1 : ", bingo_1_j, "\nGrille 2 : ", bingo_2_j)
        print("Grille de votre adversaire : ", bingo_1_o, "\nGrille 2 : ", bingo_2_o)

main_menu()