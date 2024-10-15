import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection


from business_object.avis import Avis


class DaoAvis(metaclass=Singleton):
    """
    Classe contenant les méthodes qui communique avec la base de données afin
    de gérer les avis
    """

    def __init__(self, id_utilisateur, id_manga, avis_manga: Avis):

        @log
        def creer_avis(self, id_utilisateur, id_manga):
            """Création d'un avis sur un manga dans la base de donnée

            Parameters:
            -----------

            id_utilisateur: int
                identifiant de l'utilisateur pour lequel on souhaite créer
                un avis

            id_manga: int
            identifiant du manga sur lequel l'utilisateur souhaite laisser un
            avis

            Returns:
            --------

            """

            res = None

            try:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "INSERT INTO "
                            "avis(id_utilisateur, id_jikan_manga, avis, note) "
                            "VALUES "
                            "(%(id_utilisateur)s,%(id_jikan_manga)s,%(avis)s, "
                            "%(note)s) "
                            "RETURNING id_avis; ",
                            {
                                "id_utilisateur": id_utilisateur,
                                "id_jikan_manga": id_manga,
                                "avis": avis_manga.avis,
                                "note": avis_manga.note,
                            },
                        )
                        res = cursor.fetchone()
            except Exception as e:
                logging.info(e)

            created = False
            if res:
                avis_manga.id_avis = res["id_avis"]
                created = True

            return created

        @log
        def creer_avis_collection_coherente(
            self, id_utilisateur, id_collection, avis_collection_coherente: Avis = None
        ):
            """Création d'un avis sur une collection cohérente dans la base
            de données

            Parameters:
            -----------

            id_utilisateur: int
                identifiant de l'utilisateur pour lequel on souhaite créer
                un avis

            id_collection: int
            identifiant de la collection sur lequel l'utilisateur souhaite
            laisser un avis

            Returns:
            --------

            """

            res = None

            try:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "INSERT INTO "
                            "avis_collection_coherente("
                            "id_utilisateur, id_collection_coherente, avis"
                            ",note) "
                            "VALUES "
                            "(%(id_utilisateur)s,%(id_jikan_manga)s,"
                            "%(avis)s, "
                            "%(note)s) "
                            "RETURNING id_avis; ",
                            {
                                "id_utilisateur": id_utilisateur,
                                "id_collection_coherente": id_collection,
                                "avis": avis_collection_coherente.avis,
                                "note": avis_collection_coherente.note,
                            },
                        )
                        res = cursor.fetchone()
            except Exception as e:
                logging.info(e)

            created = False
            if res:
                avis_collection_coherente.id_avis = res["id_avis_collection_coherente"]
                created = True

            return created
