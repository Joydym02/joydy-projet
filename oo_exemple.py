class Vehicule:
    numbre = 0
    # constructeur 
    def __init__(self ,v_nom, v_monteur, v_couleur, v_marque):
        self.nom_vehicule = v_nom
        self.monteur = v_monteur
        self.couleur = v_couleur
        self.marque = v_marque
        self.numbre += 1 
    
    def afficher(self):
        print(f"C'est vehicule le {self.nom_vehicule} {self.marque} {self.monteur} {self.couleur}")




v1 = Vehicule("Prado","Diesel","Grise","Toyata")

print(v1.afficher())
