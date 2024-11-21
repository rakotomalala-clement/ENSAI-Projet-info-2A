from dao.dao_compte import DaoCompte
from business_object.utilisateur import Utilisateur
from utils.securite import hash_password
from utils.log_decorator import log


class ServiceUtilisateur:

    @log
    def _valider_mot_de_passe(self, mot_de_passe: str) -> bool:
        return DaoCompte()._valider_mot_de_passe(mot_de_passe)

    @log
    def sinscrire(self, nom_utilisateur: str, mot_de_passe=str) -> Utilisateur:
        utilisateur = DaoCompte().creer_utilisateur(
            Utilisateur(nom_utilisateur, hash_password(mot_de_passe, nom_utilisateur))
        )
        print(f"Utilisateur {nom_utilisateur} inscrit avec succès.")
        return utilisateur

    @log
    def connecter_utilisateur(self, nom_utilisateur: str, mot_de_passe: str):
        utilisateur = DaoCompte().trouver_utilisateur_par_nom(nom_utilisateur)
        if utilisateur and utilisateur.mdp == hash_password(mot_de_passe, nom_utilisateur):
            print(f"Utilisateur {nom_utilisateur} connecté avec succès.")
            return utilisateur
        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")
            return None

    @log
    def modifier_informations(self, nouveau_nom: str, nouveau_mdp: str):
        nouveau_mdp = hash_password(nouveau_mdp, nouveau_nom)
        utilisateur = DaoCompte().mettre_a_jour_utilisateur(nouveau_nom, nouveau_mdp)
        if utilisateur:
            print(f"Les informations de {utilisateur.nom_utilisateur} ont été mises à jour.")
        else:
            print("Utilisateur non trouvé.")

    @log
    def modifier(self, utilisateur) -> Utilisateur:
        """Modification d'un utilisateur"""

        utilisateur.mot_de_passe = hash_password(
            utilisateur.mot_de_passe, utilisateur.nom_utilisateur
        )
        return utilisateur if DaoCompte().modifier(utilisateur) else None

    @log
    def lister_tous(self, inclure_mdp=False) -> list[Utilisateur]:
        """Lister tous les utlisateurs
        Si inclure_mdp=True, les mots de passe seront inclus
        Par défaut, tous les mdp des joueurs sont à None
        """
        utilisateurs = DaoCompte().lister_tous()
        if not inclure_mdp:
            for u in utilisateurs:
                u.mdp = None
        return utilisateurs

    @log
    def trouver_utilisateur_par_nom(self, nom_utilisateur) -> Utilisateur:
        return DaoCompte().trouver_utilisateur_par_nom(nom_utilisateur)
