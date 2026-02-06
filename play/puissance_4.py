# Règle du puissance 4 : Chaque joueur à son tour peut placer une X ou un O, le permier qui fait une suite (diagonal, horizontal ou vertical) à gagner la partie 
# --> 6 de hauteur 7 de largeur

import random

ROWS = 6
COLS = 7
grille = [["*"] * COLS for _ in range(ROWS)]

suite = 4



def affichage_grille():
    # Affichage de la grille
    for ligne in grille:
        print(" ".join(map(str, ligne)))
    for i in range(1, COLS + 1): # Boucle de 1 à COLS +1 inclu
        print(i, end=" ") # Tout sur la même ligne
    print("") # saut de ligne

def tour_joueur():
    print("tour du joueur (Les X)")
    colonne = int(input("Quelle colonne voulez jouer ? : "))

    # Sécurité
    if colonne < 0 or colonne >= len(grille[0]):
        print("Colonne invalide")
        return
    

    for i in range(len(grille) - 1, -1, -1):
        if grille[i][colonne] == "*":
            grille[i][colonne] = "X"
            return
        
def tour_bot():
    print("tour du BOT (Les O)")
    colonne = random.randint(1, COLS)

    # Sécurité
    if colonne < 0 or colonne >= len(grille[0]):
        print("Colonne invalide")
        return
    

    for i in range(len(grille) - 1, -1, -1):
        if grille[i][colonne] == "*":
            grille[i][colonne] = "O"
            return

tour_joueur()
affichage_grille()
tour_bot()
affichage_grille()
