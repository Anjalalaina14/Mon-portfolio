class Formation:
    def __init__(self , intitule , duree):
        self.intitule = intitule
        self.duree = duree
        
      
        
class Etudiant:
    def __init__(self , nom , age , formation):
        self.nom = nom
        self.age = age
        self.formation = formation
        
    def afficher_information(self):
        print(f"nom :{self.nom }")
        print(f"age:{self.age}")
        print(f"formation:{self.formation.intitule}")
            
        
# Creation d' un objet Formation
formation1= Formation("Patisserie", 2)  

# Creation formation de deuc etudiants
etudiant1 = Etudiant("Alice" , 20, formation1) 
etudiant2 = Etudiant("Maelys" , 22, formation1)

# Information de chaque etudiant
print("Etudiant1")
etudiant1.afficher_information()
print("Etudiant2")
etudiant2.afficher_information()
      
        
                
        