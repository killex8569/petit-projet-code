# Plusieurs modes : 
# Mode solo (joueur vs bot/automate)
# Mode multi joueur
# Mode IA (Vari IA entrainer à jouer)
# 
# Créer en POO python 

import random
import time
import client.client as cli

class Board:
    def __init__(self, rows=10, cols=10):
        pass
        self.ROWS = rows
        self.COLS = cols
        self.grid = [[" " for _ in range(cols)] for _ in range(rows)]



    def create_grid(self, rows, cols):
        return [["*"] * cols for _ in range(rows)]
    
    def clear_screen(self):
        print("\033[H\033[J", end="")
        
    def clean_up(self, COLS, ROWS):
        grille = [["*"] * self.COLS for _ in range(self.ROWS)] # Etat initial
    def getPlayerName(self):
        return self.player_name
    
    def setPlayerName(self, player_name):
        return player_name



c = Board()

c.setPlayerName("Alexandre")
print(c.getPlayerName())


