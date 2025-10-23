#!/bin/bash

tableau=("tableau_V2" "test" "test2")


function test() {
    for i in "${tableau[@]}"; do
        echo "$i"
    done
    read -p "Choissiez un nb : " nb
    echo $nb
}

test

for (( i=0; i -eq 4; i++ )); do
    read -p "entré votre note : " result_$[i]
done