from dao.dao_compte import DaoCompte
from business_object.utilisateur import Utilisateur
from utils.securite import hash_password
from utils.log_decorator import log


class ServiceUtilisateur:
    """Classe contenant les méthodes de service pour gérer les utilisateurs."""

    @log
    def _valider_mot_de_passe(self, mot_de_passe: str) -> bool:
        """Valider un mot de passe en fonction des critères de sécurité définis.

        Parameters
        ----------
        mot_de_passe : str
            Le mot de passe à valider.

        Returns
        -------
        bool
            True si le mot de passe est valide, False sinon.
        """
        return DaoCompte()._valider_mot_de_passe(mot_de_passe)

    @log
    def sinscrire(self, nom_utilisateur: str, mot_de_passe=str) -> Utilisateur:
        """Inscrire un utilisateur avec un nom d'utilisateur et un mot de passe haché.

        Parameters
        ----------
        nom_utilisateur : str
            Le nom d'utilisateur de l'utilisateur à inscrire.
        mot_de_passe : str
            Le mot de passe de l'utilisateur à inscrire.

        Returns
        -------
        Utilisateur
            L'objet Utilisateur créé si l'inscription réussit, None sinon.
        """

        utilisateur = DaoCompte().creer_utilisateur(
            Utilisateur(nom_utilisateur, hash_password(mot_de_passe, nom_utilisateur))
        )
        print(f"Utilisateur {nom_utilisateur} inscrit avec succès.")
        return utilisateur

    @log
    def connecter_utilisateur(self, nom_utilisateur: str, mot_de_passe: str) -> Utilisateur:
        """Connecter un utilisateur en vérifiant son nom d'utilisateur et son mot de passe.

        Parameters
        ----------
        nom_utilisateur : str
            Le nom d'utilisateur de l'utilisateur à connecter.
        mot_de_passe : str
            Le mot de passe de l'utilisateur à connecter.

        Returns
        -------
        Utilisateur
            L'utilisateur connecté si les informations sont correctes, None sinon.
        """
        utilisateur = DaoCompte().trouver_utilisateur_par_nom(nom_utilisateur)
        if utilisateur and utilisateur.mdp == hash_password(mot_de_passe, nom_utilisateur):
            print(f"Utilisateur {nom_utilisateur} connecté avec succès.")
            return utilisateur
        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")
            return None

    @log
    def modifier_informations(self, nouveau_nom: str, nouveau_mdp: str):
        """Modifier un utilisateur existant en mettant à jour son mot de passe (haché).

        Parameters
        ----------
        utilisateur : Utilisateur
            L'objet Utilisateur à modifier.

        Returns
        -------
        retourne True si les informations de l'utilisateur ont été mises à jour avec succès, sinon elle retourne False.
        """
        nouveau_mdp = hash_password(nouveau_mdp, nouveau_nom)
        utilisateur = DaoCompte().mettre_a_jour_utilisateur(nouveau_nom, nouveau_mdp)
        if utilisateur:
            print(f"Les informations de {utilisateur.nom_utilisateur} ont été mises à jour.")
        else:
            print("Utilisateur non trouvé.")

    @log
    def modifier(self, utilisateur) -> Utilisateur:
        """Modification d'un utilisateur.


        Parameters
        ----------
        utilisateur : Utilisateur
            L'objet Utilisateur à modifier.

        Returns
        -------
        Utilisateur
            L'utilisateur mis à jour si la modification réussit, None sinon.
        """

        utilisateur.mot_de_passe = hash_password(
            utilisateur.mot_de_passe, utilisateur.nom_utilisateur
        )
        return utilisateur if DaoCompte().modifier(utilisateur) else None

    @log
    def lister_tous(self, inclure_mdp=False) -> list[Utilisateur]:
        """Lister tous les utlisateurs
        Si inclure_mdp=True, les mots de passe seront inclus
        Par défaut, tous les mdp des joueurs sont à None.

        Parameters
        ----------
        inclure_mdp : bool, optional
            Si True, les mots de passe des utilisateurs seront inclus, par défaut False.

        Returns
        -------
        list[Utilisateur]
            La liste des utilisateurs. Les mots de passe sont masqués si inclure_mdp est False.
        """
        utilisateurs = DaoCompte().lister_tous()
        if not inclure_mdp:
            for u in utilisateurs:
                u.mdp = None
        return utilisateurs

    @log
    def trouver_utilisateur_par_nom(self, nom_utilisateur) -> Utilisateur:
        """Trouver un utilisateur à partir de son nom d'utilisateur.

        Parameters
        ----------
        nom_utilisateur : str
            Le nom d'utilisateur de l'utilisateur à rechercher.

        Returns
        -------
        Utilisateur
            L'objet Utilisateur correspondant au nom donné, ou None si aucun utilisateur n'est trouvé.
        """
        return DaoCompte().trouver_utilisateur_par_nom(nom_utilisateur)
