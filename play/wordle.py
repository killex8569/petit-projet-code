# Règle : Trouver le mot cacher, nous avons à notre disposition une ligne de _ avec le nombre de lettre et 
# nous avons droit à 5 erreurs pour trouver le mot, l'objectif est de reconstituer le mot lettre par lettre
#Si le mot est trouver, on augmente la streak de 1 (On propose de rejouer, si oui on incrémente de 1 et on préscise de nombre de partie et leurs difficultés)
# Si le mot est pas trouver, perdu (plus de streak) et on propose si l'on souhaite recommencer une partie
# 
# Pour présciser leurs difficulté --> Streak : 1 difficile, 2 facile et 3 moyens --> Créer d'une liste puis fin de partie .append du niveau de dificulté (1, 2, 3 ou 4)
#
# Plusieurs difficultés, facile, moyen, difficile, expert 
# --> Chaques difficultés possède sa propriété --> facile 7 chances mot entre 5 et 8 lettres, expert, 4 "essaies" et mot entre 8 et 13 lettres, 


# Option de dev --> Implémenter une recherche de mot (Genre pour en rajouter, si y'en à beaucoup ça vas être galère)

liste_mot_facile = []
liste_mot_moyen = []
liste_mot_difficile = []
liste_mot_expert = []

def main_wordle():
    print("Bienvenue dans Wordle ! ")


def dev_research():
    liste = ["courgette", "test", "baguette"]
    recherche = str(input("Votre mot ? : "))
    for i in range(0, len(liste)):
        if recherche == liste[i]:
            print("le mot est dans la liste")
            break
