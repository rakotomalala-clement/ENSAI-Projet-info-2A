from dao.dao_compte import DaoCompte
from Utilisateur import Utilisateur


class ServiceUtilisateur:

    def __init__(self, dao_compte: DaoCompte):
        self.dao_compte = dao_compte

    def sinscrire(self, nom_utilisateur: str, mot_de_passe=str) -> Utilisateur:
        utilisateur = self.dao_compte.creer_utilisateur(nom_utilisateur, mot_de_passe)
        print(f"Utilisateur {nom_utilisateur} inscrit avec succès.")
        return utilisateur

    def connecter_utilisateur(self, nom_utilisateur: str, mot_de_passe: str):
        utilisateur = self.dao_compte.trouver_utilisateur_par_nom(nom_utilisateur)
        if utilisateur and utilisateur.mot_de_passe == mot_de_passe:
            print(f"Utilisateur {nom_utilisateur} connecté avec succès.")
            return utilisateur
        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")
            return None

    def modifier_informations(self, id_utilisateur: int, nouveau_nom: str, nouveau_mdp: str):
        utilisateur = self.dao_compte.mettre_a_jour_utilisateur(
            id_utilisateur, nouveau_nom, nouveau_mdp
        )
        if utilisateur:
            print(f"Les informations de {utilisateur.nom_utilisateur} ont été mises à jour.")
        else:
            print("Utilisateur non trouvé.")
