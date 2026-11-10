class Moteur:
    def __init__(self, marque , puissance):
       self.marque = marque
       self.puissance = puissance
       
    def demarrer(self):
        print(f"le moteur demarre")
    
class Voiture:
    def __init__(self, moteur):
        self.moteur = moteur
        
    def demarrer(self):
        print(f"la voiture demarre")
    
moteur =  Moteur("Kia", 120) 
voiture = Voiture(moteur)     
voiture.demarrer()    
                
    