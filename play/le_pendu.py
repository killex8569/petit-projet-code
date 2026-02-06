# Le jeu du pendu classique
# Liste de mot complète (avec une fonction pour le dev --> Permet de rechercher si un mot est présent dans la liste)

def dev_research():
    liste = ["courgette", "test", "baguette"]
    recherche = str(input("Votre mot ? : "))
    for i in range(0, len(liste)):
        if recherche == liste[i]:
            print("le mot est dans la liste")
            break
