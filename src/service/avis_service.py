# from tabulate import tabulate

from utils.log_decorator import log

from business_object.avis import Avis
from dao.avis_dao import DaoAvis


class ServiceAvis:
    """Classe contenant les méthodes de services des Avis"""

    @log
    def ajouter_avis(self, id_utilisateur, id_manga, avis, note):
        """Création d'un avis à partir de ses attributs"""

        nouveau_avis = Avis(avis, note)
        return nouveau_avis if DaoAvis().creer(id_utilisateur, id_manga, nouveau_avis) else None
