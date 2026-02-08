import PFC as pfc
import jp as jp
import puissance_4 as p4
import Bataille_naval.main as bn_main


def main_menu():
    while True:
        print("menu principal")
        print("quelle est le jeu que vous voulez faire : \n1 - Pierre feuille ciseau\n2 - le juste nombre\n3 - Bataille naval\n4 - gambling\n5 - jeu batonnet\n6 - pendu\n7 - mastermind\n8 - morpions\n9 - wordle\n10 - mot mêle\n11 - petit BAC\n12 - reflexe\n13 - Puissance 4\n\n20 - Quitter")
        try:
            rep_user = int(input("Quel est votre choix ? : "))
        except ValueError:
            print("Entrée invalide.")
            continue

        match rep_user:
            case 1:
                pfc.main_pfc()
            case 2:
                jp.main_jp()
            case 3:
                bn_main.main()
            case 4:
                continue
            case 5:
                continue
            case 6:
                continue
            case 7:
                continue
            case 8:
                continue
            case 9:
                continue
            case 10:
                continue
            case 11:
                continue
            case 12:
                continue
            case 13:
                p4.main()
            case 20:
                print("Au revoir")
                break
            case _:
                
                print("Choix invalide.")
if __name__ == "__main__":
    main_menu()
