class Forme:
    def calculer_surface(self):
        pass
    
class Rectangle(Forme):
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur =  largeur   
        
    def calculer_surface(self):
        return self.longueur*self.largeur
    
class Carre(Forme):
    def __init__(self,cote):
        self.cote = cote
        
    def calculer_surface(self):
        return self.cote*self.cote
    
class Cercle(Forme):
    def __init__(self,rayon):
        self.rayon = rayon 
    def calculer_surface(self):
        return 3.14 * self.rayon * self.rayon    
    
rectangle1 = Rectangle(5,4)
carre1 = Carre(5)
cercle1 = Cercle(5)

formes = [rectangle1, carre1, cercle1]

print("Rectangle : surface =",rectangle1.calculer_surface()) 
print("Carre : surface =", carre1.calculer_surface()) 
print("Cercle : surface =", round(cercle1.calculer_surface(),2))       
            
    
        