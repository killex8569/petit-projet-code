import random

def main():
    listeBateaux = [
        Bateau(2),
        Bateau(3),
        Bateau(5),
        Bateau(4)
    ]

    plateau = Plateau(10, 10)
    player1 = Player("Alex", listeBateaux, plateau) # le joueur va envoyer ses coups à un plateau en particulier, il doit donc savoir sur quel plateau il est
    player2 = Player("Val", listeBateaux, plateau)
    plateau.addPlayer(player1)
    plateau.addPlayer(player2)

    for x in range(len(listeBateaux)*2):
        plateau.putBoat(plateau.getPlayerList()[x % 2]) # putBoat appelle la fonction putBoat(boat, x, y) de Player

    plateau.begin()
    i = random.randrange(0, 2)
    while not plateau.isGameFinished():
        playerToPlay = plateau.getPlayerList()[i % 2]
        plateau.getMove(playerToPlay) # getMove appelle la fonction fire(x, y) de Player    