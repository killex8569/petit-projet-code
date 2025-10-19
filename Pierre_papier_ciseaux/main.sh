#!/bin/bash

# Variable global
user_rep=0
ordi_rep=0
score_user=0
score_ordi=0

function jeu() {
    while [[ $score_user -lt 3 && $score_ordi -lt 3 ]]; do
        choix_joueur
        choix_ordinateur
        determiner_gagnant "$user_rep" "$ordi_rep"
    done

}

# Définir la fonction
function choix_joueur() {
    read -p "Quels choix ? (P/F/C) : " tmp # input
    user_rep=${tmp^^} # Majuscule
    if [[ $user_rep != "P" && $user_rep != "C" && $user_rep != "F" ]]; then # Verif si l'input est bon
        echo "réponse incorrect ! "
        choix_joueur
    fi
    echo $user_rep
}

function choix_ordinateur() {
    ordi_rep=$(( $RANDOM % 3 ))
    if [[ $ordi_rep == 0 ]]; then
        ordi_rep="P"
    fi
    if [[ $ordi_rep == 1 ]]; then
        ordi_rep="F"
    fi
    if [[ $ordi_rep == 2 ]]; then
        ordi_rep="C"
    fi

}

function determiner_gagnant() {
    if [[ $user_rep == $ordi_rep ]]; then
        echo "Egalité" # Egalité
    elif [[ $user_rep == "P" && $ordi_rep == "C" ]]; then # Opération ET logique, si les deux sont vrai alors ...
        echo "Joueur à gagner"
        ((score_user++))
        echo $score_user
    elif [[ $user_rep == "F" && $ordi_rep == "P" ]]; then
        echo "Joueur à gagner"
        ((score_user++))
        echo $score_user
    elif [[ $user_rep == "C" && $ordi_rep == "F" ]]; then
        echo "Joueur à gagner"
        ((score_user++))
        echo $score_user
    else
        echo "Robot à gagner"
        ((score_ordi++))
        echo $score_ordi
    fi
    if [[ $score_ordi -gt 3 || $score_user -gt 3 ]]; then
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
jeu