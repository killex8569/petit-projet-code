# Jeu du pierre papier ciseau en python
# A faire : 
# Corriger l'entrée utilisateur (tape X t c'est perdu)
import random
class Pfc:
    def __init__(self):
        self.nb_point = 0
        self.nb_round = 3
        self.nb_point_bot = 0
        self.rep = ["P", "F", "C"]

    def game(self):
        while self.nb_point < self.nb_round and self.nb_point_bot < self.nb_round:
            rep_bot = random.choice(self.rep)
            rep_user = str(input("Veuillez choisir entre P F C : ")).upper()
            if rep_user == "P" and rep_bot == "C":
                print("Vous avez gagner", rep_bot)
                self.nb_point += 1
            elif rep_user == "F" and rep_bot == "P":
                print("Vous avez gagner", rep_bot)
                self.nb_point += 1
            elif rep_user == "C" and rep_bot == "F":
                print("vous avez gagner", rep_bot)
                self.nb_point += 1
            elif rep_bot == rep_user:
                print("Égalité", rep_bot)
            else:
                print("Vous avez perdu", rep_bot)
                self.nb_point_bot += 1


    def setGameConfig(self):
        newNbPoint = int(input("Combiens de round voulez vous : "))
        if newNbPoint > 0:
            self.nb_round = newNbPoint
        else:
            return "Votre config n'est pas bonne"
        
    def getGameConfig(self):
        print("nombre de round : ", self.nb_round)
    
    def menu(self):
       while True:
            print("1 - Jeu\n2 - Set config\n3 - Show config\n4- Quitter")
            rep_user = int(input("Que voulez vous faire : "))
            match rep_user:
                case 1:
                    self.game()
                case 2:
                    self.setGameConfig()
                case 3:
                    self.getGameConfig()
                case 4 :
                    break
                case _:
                    print("Choix invalide")

