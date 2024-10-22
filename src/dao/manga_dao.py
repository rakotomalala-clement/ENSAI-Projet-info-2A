import logging
from utils.log_decorator import log
from dao.db_connection import DBConnection
from business_object.manga import Manga
from utils.singleton import Singleton


class MangaDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Manga de la base de données"""

    @log
    def trouver_par_titre(self, titre: str) -> Manga:
        """Trouver un manga grâce à son titre."""
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM manga WHERE titre = %(titre)s;",
                        {"titre": titre},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.error(e)
            raise

        if res:
            return Manga(
                id_manga=res["id_manga"],
                titre=res["titre"],
                auteurs=res["auteurs"],
                genres=res["genres"],
                status=res["status_manga"],
                nombre_chapitres=res["chapitres"],
            )

        return None

    @log
    def lister_manga(self) -> list[Manga]:
        """Lister tous les mangas."""
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM manga;")
                    res = cursor.fetchall()
        except Exception as e:
            logging.error(e)
            raise

        return [
            Manga(
                id_manga=row["id_manga"],
                titre=row["titre"],
                auteurs=row["auteurs"],
                genres=row["genres"],
                status=row["status_manga"],
                nombre_chapitres=row["chapitres"],
            )
            for row in res
        ]

    @log
    def supprimer_manga(self, manga: Manga) -> bool:
        """Suppression d'un manga dans la base de données."""
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM manga WHERE id_manga=%(id_manga)s;",
                        {"id_manga": manga.id_manga},
                    )
                    return cursor.rowcount > 0
        except Exception as e:
            logging.error(e)
            raise

    @log
    def ajouter_manga(self, manga: Manga) -> bool:
        """Ajout d'un manga dans la base de données."""
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO manga (titre, auteurs, genres, status_manga, nombre_chapitres)"
                        "VALUES (%(titre)s, %(auteurs)s, %(genres)s, %(status_manga)s,\
                            %(nombre_chapitres)s);",
                        {
                            "titre": manga.titre,
                            "auteurs": manga.auteurs,
                            "genres": manga.genres,
                            "status_manga": manga.status,
                            "nombre_chapitres": manga.nombre_chapitres,
                        },
                    )
                    return cursor.rowcount > 0
        except Exception as e:
            logging.error(e)
            raise
