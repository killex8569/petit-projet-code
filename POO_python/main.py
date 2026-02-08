class Cours:
    def __init__(self, titre, nb_etudiant, duree):
        self.titre = titre
        self.etudiants = nb_etudiant
        self.duree = duree

    def afficher_infos(self):
        print(f"Titre du cours : {self.titre}")
        print(f"Etudiants : {self.etudiants}")
        print(f"Temps : {self.duree}")
# c = Cours()

c1 = Cours(titre="Cour d'algo", nb_etudiant=30, duree=30)
c2 = Cours(titre="Cour de POO", nb_etudiant=30, duree=30)

c1.afficher_infos()
