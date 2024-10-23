class Utilisateur:

    def __init__(self, nom_utilisateur: str, mdp: str, id_utilisateur=None):
        self.nom_utilisateur = nom_utilisateur
        self.mdp = mdp
        self.id_utilisateur = id_utilisateur


"""
    def getIdUtilisateur(self):
        return self.id_utilisateur

    def getNomUtilisateur(self):
        return self.nom_utilisateur

    def getMdp(self):
        return self.mdp

    def afficher_info(self):
        print(f"Utilisateur {self.nom_utilisateur} (ID: {self.id_utilisateur})") """
