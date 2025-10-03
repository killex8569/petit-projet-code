#!/bin/bash

# Tableau à plusieurs valeurs

tableau=("1 2 3" "4 5 6" "7 8 9") # Tableau en bash

for tableau in "${tableau[@]}"; do
    echo "$tableau"
done

# Création d'une grille de 1 à 10 et de A à J

taille_grille=10

grille_de_jeux=($(for ((i=0; i<taille_grille*taille_grille; i++)); do echo "_"; done))


for ((i=0; i<${#grille_de_jeux[@]}; i++)); do
    echo "${grille_de_jeux[$i]}"
    if (( (i+1) % taille_grille == 0)); then
        echo;
    fi
done
