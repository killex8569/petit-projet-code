from abc import *
from dataclasses import dataclass
class Cours:
    # Constructeur
    def __init__(self, titre, nb_etudiant, duree):
        # Données publiques --> Modifications possibles
        self.titre = titre
        self.etudiants = nb_etudiant
        self.duree = duree

        # Données privées
        self._proteger = 10
        
        # Données privées
        self.__prive = 100

    def afficher_infos(self):
        print(f"Titre du cours : {self.titre}")
        print(f"Etudiants : {self.etudiants}")
        print(f"Temps : {self.duree}")
# c = Cours()
    def ajouter_etudiant(self, etudiant):
        self.etudiants += etudiant

class GetterSetter:
    def __init__(self, titre, etudiants, duree):
        self.titre = titre
        self.duree = duree
        self.__etudiants = etudiants
    def get_nb_etudiants(self):
        # if is_admin:
        return self.__etudiants
        # else:
            # print("Vous n'avez pas les permissions")
    def set_etudiants(self, valeur):
        if valeur >= 0:
            self.__etudiants = valeur
        else: 
            print("Erreur")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        


    def partir_en_pause(self):
        print(self.name, "par en pause")

class Developper(Employee):
    def __init__(self, name, salary, code_editor):
        super().__init__(name, salary)
        self.code_editor = code_editor

    def dev(self):
        print(f"{self.name}, commence le dev avec {self.code_editor}")


class Designer(Employee):
    def __init__(self, name, salary, software):
        super().__init__(name, salary)
        self.software = software

    def designer(self):
        print(f"{self.name}, se met à designer avec {self.software}")


class Forme(ABC):
    @abstractmethod
    def surface(self):
        pass

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur

    def surface(self):
        return self.largeur * self.hauteur


# Composition

class Adresse:
    def __init__(self, rue, ville):
        self.rue = rue
        self.ville = ville

    def afficher(self):
        return self.rue, self.ville

class Utilisateur:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
    def afficher_info(self):
        print(f"Utilisateur : {self.nom}, adresse : {self.adresse.afficher()}")



# Dunder

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
    
    # Permet de return le titre et l'auteur, sinon on aurait une adresse mémoire
    def __str__(self):
        return f"{self.titre} de {self.auteur}"
    



# Dataclass

# Class normal
class Utilisateur:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

# Dataclasse 
@dataclass
class User:
    nom: str
    age: int

u1 = Utilisateur("Michel", 30)
u2 = User("Bob", 40)
print(u2)














"""

livre = Livre("1984", "Goerge Orwell")
print(livre)


adr = Adresse("453 Avenue coin strip", "Strasbourg")
u = Utilisateur("Michel", adr)
u.afficher_info()


r = Rectangle(4, 5)
print(r.surface())



alice = Designer("Alice", 5000, "Krita")
bob = Developper("Bob", 6000, "VsCode")

bob.partir_en_pause()
bob.dev()
alice.partir_en_pause()
alice.designer()





# Apelle getter
c = GetterSetter("Cours algo", 20, 50)
c.set_etudiants(30)
print(c.get_nb_etudiants())







# Pour class Cours


c1 = Cours(titre="Cour d'algo", nb_etudiant=30, duree=30)
c2 = Cours(titre="Cour de POO", nb_etudiant=0, duree=60)


# Pas de sécurité mais une bonne pratique
# print(c2.__prive)
# print(c2._Cours__prive)

# c1.afficher_infos()
c2.afficher_infos()

c2.ajouter_etudiant(10)
c2.afficher_infos()


"""