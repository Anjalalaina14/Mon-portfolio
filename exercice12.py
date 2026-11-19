class Employe:
    def __init__(self, nom , salaire_base):
      self.nom = nom 
      self.salaire_base = salaire_base
      
    def calculer_salaire(self):
        return self.salaire_base
    
class Developpeur(Employe):
    def __init__(self, nom, salaire_base, prime_technique):
        super().__init__(nom,salaire_base)
        self.prime_technique = prime_technique
        
    def calculer_salaire(self):
        return self.salaire_base + self.prime_technique
    
class Commercial(Employe):
    def __init__(self, nom, salaire_base, commission):
        super().__init__(nom, salaire_base)    
        self.commission = commission
        
    def calculer_salaire(self):
        return self.salaire_base + self.commission

# Creation de deux dev    
developpeur1 = Developpeur("Soa",1200000,300000)
developpeur2 = Developpeur("Fara",1500000,300000)     

# Creation de deux com
commercial1 = Commercial("Mamy", 1000000,250000)
commercial2 = Commercial("Hery", 1200000,400000)

# Regroupements des employes sans une liste
employes = [developpeur1,developpeur2,commercial1,commercial2]

for employe in employes:
    print("Emlpoye:",employe.nom)
    print("Salaire:",employe.calculer_salaire(),"Ar")
    
                                
                        
    
                