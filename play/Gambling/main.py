# Gambling

# Plusieurs modes de jeu : 
# Mode Endless: 
# Mode Classique (plusieurs niveau de difficulté)
# All In --> Parie max de son argent à chaque fois 
# Double or nothing


import random
from .Blackjack import BlackJack


class Gambling:
    def __init__(self, nb_joueurs):
        self.somme = 100
        self.nb_joueurs = nb_joueurs

    def menu(self):
        print("1 - ")

    def blackjack(self):
        jeu = BlackJack()
        

        """
        RÈGLES DU BLACKJACK :
        - Le joueur et la banque reçoivent 2 cartes (une carte de la banque est cachée)
        - Les cartes numérales valent leur valeur, les figures (Roi, Dame, Valet) valent 10, l'As vaut 1 ou 11
        - une fois que le joueur à obtenue ces 2 cartes, il peut 'tirer' (prendre une troisième carte) ou 'rester' (ne plus en prendre)
        - Le but est d'approcher 21 sans le dépasser
        - Si le joueur dépasse 21, il 'bust' et perd sa mise
        - La banque tire jusqu'à atteindre au moins 17
        - Celui qui est le plus proche de 21 sans dépasser gagne
        - Un Blackjack naturel (As + figure dès le départ) rapporte 1.5x la mise
        - Mise min 5 mise max 300
        """


        pass

    def craps(self):
        """
        RÈGLES DU CRAPS :
        - Le joueur lance 2 dés
        - Premier lancer (Come-Out Roll) :
            * 7 ou 11 → victoire immédiate
            * 2, 3 ou 12 (Craps) → défaite immédiate
            * Autre valeur → ce chiffre devient le 'Point'
        - Si un Point est établi, le joueur relance jusqu'à :
            * Retomber sur le Point → victoire
            * Tomber sur 7 → défaite (Seven-Out)
        - La mise de base est 1:1
        """
        pass

    def roulette(self):
        """
        RÈGLES DE LA ROULETTE :
        - La roue contient les numéros 0 à 36
        - Le joueur peut parier sur :
            * Un numéro exact (paye 35:1)
            * Rouge ou Noir (paye 1:1)
            * Pair ou Impair (paye 1:1)
            * Manque (1-18) ou Passe (19-36) (paye 1:1)
            * Douzaine : 1-12, 13-24, 25-36 (paye 2:1)
        - Le 0 est vert, ni rouge ni noir — la banque gagne sur tous les paris simples
        - La bille tombe sur un numéro aléatoire, les paris correspondants sont payés
        """
        pass

    def slot_machine(self):
        """
        RÈGLES DE LA MACHINE À SOUS :
        - Le joueur mise une somme et appuie sur 'spin'
        - 3 symboles aléatoires s'affichent : 🍒 🍋 🍊 🍇 ⭐ 💎 7️⃣
        - Gains selon les combinaisons :
            * 3x 💎  → x50 la mise
            * 3x 7️⃣  → x20 la mise
            * 3x ⭐  → x10 la mise
            * 3 identiques (autres) → x5 la mise
            * 2 identiques → x1.5 la mise (remboursé + 50%)
            * Aucune correspondance → mise perdue
        - La machine a un taux de retour de ~90% (léger avantage banque)
        """
        pass

    def coin_flip(self):
        """
        RÈGLES DU COIN FLIP :
        - Le joueur choisit Pile ou Face
        - Une pièce est lancée aléatoirement
        - Bonne prédiction → x2 la mise
        - Mauvaise prédiction → mise perdue
        - Probabilité 50/50, jeu le plus simple du casino
        """
        pass

    def higher_or_lower(self):
        """
        RÈGLES DU HIGHER OR LOWER :
        - Une première carte est retournée face visible
        - Le joueur parie si la prochaine carte sera plus haute ou plus basse
        - Bonne prédiction → x2 la mise
        - Mauvaise prédiction → mise perdue
        - En cas d'égalité → mise remboursée (push)
        - Les cartes vont de 2 à As (As = 14, la plus haute)
        - Plus la différence est grande, plus la prédiction était facile (pas de bonus)
        """
        pass

    def keno(self):
        """
        RÈGLES DU KENO :
        - Le joueur choisit entre 1 et 10 numéros parmi 1 à 80
        - La machine tire 20 numéros aléatoires
        - Le gain dépend du nombre de numéros trouvés (matchés) :
            * 0 matché  → mise perdue
            * 1 matché  → remboursé
            * 3 matchés → x2
            * 5 matchés → x10
            * 7 matchés → x50
            * 10 matchés → x1000 (jackpot)
        - Plus on sélectionne de numéros, plus les gains potentiels sont élevés
        - Mais la probabilité de tout matcher diminue
        """
        pass

    def baccarat(self):
        """
        RÈGLES DU BACCARAT :
        - Le joueur parie sur : Joueur, Banque, ou Égalité — AVANT de voir les cartes
        - Deux mains sont distribuées (Joueur et Banque), chacune reçoit 2 cartes
        - Valeurs : 2-9 = valeur faciale, 10/Figures = 0, As = 1
        - Si le total dépasse 9, seul le chiffre des unités compte (ex: 15 → 5)
        - Règles de tirage automatiques :
            * Joueur tire si son total ≤ 5
            * Banque tire selon des règles fixes dépendant du total Joueur
        - La main la plus proche de 9 gagne
        - Parier sur Banque → x1 la mise (mais commission de 5%)
        - Parier sur Joueur → x1 la mise
        - Parier sur Égalité → x8 la mise
        """
        pass

    def war(self):
        """
        RÈGLES DU CASINO WAR :
        - Le joueur et la banque reçoivent chacun 1 carte face visible
        - La carte la plus haute gagne (2 = plus basse, As = plus haute)
        - Victoire joueur → x1 la mise
        - Victoire banque → mise perdue
        - Égalité → le joueur a deux options :
            * Surrendre : récupère la moitié de sa mise
            * War : double sa mise, une nouvelle carte est tirée
              - Si le joueur gagne le War → remporte uniquement la mise supplémentaire
              - Si la banque gagne le War → perd la mise totale
        """
        pass