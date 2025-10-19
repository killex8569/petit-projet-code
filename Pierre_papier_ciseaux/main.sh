#!/bin/bash

# Variable global (définis une seul fois pour tout le document)
user_rep=0
ordi_rep=0
score_user=0
score_ordi=0

function jeu() { # Fonction qui permet de faire la boucle (on aurait pu la mettre aussi dans la function : choix_joueur, mais c'est plus propre comme ça)
    while [[ $score_user -lt 3 && $score_ordi -lt 3 ]]; do
        choix_joueur
        choix_ordinateur
        determiner_gagnant "$user_rep" "$ordi_rep"
    done


}

# Définir la fonction
function choix_joueur() {
    read -p "Quels choix ? (P/F/C) : " tmp # User input
    user_rep=${tmp^^} # Input transformer en Majuscule
    if [[ $user_rep != "P" && $user_rep != "C" && $user_rep != "F" ]]; then # Verif si l'input est bon
        echo "réponse incorrect ! "
        choix_joueur # Rapelle de la même fonction si la reponse n'est pas correcte
    fi
    echo $user_rep
}

function choix_ordinateur() {
    ordi_rep=$(( $RANDOM % 3 )) # Tire un nb random entre 0 et 2 (Attention, c'est 3 non inclu)
    if [[ $ordi_rep == 0 ]]; then # Si rep == 0 alors P
        ordi_rep="P"
    fi
    if [[ $ordi_rep == 1 ]]; then # Si rep == 1 alors F
        ordi_rep="F"
    fi
    if [[ $ordi_rep == 2 ]]; then # Si rep == 3 alors C
        ordi_rep="C"
    fi
}

function determiner_gagnant() { # Définis toutes les possibilité de victoire, égalité ou défaite
    if [[ $user_rep == $ordi_rep ]]; then
        echo "Egalité" # Egalité
    elif [[ $user_rep == "P" && $ordi_rep == "C" ]]; then # Opération ET logique, si les deux sont vrai alors ...
        echo "Joueur à gagner le tour" # Victoire User
        ((score_user++))
        echo $score_user
    elif [[ $user_rep == "F" && $ordi_rep == "P" ]]; then
        echo "Joueur à gagner le tour" # Victoire User
        ((score_user++))
        echo $score_user
    elif [[ $user_rep == "C" && $ordi_rep == "F" ]]; then
        echo "Joueur à gagner le tour" # Victoire User
        ((score_user++))
        echo $score_user
    else
        echo "Ordi à gagner le tour" # Victoire Ordi
        ((score_ordi++))
        echo $score_ordi
    fi
    if [[ $score_ordi -gt 2 || $score_user -gt 2 ]]; then
        end_game
    fi
}

function end_game() {
    if [[ $score_ordi -lt $score_user ]]; then
        echo "JOUEUR REMPORTE LA VICTOIRE ! "
    else
        echo "ORDI REMPORTE LA VICTOIRE !"
    fi
}

jeu # Apelle la fonction jeu