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