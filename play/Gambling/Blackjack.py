class BlackJack:
    def __init__(self):
        self.JeuCartes = []
        self.valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        self.couleurs = ["Pique", "Coeur", "Carreau", "Trèfle"]

    def build(self):
        for couleur in self.couleurs:
            for valeur in self.valeurs:
                self.JeuCartes.append(valeur)
                print(f"valeur : {valeur} | Couleur : {couleur}")
        return self.JeuCartes