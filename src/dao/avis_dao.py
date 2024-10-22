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

    @log
    def creer_avis(self, id_utilisateur, id_manga, avis_manga: Avis):
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
                        "avis(id_utilisateur, id_manga, avis, note) "
                        "VALUES "
                        "(%(id_utilisateur)s,%(id_manga)s,%(avis)s, "
                        "%(note)s) "
                        "RETURNING id_avis; ",
                        {
                            "id_utilisateur": id_utilisateur,
                            "id_manga": id_manga,
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
        self, id_utilisateur, id_collection, avis_collection_coherente: Avis
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
                        "(%(id_utilisateur)s,%(id_collection_coherente)s,"
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

    @log
    def creer_avis_collection_physique(
        self, id_utilisateur, id_collection, avis_collection_physique: Avis
    ):
        """Création d'un avis sur une collection physique dans la base
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
                        "avis_collection_physique("
                        "id_utilisateur, id_collection_physique, avis"
                        ",note) "
                        "VALUES "
                        "(%(id_utilisateur)s,%(id_collection_physique)s,"
                        "%(avis)s, "
                        "%(note)s) "
                        "RETURNING id_avis; ",
                        {
                            "id_utilisateur": id_utilisateur,
                            "id_collection_physique": id_collection,
                            "avis": avis_collection_physique.avis,
                            "note": avis_collection_physique.note,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            avis_collection_physique.id_avis = res["id_avis_ccollection_physique"]
            created = True

        return created

    @log
    def chercher_avis(self, id_utilisateur, id_manga):
        """Chercher les avis qu'un utilisateur a laisser sur un manga

        Parameters:
        -----------
        id_utilisateur: int
            identifiant de l'utilisateur dont ont souhaite chercher les avis
            sur un manga

        id_manga: int
            identifiant du manga pour lequel on souhaite récolter les avis laisser
            par un utilisateur

        Return:
        -------


        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_avis, avis.avis, note FROM avis "
                        "JOIN utilisateur USING(id_utilisateur) "
                        "WHERE id_jikan_manga = %(id_manga)s "
                        "AND id_utilisateur = %(id_utilisateur)s;",
                        {
                            "id_manga": id_manga,
                            "id_utilisateur": id_utilisateur,
                        },
                    )
                    res = cursor.fetchall()

        except Exception as e:
            logging.info(e)
            raise

        Liste_avis = []
        if res:
            for row in res:
                Liste_avis.append(
                    Avis(
                        id_avis=row["id_avis"],
                        avis=row["avis"],
                        note=row["note"],
                    )
                )

        return Liste_avis

    @log
    def supprimer_avis(self, id_avis):
        """Supprime un avis de la base de données

        Parameters:
        -----------

        id_avis: int
            identifiant de l'avis que l'on souhaite supprimer de la base de
            données

        Returns:
        --------

        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor as cursor:
                    cursor.execute(
                        "DELETE FROM avis" " WHERE id_avis= %(id_avis)s;",
                        {"id_avis": id_avis},
                    )
                    res = cursor.rowcount

        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    @log
    def modifier_avis(self, avis: Avis):
        """Modifie un avis dans la base de données

        Parameters:
        -----------

        avis: Avis
            avis modifié que  l'on souhaite modifier dans la base de données

        Return:
        -------

        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor as cursor:
                    cursor.execute(
                        "UPDATE avis "
                        "SET avis = %(avis)s, note = %(note)s"
                        " WHERE id_avis = %(id_avis)s;",
                        {
                            "avis": avis.avis,
                            "note": avis.note,
                            "id_avis": avis.id_avis,
                        },
                    )
                    res = cursor.rowcount

        except Exception as e:
            logging.info(e)
            raise

        return res == 1

    @log
    def chercher_avis_sur_manga(self, id_manga):
        """Chercher l'ensemble des avis des utilisateurs laisser sur un manga

        Parameters:
        -----------

        id_manga: int
            identifiant du manga pour lequel on souhaite récolter les avis

        Return:
        -------

        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_avis, avis.avis, note FROM avis "
                        "WHERE id_jikan_manga = %(id_manga)s;",
                        {
                            "id_manga": id_manga,
                        },
                    )
                    res = cursor.fetchall()

        except Exception as e:
            logging.info(e)
            raise

        Liste_avis = []
        if res:
            for row in res:
                Liste_avis.append(
                    Avis(
                        id_avis=row["id_avis"],
                        avis=row["avis"],
                        note=row["note"],
                    )
                )

        return Liste_avis
