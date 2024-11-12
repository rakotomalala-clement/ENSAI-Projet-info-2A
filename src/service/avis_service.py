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

        if "c" in type_collection:
            return (
                nouveau_avis_collection
                if DaoAvis().creer_avis_collection_coherente(
                    id_utilisateur, id_collection, nouveau_avis_collection
                )
                else None
            )
        elif "p" in type_collection:
            return (
                nouveau_avis_collection
                if DaoAvis().creer_avis_collection_physique(
                    id_utilisateur, id_collection, nouveau_avis_collection
                )
                else None
            )
        else:
            raise Exception("type_collection incorrect")

    @log
    def afficher_avis_user(id_utlisateur, id_manga):
        """Afficher l'avis qu'un utilisateur a laisser sur un  manga"""

        avis_user_sur_manga = DaoAvis.chercher_avis(id_utlisateur, id_manga)

        return avis_user_sur_manga[0]


    @log
    def modifier(self, avis_message, note) -> Avis:
        """Modification d'un avis"""
        avis = Avis(note, avis_message)

        return avis if DaoAvis().modifier_avis(avis) else None

    @log
    def supprimer(self, id_avis) -> bool:
        """Supprimer un avis"""
        return DaoAvis().supprimer_avis(id_avis)

    @log
    def afficher_autre_avis(self, id_manga):
        """Afficher les avis laisser sous  un manga"""

        avis_user_sur_manga = DaoAvis().chercher_avis_sur_manga("projet_info_2a", id_manga)

        return avis_user_sur_manga
