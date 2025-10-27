import random
import time

taille_grille = 15

bingo_1_j = []
bingo_1_o = []


name_j1 = ""
name_j2 = ""

rep_2 = 0

# Choses à faire : 
# - Mettre les variables global dans les fonctions (redéfinir)
# - Modifier le code pour cela


# Tirage de la manière suivante : 
# 15 nombre entre 0 et 89

def create_grille(list_tableau):
    i = 0
    while i <= taille_grille:
        nb = random.randrange(90)
        if nb not in list_tableau:
            list_tableau.append(nb)
            i = i + 1

def tirage(list_tableau, list_tableau_ordi):
    global rep_2, name_j2, name_j1
    print("Voici la valeur de rep", rep_2, "nom 1 et 2", name_j1, name_j2)
    while len(bingo_1_j) or len(bingo_1_o) > 0:
        nb_tirage = random.randrange(90)
        print("Le nombre choisi est : ", nb_tirage)
        if nb_tirage in list_tableau and nb_tirage in list_tableau_ordi:
            verif_victoire()
            list_tableau.remove(nb_tirage)
            list_tableau_ordi.remove(nb_tirage)
            time.sleep(1)
            if rep_2 == 1:
                time.sleep(1)
                print("Vous aviez tout deux un nombre identique dans votre bingo ! ", nb_tirage)
                print(bingo_1_j, "reste : ", len(list_tableau))
                print("L'ord avait un nb dans sa liste ! rest : ", len(list_tableau_ordi))
                time.sleep(1)
            elif rep_2 == 2:
                time.sleep(1)
                print("Vous aviez tout deux un nombre identique dans votre bingo ! ", nb_tirage)
                print(name_j1, " : ", bingo_1_j, "reste donc : ", len(list_tableau))
                print(name_j2, " avait un nb dans sa liste ! rest : ", len(list_tableau_ordi))
                time.sleep(1)
        elif nb_tirage in list_tableau:
            verif_victoire()
            list_tableau.remove(nb_tirage)
            time.sleep(1)
            if rep_2 == 1:
                time.sleep(1)
                print(bingo_1_j, "reste : ", len(list_tableau))
                time.sleep(1)
            elif rep_2 == 2:
                time.sleep(1)
                print(name_j1, "reste : ", len(list_tableau))
        elif nb_tirage in list_tableau_ordi:
            verif_victoire()
            list_tableau_ordi.remove(nb_tirage)
            time.sleep(1)
            if rep_2 == 1:
                time.sleep(1)
                print("L'ord avait un nb dans sa liste ! rest : ", len(list_tableau_ordi))
                time.sleep(1)
            elif rep_2 == 2:
                time.sleep(1)
                print(name_j2, " avait un nb dans sa liste ! rest : ", len(list_tableau_ordi))
                time.sleep(1)


def verif_victoire():
    global rep_2, name_j2, name_j1
    if len(bingo_1_j) == 0:
        if rep_2 == 1:
            print("Le joueur à Gagner !")
            time.sleep(4)
            main_menu()
        elif rep_2 == 2:
            print("Le gagnant est : ", name_j1)
            time.sleep(4)
            main_menu()
    elif len(bingo_1_o) == 0:
        if rep_2 == 1:
            print("L'ordi à gagner ! ")
            time.sleep(4)
            main_menu()
        elif rep_2 == 2:
            print("Le gagnant est : ", name_j2)
            time.sleep(4)
            main_menu()


def main_menu():
    global rep_2, name_j2, name_j1
    print("Bienvenue dans le Bingo en python.\nSéléctionner votre mode de jeu : ")
    print("1 - 1 seul grille\n2 - JcJ\n3 - Ordi1 vs Ordi2\n4 - Quitter")
    rep = int(input("Veuillez choisir votre mode de jeu : "))
    if rep == 1:
        rep_2 = 1
        create_grille(bingo_1_j)
        create_grille(bingo_1_o)
        print("Votre ligne de bingo : ", bingo_1_j)
        print("Ligne de bingo de l'ordi : ", bingo_1_o)
        tirage(bingo_1_j, bingo_1_o)
    elif rep == 2:
        rep_2 = 2
        name_j1 = str(input("Veuillez mettre le nom du joueur 1 : "))
        name_j2 = str(input("Veuillez mettre le nom du joueur 2 : "))
        create_grille(bingo_1_j)
        create_grille(bingo_1_o)
        print("Votre grille 1 : ", bingo_1_j)
        print("Grille de votre adversaire : ", bingo_1_o)
        time.sleep(5)
        tirage(bingo_1_j, bingo_1_o)
    elif rep == 4:
        quit()
    else:
        print("Votre réponse n'est pas valide")
        main_menu()

main_menu()