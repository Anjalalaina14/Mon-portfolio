class CompteBancaire:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde
        
    def afficher_solde(self):
        print("Titulaire :" ,self.nom)
        print("Solde disponible :" ,self.solde, "Ar" )  
        
class CompteEpargne(CompteBancaire):
    def __init__(self, nom, solde, taux_interet):
       super().__init__(nom, solde)
       self.taux_interet = taux_interet
    def afficher_solde(self):
        super().afficher_solde()
        print(f"Taux d'interet :" ,self.taux_interet, "%") 
                 
    def calculer_interet(self):
        interet = self.solde *self.taux_interet /100
        print("Montant des interets :", interet, "Ar")
        
#Creation de l'objet
compte1 = CompteEpargne("Miora",500000, 5)    
#Affichage des informations
compte1.afficher_solde()

#Calcul des interets
compte1.calculer_interet()       