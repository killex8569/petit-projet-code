import random

def main_jp():
    try:
        user_input = input("Insérer la range (défaut 1000): ")
        range_user = int(user_input) if user_input else 1000
    except ValueError:
        range_user = 1000

    nb = random.randint(1, range_user)
    est_trouver = False
    compteur = 0
    while not est_trouver:
        try:
            nb_user = int(input("Veuillez insérer un nombre : "))
        except ValueError:
            print("Entrée invalide.")
            continue

        if nb_user > nb:
            print("C'est MOINS !")
            compteur += 1

        elif nb_user < nb:
            print("C'est PLUS")
            compteur += 1

        else:
            print("Bien joué, vous avez trouvé le nombre !", nb)
            print("Vous avez réussi en : ", compteur, " essaies")
            est_trouver = True


                