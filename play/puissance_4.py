# Règle du puissance 4 : Chaque joueur à son tour peut placer une X ou un O, le permier qui fait une suite (diagonal, horizontal ou vertical) à gagner la partie 
# --> 6 de hauteur 7 de largeur
# Fonctionnalité à rajouter --> Multi joueur local --> Possibilité de joueur à 2 sur le même pc et de mettre des noms (Au tour de : Killex par exemple)
import random
import time

ROWS = 6
COLS = 7
grille = [["*"] * COLS for _ in range(ROWS)]

suite = 4

def clear_screen():
    print("\033[H\033[J", end="")


def clean_up():
    global grille # modifie la variable
    grille = [["*"] * COLS for _ in range(ROWS)] # Etat initial


def affichage_grille():
    # Affichage de la grille
    for ligne in grille:
        print(" ".join(map(str, ligne)))
    for i in range(1, COLS + 1): # Boucle de 1 à COLS +1 inclu
        print(i, end=" ") # Tout sur la même ligne
    print("") # saut de ligne

def tour_joueur(player_name):
    print("tour du joueur : ", player_name)
    rep_user = int(input("Quelle colonne voulez jouer ? : "))
    colonne = rep_user - 1

    # Sécurité
    if colonne < 0 or colonne >= len(grille[0]):
        print("Colonne invalide")
        return
    
    for i in range(len(grille) - 1, -1, -1):
        if grille[i][colonne] == "*":
            grille[i][colonne] = "X"
            clear_screen()
            affichage_grille()
            return
        


def tour_joueur2(player_name):
    print("tour du joueur : ", player_name)
    rep_user = int(input("Quelle colonne voulez jouer ? : "))
    colonne = rep_user - 1

    # Sécurité
    if colonne < 0 or colonne >= len(grille[0]):
        print("Colonne invalide")
        return
    
    for i in range(len(grille) - 1, -1, -1):
        if grille[i][colonne] == "*":
            grille[i][colonne] = "O"
            clear_screen()
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
            clear_screen()
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




def joueurVsBot():
    joueur1 = str(input("Veuillez renseigner votre nom : "))
    while True:
        tour_joueur(joueur1)
        if verif_victoire("X"):
            print("Bien jouer, tu as gagner !")
            clean_up()
            break
        tour_bot()
        if verif_victoire("O"):
            print("Dommage, le bot à gagner")
            clean_up()
            break


def joueurVsjoueur():
    joueur1 = str(input("Veuillez renseigner le nom du joueur 1 : "))
    joueur2 = str(input("Veuillez renseigner le nom du joueur 2 : "))
    while True:
        try:
            tour_joueur(joueur1)
            if verif_victoire("X"):
                print("Le joueur 1 : ", joueur1, "remporte la partie")
                clean_up()
                break
            tour_joueur2(joueur2)
            if verif_victoire("O"):
                print("Le joueur 2 : ", joueur2, "remporte la partie")
                clean_up()
                break
        except ValueError:
            print("Mauvaise entrée, veuillez réessayez...") 

def main():
    while True:
        try:
            print("Bienvenue dans le main Menu : \nSéléctionner votre mode de jeu : \n1 - Joueur Vs Bot\n2 - Joueur Vs Joueur\n3 - Quitter")
            rep_user = (int(input("Votre choix : ")))
            if rep_user == 1:
                joueurVsBot()
            elif rep_user == 2:
                joueurVsjoueur()
            elif rep_user == 3:
                print("Good bye")
                break
        except ValueError:
            print("Mauvaise entrée, veuillez réessayez...")       