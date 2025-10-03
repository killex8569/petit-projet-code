#!/bin/bash

# Tableau à plusieurs valeurs

tableau=("_ _ _" "_ _ _" "_ _ _") # Tableau en bash

for tableau in "${tableau[@]}"; do
    tableau="_ * _"
    echo "$tableau"
done

# Création d'une grille de 1 à 10 et de A à J

taille_grille=10
letters=(A B C D E F G H I J)
grille_de_jeux=("1 2 3" "4 5" "")
# grille_de_jeux=($(for ((i=0; i<taille_grille*taille_grille; i++)); do echo "_"; done))

#for ((i=0; i<${#grille_de_jeux[@]}; i++)); do
#    if (( i % taille_grille == 0)); then # Verifie si le nb est divisable par 10
#        echo # Saut de ligne entre chaque ligne
#        printf "%s" "${letters[i/taille_grille]}"
#        printf " " # Espace entre Lettre et Grille
#    fi
#    printf "%s" "${grille_de_jeux[$i]}"
#    printf " "
#done


echo

