from dao.dao_compte import DaoCompte
from Utilisateur import Utilisateur
from utils.securite import hash_password


class ServiceUtilisateur:

    @log
    def sinscrire(self, nom_utilisateur: str, mot_de_passe=str) -> Utilisateur:
        utilisateur = DaoCompte().creer_utilisateur(
            nom_utilisateur, hash_password(mot_de_passe, nom_utilisateur)
        )
        print(f"Utilisateur {nom_utilisateur} inscrit avec succès.")
        return utilisateur

    @log
    def connecter_utilisateur(self, nom_utilisateur: str, mot_de_passe: str):
        utilisateur = DaoCompte().trouver_utilisateur_par_nom(nom_utilisateur)
        if utilisateur and utilisateur.mot_de_passe == hash_password(mot_de_passe, nom_utilisateur):
            print(f"Utilisateur {nom_utilisateur} connecté avec succès.")
            return utilisateur
        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")
            return None

    @log
    def modifier_informations(self, id_utilisateur: int, nouveau_nom: str, nouveau_mdp: str):
        nouveau_mdp = hash_password(nouveau_mdp, nouveau_nom)
        utilisateur = DaoCompte().mettre_a_jour_utilisateur(
            id_utilisateur, nouveau_nom, nouveau_mdp
        )
        if utilisateur:
            print(f"Les informations de {utilisateur.nom_utilisateur} ont été mises à jour.")
        else:
            print("Utilisateur non trouvé.")
