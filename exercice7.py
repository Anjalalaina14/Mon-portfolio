class Livre:
    def __init__(self , titre , auteur , annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee 
        
    def afficher_details(self):
        print(f"{self.titre} : {self.annee} : {self.auteur}")
        
        
class Bibliotheque:
    def __init__(self):
        self.livre = []
        
    def ajouter_livre(self,livre):
       self.livre.append(livre)
        
    def afficher_catalogue(self):
        for livre in self.livre:
            livre.afficher_details()
            
        
# Creation des trois objets livres
livre1 = Livre("Orgeuil et Prejuges" , "Jane Austen" , 1813)
livre2 = Livre("L'Alchimiste" , "Paulo Coelho" , 1988)
livre3 = Livre("Devenir" , "Michelle Obama" , 2018)

# Creation de la bibliotheque
bibliotheque = Bibliotheque()

# Ajouter des livres a la bibliotheque
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)

# Afficher le catalogue complet
bibliotheque.afficher_catalogue()               
                   
        