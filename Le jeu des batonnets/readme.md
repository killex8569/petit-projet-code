Le jeu des bâtonnets (démocratisé en France grâce à Fort Boyard) nous permet de jouer selon les règles suivantes :  

- Le jeu se joue avec 2 joueurs (2 humains, un ordinateur et un humain, ou 2 ordinateurs → implémenter les 3 modes de jeu).  
- Il y a un total de 20 bâtonnets.  
- Les joueurs/ordinateurs ne peuvent retirer par tour qu'un, deux ou trois bâtonnets maximum.  
- Le dernier à retirer un bâtonnet a perdu.  

- Implémenter un système de tour aléatoire (pas toujours le même joueur qui commence).  
- Créer une IA "Impossible" → connaît l'astuce pour gagner, mais reste soumise au tirage du premier joueur.  

## Astuce pour gagner
Il faut laisser l'adversaire commencer, puis toujours calculer pour retirer 4 bâtonnets au total à chaque tour. Par exemple : si l'adversaire retire 1 bâtonnet, vous en retirez 3 ; s'il en retire 2, vous en retirez 2, etc.
