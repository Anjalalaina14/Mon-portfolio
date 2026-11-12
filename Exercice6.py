class Produit:
    def __init__(self , nom , prix):
        self.nom = nom
        self.prix = prix
        
class Commande:
    def __init__(self , produit , quantite):
        self.produit = produit
        self.quantite = quantite
        
    def calculer_total(self):
        return self.produit.prix * self.quantite
            
    
    def afficher(self):
        print(f"{self.produit.nom} : {self.quantite} : {self.calculer_total()} Ar") 
        
# Creation produit
produit = Produit("Sac", 40000)

# Creation commande
commande = Commande(produit, 2)

# Calcul montant total
print("Montant total:", commande.calculer_total(), "Ar") 
commande.afficher()

                   