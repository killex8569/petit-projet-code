import random
import time

taille_grille = 15

bingo_1_j = []
bingo_2_j = []

bingo_1_o = []
bingo_2_o = []

nb_tirer = []

# Tirage de la manière suivante : 
# 15 nombre entre 0 et 89

def create_grille(list_tableau):
    i = 0
    while i <= taille_grille:
        nb = random.randrange(90)
        if nb not in list_tableau:
            list_tableau.append(nb)
            i = i + 1

def tirage_1(list_tableau, list_tableau_ordi):
    print("tirage")
    while len(bingo_1_j) or len(bingo_2_j) or len(bingo_1_o) or len(bingo_2_o) > 0:
        nb_tirage = random.randrange(90)
        print("Le nombre choisi est : ", nb_tirage)
        if nb_tirage in list_tableau:
            verif_victoire_1()
            list_tableau.remove(nb_tirage)
            time.sleep(1)
            print(bingo_1_j, "reste : ", len(list_tableau))
            time.sleep(1)
        elif nb_tirage in list_tableau_ordi:
            verif_victoire_1()
            list_tableau_ordi.remove(nb_tirage)
            time.sleep(1)
            print("L'ord avait un nb dans sa liste ! rest : ", len(list_tableau_ordi))
            time.sleep(1)


def verif_victoire_1():
    if len(bingo_1_j) == 0:
        print("Le joueur à Gagner !")
        time.sleep(4)
        main_menu()
    elif len(bingo_1_o) == 0:
        print("L'ordi à gagner ! ")
        time.sleep(4)
        main_menu()


def verif_victoire_2():
    if len(bingo_1_j) and len(bingo_2_j)== 0:
        print("Le joueur à Gagner !")
    elif len(bingo_1_o) and len(bingo_2_o)== 0:
        print("L'ordi à gagner ! ")



def main_menu():
    print("Bienvenue dans le Bingo en python.\nSéléctionner votre mode de jeu : ")
    print("1 - 1 seul grille\n2 - 2 Grilles\n3 - JcJ\n4 - Ordi1 vs Ordi2")
    rep = int(input("Veuillez choisir votre mode de jeu : "))
    if rep == 1:
        create_grille(bingo_1_j)
        create_grille(bingo_1_o)
        print("Votre ligne de bingo : ", bingo_1_j)
        print("Ligne de bingo de l'ordi : ", bingo_1_o)
        tirage_1(bingo_1_j, bingo_1_o)
    elif rep == 2:
        create_grille(bingo_1_j)
        create_grille(bingo_2_j)

        create_grille(bingo_1_o)
        create_grille(bingo_2_o)
        print("Votre grille 1 : ", bingo_1_j, "\nGrille 2 : ", bingo_2_j)
        print("Grille de votre adversaire : ", bingo_1_o, "\nGrille 2 : ", bingo_2_o)
    else:
        print("Votre réponse n'est pas valide")
        main_menu()

main_menu()