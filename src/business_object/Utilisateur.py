class Utilisateur:

    def __init__(self, id_utilisateur: int, nom_utilisateur: str, mot_de_passe: str):
        self.id_utilisateur = id_utilisateur
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe

    def getIdUtilisateur(self):
        return self.id_utilisateur

    def getNomUtilisateur(self):
        return self.nom_utilisateur

    def getMdp(self):
        return self.mot_de_passe

    def afficher_info(self):
        print(f"Utilisateur {self.nom_utilisateur} (ID: {self.id_utilisateur})")
