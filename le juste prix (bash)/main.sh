#!/bin/bash

echo "Bienvenue dans le juste prix"

random_nb=$(( $RANDOM % 1000 + 1)) #Choisi un nombre entre 0 et 1000

vie=10

while [ rep_user != random_nb ]; do
    read -p "votre nombre : " rep_user
    if ((rep_user > random_nb))
    then
        echo -e "\nPlus petit"
        echo "$vie"
    else
        echo "Plus Grand"
        echo "$vie"
    fi
    if (( rep_user == random_nb))
    then
        echo "Vous avez gagnez ! "
        echo "Il vous restait : $vie vie(s)"
        break
    fi


    ((vie--))
    if (( $vie <= 0 )); then
    echo "Perdu, le nb était : $random_nb"
    break
    fi
done