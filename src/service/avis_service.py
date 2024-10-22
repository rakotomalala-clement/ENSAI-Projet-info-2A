from tabulate import tabulate

from utils.log_decorator import log

from business_object.avis import Avis
from dao.avis_dao import DaoAvis


class ServiceAvis:
    """Classe contenant les méthodes de services des Avis"""

    @log
    def ajouter_avis(self, id_utilisateur, id_manga, avis, note):
        """Création d'un avis à partir de ses attributs"""

        nouveau_avis = Avis(avis, note)
        return (
            nouveau_avis if DaoAvis().creer_avis(id_utilisateur, id_manga, nouveau_avis) else None
        )

    @log
    def ajouter_avis_collection(self, id_utilisateur, id_collection, type_collection, avis, note):
        """Création d'un avis sur une collection à partir de ses attributs"""

        nouveau_avis_collection = Avis(avis, note)

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
        """Afficher les avis qu'un utilisateur a laisser sur un  manga"""

        entetes = ["note", "avis"]  # ajouter nom du mangas correspondant ?

        avis_user_sur_manga = DaoAvis.chercher_avis(id_utlisateur, id_manga)

        avis_as_list = [a.as_list() for a in avis_user_sur_manga]

        str_avis = "-" * 100
        str_avis += "\nListe des joueurs \n"
        str_avis += "-" * 100
        str_avis += "\n"
        str_avis += tabulate(
            tabular_data=avis_as_list,
            headers=entetes,
            tablefmt="psql",
            floatfmt=".2f",
        )
        str_avis += "\n"

        return str_avis

    @log
    def modifier(self, avis) -> Avis:
        """Modification d'un avis"""

        return avis if DaoAvis().modifier_avis(avis) else None

    @log
    def supprimer(self, id_avis) -> bool:
        """Supprimer un avis"""
        return DaoAvis().supprimer_avis(id_avis)

    @log
    def afficher_autre_avis(self, id_manga):
        """Afficher les avis laisser sous  les mangas"""

        """Afficher les avis qu'un utilisateur a laisser sur un  manga"""

        entetes = ["note", "avis"]  # ajouter nom du mangas correspondant ?

        avis_user_sur_manga = DaoAvis.chercher_avis_sur_manga(id_manga)

        avis_as_list = [a.as_list() for a in avis_user_sur_manga]

        str_avis = "-" * 100
        str_avis += "\nListe des joueurs \n"
        str_avis += "-" * 100
        str_avis += "\n"
        str_avis += tabulate(
            tabular_data=avis_as_list,
            headers=entetes,
            tablefmt="psql",
            floatfmt=".2f",
        )
        str_avis += "\n"

        return str_avis


resultat = ServiceAvis().ajouter_avis(id_utilisateur=1, id_manga=1, avis="cool", note=5)

if resultat:
    print("Avis ajouté avec succès :", resultat)
else:
    print("Échec de l'ajout de l'avis.")
