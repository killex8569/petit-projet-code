import PPC as pfc
import test as t

def main_menu():
    while True:
        print("menu principal")
        print("quelle est le jeu que vous voulez faire : \n1 - Pierre feuille ciseau\n2 - le juste nombre\n3 - Quitter")
        try:
            rep_user = int(input("Quel est votre choix ? : "))
        except ValueError:
            print("Entrée invalide.")
            continue

        match rep_user:
            case 1:
                pfc.main_pfc()
            case 2:
                t.main()
            case 3:
                break
            case _:
                print("Choix invalide.")
if __name__ == "__main__":
    main_menu()
