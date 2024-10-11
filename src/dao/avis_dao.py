import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.manga import Manga
from business_object.avis import Avis
from business_object.collection_cohérente import CollectionCohérente

class DaoAvis:
    """
    Classe contenant les méthodes qui communique avec la base de données afin
    de gérer les avis
    """

    def __init__(self, id_utilisateur, id_manga)
