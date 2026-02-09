# Programmation Orientée Objet (POO) vs Programmation Procédurale

![Illustration](./data/image.png)

La programmation procédurale repose principalement sur l'utilisation de
fonctions et de structures de données manipulées directement.
La programmation orientée objet (POO), quant à elle, structure le code
autour d'objets qui encapsulent à la fois des **données (attributs)** et
des **comportements (méthodes)**.

**Équivalence conceptuelle :**
- Méthode (POO) ≈ Fonction (procédural)
La différence majeure est qu'une méthode est liée à un objet et agit sur
son état interne.

**Avantages de la POO :** - Meilleure modularité du code
- Réutilisabilité accrue
- Maintenance facilitée
- Meilleure modélisation de systèmes complexes

------------------------------------------------------------------------

## `self`

Le paramètre `self` est obligatoire dans les méthodes d'instance en
Python.

Il représente une référence vers **l'instance actuelle** de la classe.
Chaque objet possède donc son propre contexte.

``` python
class Personne:
    def __init__(self, nom):
        self.nom = nom
```

**Points importants :** - `self` est une convention, mais elle doit être
respectée pour la lisibilité du code. - Ce n'est **pas** un mot-clé
Python. - Il permet d'accéder aux attributs et aux autres méthodes de
l'objet.

------------------------------------------------------------------------

## Vocabulaire

**Objet (Instance)**
Entité concrète créée à partir d'une classe.

``` python
p = Personne("Alice")
```

**Classe**
Modèle (template) permettant de créer des objets. Elle définit les
attributs et les comportements.

**Méthode**
Fonction définie dans une classe et opérant sur ses instances.

**Attribut**
Variable associée à une instance ou à une classe.

**Encapsulation**
Principe consistant à regrouper données et comportements tout en
contrôlant l'accès aux informations internes.

------------------------------------------------------------------------

# Encapsulation

L'encapsulation permet de : 

- protéger l'intégrité des données

- éviter les modifications non contrôlées

- définir des règles d'accès.

### Niveaux d'accès en Python

Python ne possède pas de véritables modificateurs (`public`, `private`,
`protected`) comme Java ou C++, ni de contrôle strict d'accès. Il repose
sur des conventions :

-   **Public** : `variable`
-   **Protégé (convention)** : `_variable`
-   **Privé (name mangling)** : `__variable`

``` python
class Exemple:
    def __init__(self):
        self.public = 1
        self._protege = 2
        self.__prive = 3
```

⚠️ Le privé n'est pas totalement inaccessible : Python applique un
mécanisme appelé **name mangling** (`_NomDeClasse__variable`).
L'objectif est surtout d'éviter les erreurs, pas de garantir une
sécurité absolue.

------------------------------------------------------------------------

# Getters et Setters

Ils permettent de contrôler l'accès aux attributs (lecture et écriture)
et d'ajouter des validations.

``` python
class Compte:
    def __init__(self, solde):
        self._solde = solde

    def get_solde(self):
        return self._solde

    def set_solde(self, valeur):
        if valeur >= 0:
            self._solde = valeur
```

Cependant, en Python moderne, on privilégie souvent `@property`.

------------------------------------------------------------------------

# `@property` en Python

Le décorateur `@property` permet d'exposer une méthode comme un attribut
tout en gardant un contrôle interne.

``` python
class Compte:
    def __init__(self, solde):
        self._solde = solde

    @property
    def solde(self):
        return self._solde

    @solde.setter
    def solde(self, valeur):
        if valeur < 0:
            raise ValueError("Le solde ne peut pas être négatif.")
        self._solde = valeur
```

**Avantage majeur :**
Changer l'implémentation interne sans casser le code existant.

------------------------------------------------------------------------

# Héritage

L'héritage permet à une classe enfant de récupérer les attributs et
méthodes d'une classe parent.

``` python
class Animal:
    def parler(self):
        print("L'animal fait un bruit")

class Chien(Animal):
    pass
```

Python supporte aussi **l'héritage multiple**, mais il doit être utilisé
avec prudence pour éviter une complexité excessive (problème de
résolution des méthodes --- MRO).

------------------------------------------------------------------------

# Polymorphisme

Le polymorphisme permet d'utiliser une même interface pour des
comportements différents.

``` python
class Animal:
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        print("Wouf")

class Chat(Animal):
    def parler(self):
        print("Miaou")
```

Même appel, comportement différent :

``` python
for animal in [Chien(), Chat()]:
    animal.parler()
```

👉 Cela favorise un code extensible sans modifier l'existant.

------------------------------------------------------------------------

# Abstraction

L'abstraction consiste à définir un **contrat** que les classes dérivées
doivent respecter.

On utilise généralement le module `abc` :

``` python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def parler(self):
        pass
```

Une classe abstraite : - ne peut pas être instanciée, - force
l'implémentation des méthodes abstraites.

Objectif : imposer une architecture claire.

------------------------------------------------------------------------

# Composition

La composition consiste à construire une classe en utilisant d'autres
classes comme composants.

``` python
class Clavier:
    pass

class Ordinateur:
    def __init__(self):
        self.clavier = Clavier()
```

**Avantage clé :**
Souvent préférable à l'héritage → relation **"possède un"** plutôt que
**"est un"**.

👉 Favorise un couplage plus faible et une meilleure flexibilité.

------------------------------------------------------------------------

# Méthodes Dunder (Double Underscore)

Les méthodes spéciales, appelées **dunder methods** (`__nom__`),
permettent de modifier le comportement natif des objets.

Exemples : - `__init__` : constructeur - `__str__` : affichage
utilisateur - `__repr__` : représentation pour les développeurs -
`__len__` : longueur - `__add__` : opérateur `+` - `__eq__` :
comparaison d'égalité

![Dunder](./data/dunder.png)

### Exemple

``` python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

![Comparaison](./data/dunder_comparaison.png)
![Add et repr](./data/dunder_add_et_repr.png)

------------------------------------------------------------------------

# Dataclasses

Les **dataclasses** simplifient la création de classes servant
principalement à stocker des données.

Elles génèrent automatiquement : - `__init__` - `__repr__` - `__eq__` -
et d'autres méthodes utiles.

``` python
from dataclasses import dataclass

@dataclass
class Personne:
    nom: str
    age: int
```

**Pourquoi les utiliser ?** - Moins de code boilerplate
- Meilleure lisibilité
- Idéales pour les objets immuables ou les structures de données

⚠️ À privilégier lorsque la classe contient surtout des données et peu
de logique métier.

------------------------------------------------------------------------

# Bonnes pratiques en POO Python

-   Favoriser la **composition** plutôt que l'héritage lorsque possible.
-   Éviter les hiérarchies trop profondes.
-   Respecter le principe **SRP (Single Responsibility Principle)** :
    une classe = une responsabilité.
-   Ne pas sur-architecturer : toute abstraction doit répondre à un
    besoin réel.
-   Penser à la maintenabilité avant l'optimisation prématurée.
