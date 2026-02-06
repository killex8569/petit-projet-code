# Règle du puissance 4 : Chaque joueur à son tour peut placer une X ou un O, le permier qui fait une suite (diagonal, horizontal ou vertical) à gagner la partie 
# --> 6 de hauteur 7 de largeur

import random
import time

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
    rep_user = int(input("Quelle colonne voulez jouer ? : "))
    colonne = rep_user - 1

    # Sécurité
    if colonne < 0 or colonne >= len(grille[0]):
        print("Colonne invalide")
        return
    
    for i in range(len(grille) - 1, -1, -1):
        if grille[i][colonne] == "*":
            grille[i][colonne] = "X"
            affichage_grille()
            return
        
def tour_bot():
    print("tour du BOT (Les O)")
    time.sleep(1)
    colonne = random.randint(0, COLS - 1)

    # Sécurité
    if colonne < 0 or colonne >= len(grille[0]):
        print("Colonne invalide")
        return
    

    for i in range(len(grille) - 1, -1, -1):
        if grille[i][colonne] == "*":
            grille[i][colonne] = "O"
            affichage_grille()
            verif_victoire("X")
            return

def verif_victoire(type_joueur):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(grille[r][c+i] == type_joueur for i in range(4)):
                return True

    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(grille[r+i][c] == type_joueur for i in range(4)):
                return True

    # Diagonal montante (/) 
    # On part des lignes 3 à 5 et on remonte
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if (grille[r][c] == type_joueur and 
                grille[r-1][c+1] == type_joueur and 
                grille[r-2][c+2] == type_joueur and 
                grille[r-3][c+3] == type_joueur):
                return True

    # Diagonal descendante (\)
    # On part des lignes 0 à 2 et on descend
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if (grille[r][c] == type_joueur and 
                grille[r+1][c+1] == type_joueur and 
                grille[r+2][c+2] == type_joueur and 
                grille[r+3][c+3] == type_joueur):
                return True
    return False




def main():
    while True:
        tour_joueur()
        if verif_victoire("X"):
            print("Bien jouer, tu as gagner !")
            break
        tour_bot()
        if verif_victoire("O"):
            print("Dommage, le bot à gagner")
            break
main()