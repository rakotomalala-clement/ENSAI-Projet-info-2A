import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.manga import Manga


class MangaDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Manga de la base de données"""

    @log
    def trouver_par_titre(self, titre) -> Manga:
        """trouver un manga grace à son titre

        Parameters
        ----------
        titre : str
            titre du manga que l'on souhaite trouver

        Returns
        -------
        manga : Manga
            renvoie le manga que l'on cherche par son titre
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM manga                      "
                        " WHERE titre = %(titre)s;  ",
                        {"titre": titre},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        manga = None
        if res:
            manga = Manga(
                id_manga=res["id_manga"],
                titre=res["titre"],
                id_jikan=res["id_jikan"],
            )

        return manga

    @log
    def lister_manga(self) -> list[Manga]:
        """lister tous les mangas

        Parameters
        ----------
        None

        Returns
        -------
        liste_mangas : list[Manga]
            renvoie la liste de tous les mangas dans la base de données
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                              "
                        "  FROM manga;                        "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_mangas = []

        if res:
            for row in res:
                manga = Manga(
                    id_manga=row["id_manga"],
                    titre=row["titre"],
                    id_jikan=row["id_jikan"],
                )

                liste_mangas.append(manga)

        return liste_mangas

    @log
    def supprimer_manga(self, manga) -> bool:
        """Suppression d'un manga dans la base de données

        Parameters
        ----------
        manga : Manga
            manga à supprimer de la base de données

        Returns
        -------
            True si le manga a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM manga                  " " WHERE id_manga=%(id_manga)s      ",
                        {"id_manga": manga.id_manga},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    @log
    def Ajouter_manga(self, manga) -> bool:
        """Ajout d'un manga dans la base de données

        Parameters
        ----------
        manga : Manga
            manga à ajouter de la base de données

        Returns
        -------
            True si le manga a bien été ajouté
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE FROM manga                  " " WHERE id_manga=%(id_manga)s      ",
                        {"id_manga": manga.id_manga},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0
