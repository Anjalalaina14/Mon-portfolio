class Employe:
    def __init__(self, nom, salaire_de_base):
        self.nom = nom
        self.salaire_de_base = salaire_de_base

    def afficher_details(self):
        return f"Employé: {self.nom} | Salaire: {self.salaire_de_base}€"

class Manager(Employe):
    def __init__(self, nom, salaire_de_base, bonus):
        # On utilise super() pour initialiser le nom et le salaire via la classe parent
        super().__init__(nom, salaire_de_base)
        # On ajoute la spécificité du Manager
        self.bonus = bonus

    def afficher_details(self):
        # On utilise super() pour récupérer le texte de base de la classe parent
        texte_parent = super().afficher_details()
        # On y ajoute les informations spécifiques au manager
        return f"{texte_parent} | Bonus: {self.bonus}€ (Total: {self.salaire_de_base + self.bonus}€)"


# Création d'un employé standard
employe1 = Employe("Alice", 2500)
print(employe1.afficher_details())

# Création d'un manager
manager1 = Manager("Bob", 4000, 800)
print(manager1.afficher_details())