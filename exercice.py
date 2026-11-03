class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
        
    def afficher(self):
        print("Produit :",self.nom)
        print("Prix :" ,self.prix, "Ar")
        print("Quantite :" ,self.quantite)
        
produit1 = Produit("Robe", 20000, 5)
produit1.afficher()           
