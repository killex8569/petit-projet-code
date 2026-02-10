# Informations général

Grille de 1 à 10 (colonne), et de A à J (ligne) (Augmentation de cette graille possible)

--> Voir architecture client serveur.
TCP, le serveur vas contenire l'état de la partie, c'est lui qui valide les coups, il empêche la triche, il sync les clients (Choisir asyncio)

## Coté serveur (Classes POO)
Classe coté serveur : 
- Game
- Board
- Ship
- Player
- Server




### Game

- état global
- tour actuel
- victoire
- règles

### Board

- grille
- placements
- tirs reçus

### Ship

- positions
- touché / coulé

### Player

- socket
- board
- pseudo
- prêt / pas prêt

## Coté client (Classes POO)
Client
CLI
ProtocolHandler


## Protocol réseau

Client --> Serveur
```
{
  "type": "fire",
  "x": 4,
  "y": 7
}
```

Serveur --> Client
```
{
  "type": "result",
  "hit": true,
  "sunk": false
}
```


## Gestion des erreurs

- client qui crash
- socket fermé
- timeout
- packet incomplet


## En plus (Pas obligatoire mais utile pour se distinguer)

- Reconnexion d’un ou de plusieurs joueurs
- Spectateurs
- Plusieurs parties simultanées --> Multi threading
- IA
- Dockerisation
- Tests unitaires



## Modes de jeux

### Mode personnaliser

possible amélioration : 

- Possible d'intégrer une fonctionnalité "progressive", tout les 5 tours et jusqu'a ce qu'il obtien un total de 5 bateau (ou plus selon paramètre), il commence avec un bateau et le joueur à la possibilité de faire venir un nouveau bateau.
- Choisir la taille de la grille (par défaut 10, 10)
- Choisir le nombre de bateau et leurs type (Combiens de Destroyer, de Sous marin, de port-avions etc...)
- Ajouter des nouveau objets et power Up (Genre un radar pour voirs les 4 Cases autour de celle séléctionner par le joueur, un powerUp qui permet de tirer 2 coup si on le souhaite etc... Surement d'autres powerUp, par défaut désactiver, uniquement présent si le joueur coche la case "Actvation des powerup")

### Mode Solo

Mode Solo --> Automate intélligent (si bateau toucher, alors il tests autour des autres zones du tire réussi) sinon tir aléatoire

### Mode multiJoueur

Mode multiJoueur --> Client serveur, le serveur ne s'arrête pas tant que l'on pas à entrer stop ou ctrl + c. Plusieurs parties en même temps peuvent être commencer.
Information supplémentaire --> Chaque client peut lancer depuis l'interface un serveur ou s'y connecter (Host or connect --> Demande d'ip pour connexion ou lors de la création --> Propose de configurer les settings, le nom du serveur etc...)

### Mode IA

Mode IA (bien plus tard)



## Amélioration possible



