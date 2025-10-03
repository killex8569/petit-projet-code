#!/bin/bash

# Règles de la bataille naval : 
# Une grille de 1 à 10 (horizontal) et de A à J (Verticale)
# 
#
#
#
#
# Mode possibles : 
# 1 - Mode solo (Jouer avec une "ia")
# 2 - Jouer avec un pote en local 
#
# Description 2 : Entre chaque tour, le joueur doit cliquer sur "Enter" pour voir la grille (sinon le joueur d'avant pourrais voir les bateaux de l'autre).
#                 Aussi, Le dernier joueurs à mettre en place ces bateaux est le premier à jouer (pareils, sinon il pourrais voir les bateaux de l'adversaire)


# Création d'une grille de 1 à 10 et de A à J

taille_grille=10
letters=(A B C D E F G H I J)
grille_de_jeux=($(for ((i=0; i<taille_grille*taille_grille; i++)); do echo "_"; done))


for ((i=0; i<${#grille_de_jeux[@]}; i++)); do
    if (( (i) % taille_grille == 0)); then
        echo # Saut de ligne entre chaque ligne
        printf "%s" "${letters[i/taille_grille]}"
        printf " " # Espace entre Lettre et Grille
    fi
    printf "%s" "${grille_de_jeux[$i]}"
    printf " "
done
echo

