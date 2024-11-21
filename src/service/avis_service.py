from utils.log_decorator import log

from business_object.avis import Avis
from dao.avis_dao import DaoAvis


class ServiceAvis:
    """Classe contenant les méthodes de services des Avis"""

    @log
    def ajouter_avis(self, id_utilisateur, id_manga, avis, note):
        """Création d'un avis à partir de ses attributs"""

        nouveau_avis = Avis(note, avis)
        return (
            nouveau_avis
            if DaoAvis().creer_avis(id_utilisateur, id_manga, nouveau_avis, "projet_info_2a")
            else None
        )

    @log
    def ajouter_avis_collection(self, id_utilisateur, id_collection, type_collection, avis, note):
        """Création d'un avis sur une collection à partir de ses attributs"""

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
        """Afficher l'avis qu'un utilisateur a laisser sur un  manga"""

        avis_user_sur_manga = DaoAvis().chercher_avis("projet_info_2a", id_utlisateur, id_manga)

        if len(avis_user_sur_manga) > 0:
            return avis_user_sur_manga[0]
        else:
            return None

    @log
    def afficher_avis_collection_coherente(self, id_collection):
        """Afficher les avis laisser sur une collection cohérente"""

        avis_user_sur_col_co = DaoAvis().chercher_avis_sur_collection_coherente(
            "projet_info_2a", id_collection
        )

        if len(avis_user_sur_col_co) > 0:
            return avis_user_sur_col_co
        else:
            return None

    @log
    def afficher_avis_collection_physique(self, id_collection):
        """Afficher les avis laisser sur une collection cohérente"""

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
        """Modification d'un avis"""
        avis = Avis(note, avis_message)

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
        """Modification d'un avis d'une collection coherente"""
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
        """Modification d'un avis d'une collection physique"""
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
        """Supprimer un avis"""
        return DaoAvis().supprimer_avis("projet_info_2a", id_avis)

    @log
    def afficher_autre_avis(self, id_manga):
        """Afficher les avis laisser sous  un manga"""

        avis_user_sur_manga = DaoAvis().chercher_avis_sur_manga("projet_test_dao", id_manga)

        if len(avis_user_sur_manga) > 0:
            return avis_user_sur_manga
        else:
            return None
