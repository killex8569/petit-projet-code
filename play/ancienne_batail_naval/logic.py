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
        self.ships_list = []
        # On créer la grille
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        # On garde une trace des tires (pour l'affichage)
        self.hits = [[False for _ in range(cols)] for _ in range(rows)]

    def is_placement_valide(self, row, col, length, orientation):
        if row < 0 or col < 0 or orientation not in ("H", "V"):
            return False
        if orientation == "H":
            # Horizontal
            if col + length > self.cols:
                return False
            # Collision entre bateau ? (superposition)
            for i in range(length):
                if self.grid[row][col + i] is not None: # Si différent d'un espace sur la longeur d'un bateau, alors False
                    return False
        elif orientation == "V":
            # Vertical
            if row + length > self.rows:
                return False
            # Collision entre bateau ? (superposition)
            for i in range(length):
                if self.grid[row + i][col] is not None: # Si différent d'un espace sur la longeur d'un bateau, alors False
                    return False
        return True 

    def place_ship(self, ship, row, col, orientation):
        if self.is_placement_valide(row, col, ship.size, orientation):
            for i in range(ship.size):
                r, c = (row + i, col) if orientation == "V" else (row, col + i)
                # IMPORTANT : On met l'OBJET ship dans la grille, pas juste un texte "S"
                self.grid[r][c] = ship
            return True
        self.ships_list.append(ship)
        return False


    def display(self, hide_ships=False):
            # On améliore l'affichage : si c'est un bateau et qu'on n'a pas tiré -> "S"
            # Si c'est un bateau et qu'on a tiré -> "X"
            print("  " + " ".join(str(i) for i in range(self.cols)))
            for r in range(self.rows):
                row_str = []
                for c in range(self.cols):
                    cell = self.grid[r][c]
                    hit = self.hits[r][c]
                    
                    if isinstance(cell, Ship):
                        if hit: row_str.append("X") # Touché
                        else: row_str.append("S" if not hide_ships else " ") # Caché ou visible
                    else:
                        row_str.append("O" if hit else " ") # Loupé ou vide
                print(f"{r} " + "|".join(row_str))
    
    def reive_hit(self, row, col):
        self.hits[row][col] = True
        target = self.grid[row][col]

        if isinstance(target, Ship): # Si l'objet à cet endroit est un Bateau
            target.hit()
            return "HIT"
        return "MISS"

    def clear_screen(self):
        print("\033[H\033[J", end="")
        
    def clean_up(self):
        self.grid = [None * self.cols for _ in range(self.rows)] # Etat initial




# Gère nom, type et longeur
class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.health = size
        self.position = []
        self.is_sunk = False

    def hit(self):
        if self.health > 0:
            self.health -= 1
        elif self.health == 0:
            self.is_sunk = True
            return True
        return False
    
    def is_sunk(self):
        if self.health == 0:
            return True
        return False

class GameEngine:
    # Doit contenir Game_Over
    def __init__(self):
        self.player_board = Board()
        self.opponent_board = Board()
        self.is_game_over = False

    def setup_bot_game(self, row, col):
        # Le bot vas devoirs placer ces bateaux via random
        pass
    def game_over(self, player):
        return True




