class Apprenant:
    def __init__(self , nom ,identifiant):
        self.nom = nom 
        self.identifiant = identifiant
        self.modules = []
        
                   
    def inscrire(self,module): 
        self.modules.append(module)  
        
    def afficher_module(self):
        print(f"Nom :", self.nom)
        print(f"Identifiant :", self.identifiant)
        print(f"Modules suivis :")
        for module in self.modules:
            print(module.titre, module.nombre_heures, "heures")    
        
class Module:
    def __init__(self ,titre , nombre_heures ):
        self.titre = titre
        self.nombre_heures = nombre_heures 
        
    
       
            
# Creation des apprenants et modules
apprenant1 = Apprenant("Alice" , 100)
apprenant2 = Apprenant("Maya" , 101)  

module1 = Module("Patisserie" , 20)
module2 = Module("Arts" , 15) 
module3 = Module("Cuisine" , 25)

# Inscription de chaque apprenant
apprenant1.inscrire(module1)
apprenant1.inscrire(module2)

apprenant2.inscrire(module1)
apprenant2.inscrire(module3)

# Affichage des inscriptions
print("Apprenant1")
apprenant1.afficher_module()
print("Apprenant2")
apprenant2.afficher_module()
           
        
        
                
                