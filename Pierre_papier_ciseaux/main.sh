#!/bin/bash

# Variable global
user_rep=0
ordi_rep=0
score_user=0
score_ordi=0


# Définir la fonction
function choix_joueur() {
    read -p "Quels choix ? (P/F/C) : " tmp # input
    user_rep=${tmp^^} # Majuscule
    if [[ $user_rep != "P" && $user_rep != "C" && $user_rep != "F" ]]; then # Verif si l'input est bon
        echo "réponse incorrect ! "
        choix_joueur
    fi
    echo $user_rep
    choix_ordinateur
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
    echo "rep ordi : $ordi_rep"
    determiner_gagnant $user_rep $ordi_rep
}

function determiner_gagnant() {
    while [[ $score_ordi != 3 || $score_user != 3 ]]; do
        echo "nombre d'arguments : $#"
        if [[ $user_rep == $ordi_rep ]]; then
            echo "Egalité"
        elif [[ $user_rep == "P" && $ordi_rep == "C" ]]; then # Opération ET logique, si les deux sont vrai alors ...
            echo "Joueur à gagner"
            (($score_user++))
            echo $score_user
        elif [[ $user_rep == "F" && $ordi_rep == "P" ]]; then
            echo "Joueur à gagner"
            (($score_user++))
        elif [[ $user_rep == "C" && $ordi_rep == "F" ]]; then
            echo "Joueur à gagner"
            (($score_user++))
        else
            echo "Robot à gagner"
            (($score_ordi++))
        fi
        choix_joueur
    done
    if [[ $score_ordi -gt 3 || $score_user -gt 3 ]]; then
        end_game
    fi
}

function end_game() {
    if [[ $score_ordi -lt $score_user ]]; then
        echo "Joueur 1 à Gagner"
    else
        echo "Ordi à gagner"
    fi
}
choix_joueur