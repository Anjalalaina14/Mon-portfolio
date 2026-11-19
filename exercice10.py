# Classe mère
class Transport:
    def se_deplacer(self):
        print("Ce moyen de transport se deplace")
        
# Classe fille 1
class Voiture(Transport):
    def se_deplacer(self):
        print("La voiture roule sur la route")  
        
# Classe fille 2 
class Avion(Transport):
    def se_deplacer(self):
        print("L'avion vole dans l'air")  
        
# Classe fille 3
class Bateau(Transport):
    def se_deplacer(self):
        print("Le bateau navigue sur l'eau")  
        
# Creation des objets
voiture1 = Voiture()
avion1 = Avion()
bateau1 = Bateau()

# Placements des objets dans une liste
transports = [voiture1,avion1,bateau1]

# Parcourt de la liste avec une boucle
for transport in transports:
    transport.se_deplacer()                        