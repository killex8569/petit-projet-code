# Plusieurs modes : 
# Mode solo (joueur vs bot/automate)
# Mode multi joueur
# Mode IA (Vari IA entrainer à jouer)
# 
# Créer en POO python 

import random
import time


class Board:
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        self.grid = [[" " for _ in range(cols)] for _ in range(rows)]

    def is_placement_valide(self, row, col, length, orientation):
        if orientation == "H":
            # Horizontal
            if col + length > self.cols:
                return False
            # Collision entre bateau ? (superposition)
            for i in range(length):
                if self.grid[row][col + i] != " ": # Si différent d'un espace sur la longeur d'un bateau, alors False
                    return False
        elif orientation == "V":
            # Vertical
            if row + length > self.rows:
                return False
            # Collision entre bateau ? (superposition)
            for i in range(length):
                if self.grid[row + i][col] != " ": # Si différent d'un espace sur la longeur d'un bateau, alors False
                    return False
        return True

    def display(self):
        # Affiche l'écran
        print("  " + " ".join(str(i) for i in range(self.cols)))
        for r in range(self.rows):
            print(f"{r} " + "|".join(self.grid[r]))   

    def place_ship(self, row, cols, length, orientation):
        if self.is_placement_valide(row, cols, length, orientation) == True:
            for i in range(length):
                    # Horizontal
                if orientation == "H":
                    self.grid[row][cols + i] = "S"
                    # Vertical
                elif orientation == "V":
                    self.grid[row + i][cols] = "S"
            return True # Placement réussi
        return False # Placement pas bon


    def receive_hit(self, row, col):
        if row >= self.rows or col >= self.cols:
            print("En dehors de la grille")
        else:
            if self.grid[row][col] == "S":
                self.grid[row][col] = "X"
                return "HIT"
            elif self.grid[row][col] == " ":
                self.grid[row][col] = "O"
                return "MISS"
            elif self.grid[row][col] == "X" or self.grid[row][col]== "O":
                print("Déjà tirer")

    def clear_screen(self):
        print("\033[H\033[J", end="")
        
    def clean_up(self):
        grille = [["*"] * self.cols for _ in range(self.rows)] # Etat initial


