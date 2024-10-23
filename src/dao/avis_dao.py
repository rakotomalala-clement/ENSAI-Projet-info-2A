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
    def trouver_id_avis_par_id_manga_utilisateur(
        self, schema: str, id_manga: int, id_utilisateur: int
    ) -> int:
        """Trouver l'identifiant d'un avis grâce aux id manga et utilisateur."""
        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_avis FROM avis WHERE id_manga = %(id_manga)s "
                        "AND id_utilisateur = %(id_utilisateur)s;",
                        {"id_manga": id_manga, "id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchone()

        except Exception as e:
            logging.error(f"Erreur lors de la recherche de l'avis : {e}")
            raise e

        if res:
            return res["id_avis"]

        return None

    @log
    def trouver_id_avis_par_id_manga_utilisateur(
        self, schema: str, id_manga: int, id_utilisateur: int
    ) -> int:
        """Trouver l'identifiant d'un avis grâce aux id manga et utilisateur."""
        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_avis FROM avis WHERE id_manga = %(id_manga)s "
                        "AND id_utilisateur = %(id_utilisateur)s;",
                        {"id_manga": id_manga, "id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchone()

        except Exception as e:
            logging.error(f"Erreur lors de la recherche de l'avis : {e}")
            raise e

        if res:
            return res["id_avis"]

        return None

    @log
    def creer_avis(self, id_utilisateur: int, id_manga: int, avis: Avis, schema) -> bool:
        """Création d'un avis sur un manga dans la base de donnée.

        Parameters:
        -----------
        id_utilisateur: int
            Identifiant de l'utilisateur qui souhaite créer un avis.

        id_manga: int
            Identifiant du manga sur lequel l'utilisateur souhaite laisser un avis.

        avis: Avis
            Objet contenant le texte de l'avis et la note.

        Returns:
        --------
        bool
            True si l'avis a été créé avec succès, False sinon.
        """

        try:
            with DBConnection(schema).connection as connection:
                print(id_utilisateur)
                print(id_manga)
                print(avis.avis)
                print(avis.note)
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO avis (id_utilisateur, id_manga, avis, note)
                        VALUES (%s, %s, %s, %s)
                        RETURNING id_avis;
                        """,
                        (id_utilisateur, id_manga, avis.avis, avis.note),
                    )
                    # Récupérer l'ID de l'avis inséré
                    id_avis = cursor.fetchone()

                    # Si un ID a été retourné, l'avis a été créé avec succès
                    if id_avis:
                        avis.id_avis = id_avis["id_avis"]
                        return True

        except Exception as e:
            logging.error(f"Erreur lors de la création de l'avis: {e}")

        return False

    @log
    def creer_avis_collection_coherente(
        self, id_utilisateur, id_collection_coherente, avis_collection_coherente: Avis, schema
    ) -> bool:
        """Création d'un avis sur une collection cohérente dans la base
        de données

        Parameters:
        -----------
        id_utilisateur: int
            identifiant de l'utilisateur pour lequel on souhaite créer
            un avis

        id_collection: int
            identifiant de la collection sur laquelle l'utilisateur souhaite
            laisser un avis

        Returns:
        --------
        bool
            True si l'avis a été créé avec succès, False sinon.
        """

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """INSERT INTO avis_collection_coherente_db(
                        id_utilisateur, id_collection_coherente, avis,note)
                        VALUES (%(id_utilisateur)s,%(id_collection_coherente)s,
                        %(avis)s, %(note)s)
                        RETURNING id_avis_collection_coherente;
                        """,
                        {
                            "id_utilisateur": id_utilisateur,
                            "id_collection_coherente": id_collection_coherente,
                            "avis": avis_collection_coherente.avis,
                            "note": avis_collection_coherente.note,
                        },
                    )
                    # Récupérer l'ID de l'avis inséré
                    id_avis = cursor.fetchone()

                    # Si un ID a été retourné, l'avis a été créé avec succès
                    if id_avis:
                        avis_collection_coherente.id_avis = id_avis["id_avis_collection_coherente"]
                        return True

        except Exception as e:
            logging.error(f"Erreur lors de la création de l'avis: {e}")

        return False

    @log
    def creer_avis_collection_physique(
        self, id_utilisateur, id_collection, avis_collection_physique: Avis, schema
    ):
        """Création d'un avis sur une collection physique dans la base
        de données

        Parameters:
        -----------
        id_utilisateur: int
            identifiant de l'utilisateur pour lequel on souhaite créer
            un avis

        id_collection: int
            identifiant de la collection sur laquelle l'utilisateur souhaite
            laisser un avis

        Returns:
        --------
        bool
            True si l'avis a été créé avec succès, False sinon.
        """

        res = None

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO "
                        "avis_collection_physique_db("
                        "id_utilisateur, id_collection_physique, avis"
                        ",note) "
                        "VALUES "
                        "(%(id_utilisateur)s,%(id_collection_physique)s,"
                        "%(avis)s, "
                        "%(note)s) "
                        "RETURNING id_avis_collection_physique; ",
                        {
                            "id_utilisateur": id_utilisateur,
                            "id_collection_physique": id_collection,
                            "avis": avis_collection_physique.avis,
                            "note": avis_collection_physique.note,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.error(f"Erreur lors de la création de l'avis de collection physique : {e}")

        created = False
        if res:
            avis_collection_physique.id_avis = res["id_avis"]
            created = True

        return created

    @log
    def chercher_avis(self, schema, id_utilisateur, id_manga):
        """Chercher les avis qu'un utilisateur a laissés sur un manga.

        Parameters:
        -----------
        id_utilisateur: int
            identifiant de l'utilisateur dont on souhaite chercher les avis
            sur un manga

        id_manga: int
            identifiant du manga pour lequel on souhaite récolter les avis laissés
            par un utilisateur

        Return:
        -------
        List[Avis]
            Liste des avis trouvés.
        """
        id_avis = self.trouver_id_avis_par_id_manga_utilisateur(schema, id_manga, id_utilisateur)
        res = None

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_avis, avis, note FROM avis " "WHERE id_avis = %(id_avis)s;",
                        {
                            "id_avis": id_avis,
                        },
                    )
                    res = cursor.fetchall()

        except Exception as e:
            logging.error(f"Erreur lors de la recherche d'avis : {e}")
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
    def supprimer_avis(self, schema, id_manga, id_utilisateur) -> bool:
        """Supprime un avis de la base de données.

        Parameters:
        -----------
        id_utilisateur: int
            Identifiant de l'utilisateur.

        id_manga: int
            Identifiant du manga dont l'avis sera supprimé.

        Returns:
        --------
        bool
            True si l'avis a été supprimé, False sinon.
        """

        res = None

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:  # Fix: Use 'with connection.cursor()'
                    cursor.execute(
                        "DELETE FROM avis WHERE id_avis= %(id_avis)s;",
                        {
                            "id_avis": self.trouver_id_avis_par_id_manga_utilisateur(
                                schema, id_manga, id_utilisateur
                            )
                        },
                    )
                    res = cursor.rowcount

        except Exception as e:
            logging.error(f"Erreur lors de la suppression de l'avis : {e}")
            raise

        return res > 0

    @log
    def modifier_avis(self, schema, id_manga, id_utilisateur, avis: Avis) -> bool:
        """
        Modifie un avis dans la base de données.

        Parameters
        ----------
        avis : Avis
            Avis modifié que l'on souhaite mettre à jour dans la base de données.

        Returns
        -------
        bool
            Retourne True si la mise à jour a été effectuée avec succès, sinon False.
        """
        id_avis = self.trouver_id_avis_par_id_manga_utilisateur(schema, id_manga, id_utilisateur)
        res = None

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE avis
                        SET avis = %(avis)s, note = %(note)s
                        WHERE id_avis = %(id_avis)s;
                        """,
                        {
                            "avis": avis.avis,
                            "note": avis.note,
                            "id_avis": id_avis,
                        },
                    )
                    res = cursor.rowcount

        except Exception as e:
            logging.error(f"Erreur lors de la modification de l'avis : {e}")
            raise

        return res == 1

    @log
    def chercher_avis_sur_manga(self, schema, id_manga):
        """Chercher l'ensemble des avis des utilisateurs laissés sur un manga.

        Parameters
        ----------
        schema: str
            Nom du schéma de la base de données.
        id_manga: int
            Identifiant du manga pour lequel on souhaite récolter les avis.

        Returns
        -------
        List[Avis]
            Liste des avis trouvés.
        """
        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT id_avis, avis, note
                        FROM avis
                        WHERE id_manga = %(id_manga)s;
                        """,
                        {"id_manga": id_manga},
                    )
                    res = cursor.fetchall()

        except Exception as e:
            logging.error(f"Erreur lors de la recherche d'avis sur le manga {id_manga} : {e}")
            raise

        # Transforme les résultats en une liste d'objets Avis
        liste_avis = (
            [Avis(id_avis=row["id_avis"], avis=row["avis"], note=row["note"]) for row in res]
            if res
            else []
        )

        return liste_avis

    @log
    def supprimer_avis_col_coherente(self, id_avis_collection_coherente, schema):
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
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM avis_collection_coherente_db\
                            WHERE id_avis_collection_coherente= %(id_avis_collection_coherente)s;",
                        {"id_avis_collection_coherente": id_avis_collection_coherente},
                    )
                    res = cursor.rowcount

        except Exception as e:
            logging.info(e)
            raise

        return res > 0
