class Module:
    def __init__(self , titre , duree):
        self.titre = titre
        self.duree = duree
        
class Formation:
    def __init__(self , intitule):
        self.intitule = intitule
        self.modules = []
        
    def ajouter_module(self ,module):
        self.modules.append(module)
        
        
class Apprenant:
    def __init__(self , nom):
        self.nom = nom
        self.formations = []
        
    def s_inscrire(self,formation):
        print(f"Apprenant",self.nom)
        for formation in self.formations:
            print(f"Formation",formation.intitule)
            
        for module in formation.modules:
            print(module.titre,module.duree,"heures")
            
# Creation des formations
formation1 = Formation("Patisserie")
formation2 = Formation("Cuisine")

# Creation des modules
module1 = Module("Entremets et Gateaux de voyage", 50)
module2 = Module("Glacages", 20)
module3 = Module("Trompe l'oeil", 30)
module4 = Module("Bases Sakafo Malagasy", 25)
module5 = Module("Entrees froides et chaudes", 30)
module6 = Module("Desserts de Restauration", 20)

# Ajout des modules aux formations
formation1.ajouter_module(module1)
formation1.ajouter_module(module2)
formation1.ajouter_module(module3)

formation2.ajouter_module(module4)
formation2.ajouter_module(module5)
formation2.ajouter_module(module6)

# Creation des Apprenants
apprenant1 = Apprenant("Soa")
apprenant2 = Apprenant("Antsa")

# Inscriptions
apprenant1.s_inscrire(formation1)
apprenant1.s_inscrire(formation2)
apprenant2.s_inscrire(formation2)

# Affichages des parcours
apprenant1.afficher_parcours()

apprenant2.afficher_parcours()



            
                
          
                
                
        