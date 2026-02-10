import logic as l


def main():
    print("Bienvenue sur le menu principal")
    while True:
        try:
            print("Mode de jeux : \n1 - Mode Solo\n2 - Mode multi (PVP)\n3 - Custom\n4 - Quitter")
            rep_user = int(input("Quelle mode de jeu voulez vous séléctionner : "))
        except ValueError:
            print("Entrée invalide.")
            continue
        match rep_user:
            case 1:
                start_game()
            case 2:
                print("Encore en developpement")
            case 3:
                print("Encore en developpement")
            case 4:
                print("Au revoir")
                break



def start_game():
    game = l.Board()
    nb_bateau = 5 # temporaire, mode custom permetteras de le modifier
    bateau_placer = 0
    game.clean_up()
    
    while bateau_placer < nb_bateau:
        try:
            game.display()
            print("Bateau numéro : ", bateau_placer + 1)
            row = int(input("Placer votre bateau sur qu'elle ligne : "))
            col = int(input("Placer votre bateau sur qu'elle collone : "))
            lenght = int(input("Qu'elle longeur fera votre bateau : "))
            orientation = input("Dans qu'elle sens voulez-vous votre bateau (H/V) : ").strip().upper()
            if row < 0 or row >= 10 or col < 0 or col >= 10:
                print("Position hors grille")
                continue

            if lenght < 1 or lenght > 5:
                print("Longueur invalide")
                continue
            if orientation not in ("H", "V"):
                print("Orientation invalide")
                continue              
        except ValueError:
            print("Entrée invalide.")
            continue
        
        if game.place_ship(row, col, lenght, orientation):
            game.clear_screen()
            print("Bateau placé")
            game.display()
            bateau_placer += 1
            if bateau_placer == 5:
                while not game.has_lost():
                    try:
                        game.clear_screen()
                        game.display()
                        rows = int(input("Sur qu'elle ligne voulez vous tirer : "))
                        cols = int(input("Sur qu'elle colonne voulez vous tirer : "))
                        game.receive_hit(rows, cols)
                    except ValueError:
                        print("Entrée invalide.")
                        continue  
        else:
            print("Placement impossible")
            continue



if __name__ == "__main__":
    main()
