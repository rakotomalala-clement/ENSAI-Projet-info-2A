from utils.log_decorator import log

from business_object.avis import Avis
from dao.avis_dao import DaoAvis


class ServiceAvis:
    """Classe contenant les méthodes de services des Avis"""

    @log
    def ajouter_avis(self, id_utilisateur, id_manga, avis, note):
        """Création d'un avis à partir de ses attributs

        Parameters:
        -----------
        id_utilisateur: int
            Identifiant de l'utilisateur qui souhaite créer un avis.

        id_manga: int
            Identifiant du manga sur lequel l'utilisateur souhaite laisser un
            avis.

        avis: str
            texte de l'avis.

        note: int
            note de l'avis.

        Returns:
        --------
        nouveau_avis: avis
            Renvoie l'avis qui a été ajouté.
        """

        nouveau_avis = Avis(note, avis)
        return (
            nouveau_avis
            if DaoAvis().creer_avis(id_utilisateur, id_manga, nouveau_avis, "projet_info_2a")
            else None
        )

    @log
    def ajouter_avis_collection(self, id_utilisateur, id_collection, type_collection, avis, note):
        """Création d'un avis sur une collection à partir de ses attributs

        Parameters:
        -----------
        id_utilisateur: int
            Identifiant de l'utilisateur qui souhaite créer un avis.

        id_collection: int
            Identifiant de la collection sur laquelle l'utilisateur souhaite
            laisser un avis.

        type_collection: str
            Type de la collection sur laquelle on souhaite laisser un avis.
            type_collection = "Coherente" ou "Physique".

        avis: str
            texte de l'avis.

        note: int
            note de l'avis.

        Returns:
        --------
        nouveau_avis: avis
            Renvoie l'avis qui a été ajouté.
        """

        nouveau_avis_collection = Avis(note, avis)
        if type_collection == "Coherente":
            return (
                nouveau_avis_collection
                if DaoAvis().creer_avis_collection_coherente(
                    id_utilisateur, id_collection, nouveau_avis_collection, "projet_info_2a"
                )
                else None
            )
        elif type_collection == "Physique":
            return (
                nouveau_avis_collection
                if DaoAvis().creer_avis_collection_physique(
                    id_collection, id_utilisateur, nouveau_avis_collection, "projet_info_2a"
                )
                else None
            )
        else:
            raise Exception("type_collection incorrect")

    @log
    def afficher_avis_user(self, id_utlisateur, id_manga):
        """Afficher l'avis qu'un utilisateur a laisser sur un  manga

        Parameters:
        -----------

        id_utilisateur: int
            identifiant de l'utilisateur dont on souhaite chercher les avis
            sur un manga

        id_manga: int
            identifiant du manga pour lequel on souhaite récolter les avis laissés
            par un utilisateur

        Returns:
        --------
            Renvoie l'avis trouvé si il existe sinon renvoie None.
        """

        avis_user_sur_manga = DaoAvis().chercher_avis("projet_info_2a", id_utlisateur, id_manga)

        if len(avis_user_sur_manga) > 0:
            return avis_user_sur_manga[0]
        else:
            return None

    @log
    def afficher_avis_collection_coherente(self, id_collection):
        """Afficher les avis laisser sur une collection cohérente

        Parameters:
        -----------

        id_collection: int
            identifiant de la collection pour laquelle on souhaite récolter les avis laissés
            par les utilisateurs

        Returns:
        --------
        avis_user_sur_col_co: Liste[Avis]
            Renvoie les avis trouvé si ils existent sinon renvoie None.
        """

        avis_user_sur_col_co = DaoAvis().chercher_avis_sur_collection_coherente(
            "projet_info_2a", id_collection
        )

        if len(avis_user_sur_col_co) > 0:
            return avis_user_sur_col_co
        else:
            return None

    @log
    def afficher_avis_collection_physique(self, id_collection):
        """Afficher les avis laisser sur une collection physique

        Parameters:
        -----------

        id_collection: int
            identifiant de la collection pour laquelle on souhaite récolter les avis laissés
            par les utilisateurs

        Returns:
        --------
        avis_user_sur_col_phy: Liste[Avis]
            Renvoie les avis trouvé si ils existent sinon renvoie None.
        """

        avis_user_sur_col_phy = DaoAvis().chercher_avis_sur_collection_physique(
            "projet_info_2a", id_collection
        )

        if len(avis_user_sur_col_phy) > 0:
            return avis_user_sur_col_phy
        else:
            return None

    @log
    def afficher_avis_user_sur_collection_coherente(self, id_utilisateur, id_collection):
        """
        Afficher avis d'un utilisateur laissé sur une collection cohérente

        Parameters:
        -----------
        id_utilisateur: int
            id de l'utilisateur dont on veut afficher l'avis.

        id_collection: int
            Identifiant de la collection pour laquel on souhaite récolter
            l'avis de l'utilisateur.

        Returns
        -------
        avis_user_sur_col_co: Avis
            Renvoie l'avis touvé si il existe, renvoie None sinon.

        """

        avis_user_sur_col_co = DaoAvis().chercher_avis_user_sur_collection_coherente(
            "projet_info_2a", id_utilisateur=id_utilisateur, id_collection_coherente=id_collection
        )

        if len(avis_user_sur_col_co) > 0:
            return avis_user_sur_col_co[0]
        else:
            return None

    @log
    def afficher_avis_user_sur_collection_physique(self, id_utilisateur, id_collection):
        """
        Afficher avis d'un utilisateur laissé sur une collection physique

        Parameters:
        -----------
        id_utilisateur: int
            id de l'utilisateur dont on veut afficher l'avis.

        id_collection: int
            Identifiant de la collection pour laquel on souhaite récolter
            l'avis de l'utilisateur.

        Returns
        -------
        avis_user_sur_col_phy: Avis
            Renvoie l'avis touvé si il existe, renvoie None sinon.

        """

        avis_user_sur_col_phy = DaoAvis().chercher_avis_user_sur_collection_physique(
            "projet_info_2a", id_utilisateur=id_utilisateur, id_collection=id_collection
        )

        if len(avis_user_sur_col_phy) > 0:
            return avis_user_sur_col_phy[0]
        else:
            return None

    @log
    def modifier(self, id_manga, id_utilisateur, avis_message, note) -> Avis:
        """Modification d'un avis

        Parameters:
        -----------
        id_manga: int
            identifiant du manga sur lequel se trouve l'avis que l'on souhaite
            modifier.

        id_utilisateur: int
            identifiant de l'utilisateur qui souhaite modifier son avis.

        avis_message : str
            nouveau texte de l'avis.

        note: int
            nouvelle note de l'avis.

        Returns
        -------
        avis: Avis
            Renvoie nouvelle avis si il a bien été modifier, renvoie None sinon.
        """
        avis = Avis(note, str(avis_message))

        return (
            avis
            if DaoAvis().modifier_avis(
                schema="projet_info_2a", id_manga=id_manga, id_utilisateur=id_utilisateur, avis=avis
            )
            else None
        )

    @log
    def modifier_collection_cohérente(
        self, id_collection, id_utilisateur, avis_message, note
    ) -> Avis:
        """Modification d'un avis d'une collection coherente

        Parameters:
        -----------
        id_collecton: int
            identifiant de la collectionsu laquelle se trouve l'avis que l'on souhaite
            modifier.

        id_utilisateur: int
            identifiant de l'utilisateur qui souhaite modifier son avis.

        avis_message : str
            nouveau texte de l'avis.

        note: int
            nouvelle note de l'avis.

        Returns
        -------
        avis: Avis
            Renvoie nouvelle avis si il a bien été modifier, renvoie None sinon.
        """
        avis = Avis(note, avis_message)

        return (
            avis
            if DaoAvis().modifier_avis_collection_co(
                schema="projet_info_2a",
                id_collection=id_collection,
                id_utilisateur=id_utilisateur,
                avis=avis,
            )
            else None
        )

    @log
    def modifier_collection_physique(
        self, id_collection, id_utilisateur, avis_message, note
    ) -> Avis:
        """Modification d'un avis d'une collection physique

        Parameters:
        -----------
        id_collecton: int
            identifiant de la collectionsu laquelle se trouve l'avis que l'on souhaite
            modifier.

        id_utilisateur: int
            identifiant de l'utilisateur qui souhaite modifier son avis.

        avis_message : str
            nouveau texte de l'avis.

        note: int
            nouvelle note de l'avis.

        Returns
        -------
        avis: Avis
            Renvoie nouvelle avis si il a bien été modifier, renvoie None sinon.
        """
        avis = Avis(note, avis_message)

        return (
            avis
            if DaoAvis().modifier_avis_collection_phy(
                schema="projet_info_2a",
                id_collection=id_collection,
                id_utilisateur=id_utilisateur,
                avis=avis,
            )
            else None
        )

    @log
    def supprimer(self, id_avis) -> bool:
        """Supprimer un avis

        Parameters:
        -----------
        id_avis:
            identifiant de l'avis que l'on souhaite supprimé.

        Returns:
        --------
        Bool:
            Return True si la suppression à bien été effectué.
        """
        return DaoAvis().supprimer_avis("projet_info_2a", id_avis)

    @log
    def supprimer_avis_collection_cohérente(self, id_avis):
        """Supprimer un avis sur collection coherente

        Parameters:
        -----------
        id_avis:
            identifiant de l'avis que l'on souhaite supprimé.

        Returns:
        --------
        Bool:
            Return True si la suppression à bien été effectué.
        """
        return DaoAvis().supprimer_avis_col_coherente(
            schema="projet_info_2a", id_avis_collection_coherente=id_avis
        )

    @log
    def supprimer_avis_collection_physique(self, id_avis):
        """Supprimer un avis sur collection physique

        Parameters:
        -----------
        id_avis:
            identifiant de l'avis que l'on souhaite supprimé.

        Returns:
        --------
        Bool:
            Return True si la suppression à bien été effectué.
        """
        return DaoAvis().supprimer_avis_col_physique(
            schema="projet_info_2a", id_avis_collection_physique=id_avis
        )

    @log
    def afficher_autre_avis(self, id_manga):
        """Afficher les avis laisser sous  un manga

        Parameters:
        -----------
        id_manga: int
            identifiant du manga sur lequel on souhaite consulter les avis
            laisser par les utilisateurs.

        Returns:
        --------
        avis_user_sur_manga: Liste[Avis]
            Renvoie liste d'avis laisser par les utilisateurs sur un manga,
            renvoie None si cette liste est vide.
        """
        avis_user_sur_manga = DaoAvis().chercher_avis_sur_manga("projet_info_2a", id_manga)
        if len(avis_user_sur_manga) > 0:
            return avis_user_sur_manga
        else:
            return None

    @log
    def trouver_auteur_avis_sur_manga(self, id_avis, id_manga):
        """
        Permet de trouver le nom d'utilisateur de celui qui à écrit l'avis

        Parameters:
        -----------
        id_avis: int
            identifiant de l'avis dont on souhaite connaitre l'auteur.

        id_manga: int
            identifiant du manga sur lequel se trouve l'avis.

        Returns:
        --------
        username: str
            nom d'utilisateur de l'auteur de l'avis
        """
        username = DaoAvis().trouver_auteur_avis_sur_manga(
            schema="projet_info_2a", id_avis=id_avis, id_manga=id_manga
        )
        return username

    @log
    def trouver_auteur_avis_sur_col_co(self, id_avis_collection_coherente, id_collection_coherente):
        """
        Permet de trouver le nom d'utilisateur de celui qui à écrit l'avis

        Parameters:
        -----------
        id_avis_collection_coherente: int
            identifiant de l'avis dont on souhaite connaitre l'auteur.

        id_collection_coherente: int
            identifiant de la collection sur laquelle se trouve l'avis.

        Returns:
        --------
        username: str
            nom d'utilisateur de l'auteur de l'avis
        """
        username = DaoAvis().trouver_auteur_avis_sur_col_co(
            schema="projet_info_2a",
            id_avis_collection_coherente=id_avis_collection_coherente,
            id_collection_coherente=id_collection_coherente,
        )
        return username

    @log
    def trouver_auteur_avis_sur_col_phy(self, id_avis_collection_physique, id_collection):
        """
        Permet de trouver le nom d'utilisateur de celui qui à écrit l'avis

        Parameters:
        -----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_avis_collection_physique: int
            identifiant de l'avis dont on souhaite connaitre l'auteur.

        id_collection: int
            identifiant de la collection sur laquelle se trouve l'avis.

        Returns:
        --------
        username: str
            nom d'utilisateur de l'auteur de l'avis
        """
        username = DaoAvis().trouver_auteur_avis_sur_col_phy(
            schema="projet_info_2a",
            id_avis_collection_physique=id_avis_collection_physique,
            id_collection=id_collection,
        )
        return username

    @log
    def Validation_avis(self, message_avis: str):
        """Permet de valider si le mesage laisser par l'utilisateur n'est pas
        insultant

        Prameters:
        ----------
        message_avis: str
            texte de l'avis que l'on souhaite valider.

        Returns:
        --------
        is_avis_valide: Bool
            Renvoie True si le message est valide et False sinon.
        """
        is_avis_valide = True

        Liste_mot_invalide = [
            "TA GUEULE",
            "CHIER",
            "TOCARD",
            "MERDIQUE",
            "SALOPE",
            "MERDE",
            "CON",
            "CONNARD",
            "CONNASSE",
            "PUTAIN",
            "PUTE",
        ]
        message_avis = str(message_avis)
        message_dans_avis = message_avis.split()

        for message in message_dans_avis:
            for mot_vulgaire in Liste_mot_invalide:
                if message.upper() == mot_vulgaire:
                    is_avis_valide = False

        return is_avis_valide
