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
    print("create_grille")
    i = 0
    while i <= taille_grille:
        nb = random.randrange(90)
        list_tableau.append(nb)
        i = i + 1
    print(list_tableau)

create_grille(bingo_1_j)
print("test : ", bingo_1_j)