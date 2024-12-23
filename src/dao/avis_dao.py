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
        """
        Trouver l'identifiant d'un avis grâce aux id manga et utilisateur.

        Parameters:
        -----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_manga: int
            identifiant du manga sur lequel se trouve l'avis dont on souhaite
            trouver l'identifiant.

        id_utilisateur: int
            identifiant de l'utilisateur ayant écrit l'avis dont on souhaite
            trouver l'identifiant.

        Returns:
        --------
        id_avis: int
            identifiant de l'avis souhaité.
        """

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
    def trouver_id_avis_par_id_manga_utilisateur_col_physique(
        self, schema: str, id_collection: int, id_utilisateur: int
    ) -> int:
        """
        Trouver l'identifiant d'un avis sur une collection physique
        grâce à l'identifiant de la collection et de utilisateur.

        Parameters:
        -----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_collection: int
            identifiant de la collection physique sur laquelle se trouve
            l'avis dont on souhaite trouver l'identifiant.

        id_utilisateur: int
            identifiant de l'utilisateur ayant écrit l'avis dont on souhaite
            trouver l'identifiant.

        Returns:
        --------
        id_avis: int
            identifiant de l'avis souhaité.
        """

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_avis_collection_physique FROM "
                        "avis_collection_physique_db WHERE "
                        "id_collection = %(id_collection)s "
                        "AND id_utilisateur = %(id_utilisateur)s;",
                        {
                            "id_collection": id_collection,
                            "id_utilisateur": id_utilisateur,
                        },
                    )
                    res = cursor.fetchone()

        except Exception as e:
            logging.error(f"Erreur lors de la recherche de l'avis : {e}")
            raise e

        if res:
            return res["id_avis_collection_physique"]

        return None

    @log
    def trouver_id_avis_par_id_col_coherente_utilisateur(
        self, schema: str, id_collection_coherente: int, id_utilisateur: int
    ) -> int:
        """
        Trouver l'identifiant d'un avis sur une collection cohérente
        grâce à l'identifiant de la collection et de utilisateur.

        Parameters:
        -----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_collection: int
            identifiant de la collection cohérente sur laquelle se trouve
            l'avis dont on souhaite trouver l'identifiant.

        id_utilisateur: int
            identifiant de l'utilisateur ayant écrit l'avis dont on souhaite
            trouver l'identifiant.

        Returns:
        --------
        id_avis: int
            identifiant de l'avis souhaité.
        """

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_avis_collection_coherente "
                        "FROM avis_collection_coherente_db "
                        "WHERE id_collection_coherente = "
                        "%(id_collection_coherente)s "
                        "AND id_utilisateur = %(id_utilisateur)s;",
                        {
                            "id_collection_coherente": id_collection_coherente,
                            "id_utilisateur": id_utilisateur,
                        },
                    )
                    res = cursor.fetchone()

        except Exception as e:
            logging.error(f"Erreur lors de la recherche de l'avis : {e}")
            raise e

        if res:
            return res["id_avis_collection_coherente"]

        return None

    @log
    def creer_avis(self, id_utilisateur: int, id_manga: int, avis: Avis, schema) -> bool:
        """Création d'un avis sur un manga dans la base de donnée.

        Parameters:
        -----------
        id_utilisateur: int
            Identifiant de l'utilisateur qui souhaite créer un avis.

        id_manga: int
            Identifiant du manga sur lequel l'utilisateur souhaite laisser un
            avis.

        avis: Avis
            Objet contenant le texte de l'avis et la note.

        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

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
                    id_avis = cursor.fetchone()

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
            un avis.

        id_collection_coherente: int
            identifiant de la collection sur laquelle l'utilisateur souhaite
            laisser un avis.

        avis_collection_coherente: Avis
            Objet contenant le texte et la note de l'avis.

        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

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
                    id_avis = cursor.fetchone()

                    if id_avis:
                        avis_collection_coherente.id_avis = id_avis["id_avis_collection_coherente"]
                        return True

        except Exception as e:
            logging.error(f"Erreur lors de la création de l'avis: {e}")

        return False

    @log
    def creer_avis_collection_physique(
        self, id_collection, id_utilisateur, avis_collection_physique: Avis, schema
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
            laisser un avis.

        avis_collection_physique: Avis
            Objet contentant le texte et la note de l'avis.

        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

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
                        "id_utilisateur, id_collection, avis"
                        ",note) "
                        "VALUES "
                        "(%(id_utilisateur)s,%(id_collection)s,"
                        "%(avis)s, "
                        "%(note)s) "
                        "RETURNING id_avis_collection_physique; ",
                        {
                            "id_utilisateur": id_utilisateur,
                            "id_collection": id_collection,
                            "avis": avis_collection_physique.avis,
                            "note": avis_collection_physique.note,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.error(f"Erreur lors de la création de l'avis de collection physique : {e}")

        created = False
        if res:
            avis_collection_physique.id_avis = res["id_avis_collection_physique"]
            created = True

        return created

    @log
    def chercher_avis(self, schema, id_utilisateur, id_manga):
        """Chercher l'avis qu'un utilisateur a laissé sur un manga.

        Parameters:
        -----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_utilisateur: int
            identifiant de l'utilisateur dont on souhaite chercher les avis
            sur un manga

        id_manga: int
            identifiant du manga pour lequel on souhaite récolter les avis laissés
            par un utilisateur

        Return:
        -------
        Avis
            avis trouvés.
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
    def supprimer_avis(self, schema, id_avis) -> bool:
        """Supprime un avis de la base de données.

        Parameters:
        -----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_avis:
            identifiant de l'avis que l'on souhaite supprimé.

        Returns:
        --------
        bool
            True si l'avis a été supprimé, False sinon.
        """

        res = None

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM avis WHERE id_avis= %(id_avis)s;",
                        {"id_avis": id_avis},
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
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_manga: int
            identifiant du manga sur lequel ce trouve l'avis que l'on souhaite
            modifier.

        id_utilisateur: int
            identifiant de l'utilisateur qui souhaite modifier son avis.

        avis : Avis
            Avis modifié que l'on souhaite mettre à jour dans la base de données.

        Returns
        -------
        bool
            Retourne True si la mise à jour a été effectuée avec succès, sinon
            False.
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
    def modifier_avis_collection_co(
        self, schema, id_collection, id_utilisateur, avis: Avis
    ) -> bool:
        """
        Modifie un avis d'une colletion cohérente dans la base de données.

        Parameters
        ----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_collection: int
            identifiant de la collection cohérente sur laquelle se trouve
            l'avis que l'on souhaite modifier.

        id_utilisateur: int
            identifiant de l'utilisateur qui souhaite modifier son avis.

        avis : Avis
            Avis modifié que l'on souhaite mettre à jour dans la base de
            données.

        Returns
        -------
        bool
            Retourne True si la mise à jour a été effectuée avec succès,
            sinon False.
        """
        id_avis_collection_coherente = self.trouver_id_avis_par_id_col_coherente_utilisateur(
            schema=schema, id_collection_coherente=id_collection, id_utilisateur=id_utilisateur
        )
        res = None

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE avis_collection_coherente_db
                        SET avis = %(avis)s, note = %(note)s
                        WHERE id_avis_collection_coherente = %(id_avis_collection_coherente)s;
                        """,
                        {
                            "avis": avis.avis,
                            "note": avis.note,
                            "id_avis_collection_coherente": id_avis_collection_coherente,
                        },
                    )
                    res = cursor.rowcount

        except Exception as e:
            logging.error(f"Erreur lors de la modification de l'avis : {e}")
            raise

        return res == 1

    @log
    def modifier_avis_collection_phy(
        self, schema, id_collection, id_utilisateur, avis: Avis
    ) -> bool:
        """
        Modifie un avis d'une colletion cohérente dans la base de données.

        Parameters
        ----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_collection: int
            identifiant de la collection physique sur laquelle se trouve
            l'avis que l'on souhaite modifier.

        id_utilisateur: int
            identifiant de l'utilisateur qui souhaite modifier son avis.

        avis : Avis
            Avis modifié que l'on souhaite mettre à jour dans la base de données.

        Returns
        -------
        bool
            Retourne True si la mise à jour a été effectuée avec succès, sinon False.
        """
        id_avis_collection_physique = self.trouver_id_avis_par_id_manga_utilisateur_col_physique(
            schema=schema, id_collection=id_collection, id_utilisateur=id_utilisateur
        )
        res = None

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE avis_collection_physique_db
                        SET avis = %(avis)s, note = %(note)s
                        WHERE id_avis_collection_physique = %(id_avis_collection_physique)s;
                        """,
                        {
                            "avis": avis.avis,
                            "note": avis.note,
                            "id_avis_collection_physique": id_avis_collection_physique,
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
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

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

        liste_avis = (
            [Avis(id_avis=row["id_avis"], avis=row["avis"], note=row["note"]) for row in res]
            if res
            else []
        )

        return liste_avis

    @log
    def chercher_avis_sur_collection_coherente(self, schema, id_collection_coherente):
        """Chercher l'ensemble des avis des utilisateurs laissés sur une
        collection cohérente.

        Parameters
        ----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_collection_coherente: int
            Identifiant de la collection coherente pour laquelle
            on souhaite récolter les avis.

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
                        SELECT id_avis_collection_coherente, avis, note
                        FROM avis_collection_coherente_db
                        WHERE id_collection_coherente =
                        %(id_collection_coherente)s;
                        """,
                        {"id_collection_coherente": id_collection_coherente},
                    )
                    res = cursor.fetchall()

        except Exception as e:
            logging.error(f"Erreur sur collection {id_collection_coherente} : {e}")
            raise

        liste_avis = (
            [
                Avis(
                    id_avis=row["id_avis_collection_coherente"], avis=row["avis"], note=row["note"]
                )
                for row in res
            ]
            if res
            else []
        )

        return liste_avis

    @log
    def chercher_avis_sur_collection_physique(self, schema, id_collection):
        """Chercher l'ensemble des avis des utilisateurs laissés sur une
        collection cohérente.

        Parameters
        ----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_collection: int
            Identifiant de la collection pour laquelle on souhaite récolter
            les avis.

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
                        SELECT id_avis_collection_physique, avis, note
                        FROM avis_collection_physique_db
                        WHERE id_collection = %(id_collection)s;
                        """,
                        {"id_collection": id_collection},
                    )
                    res = cursor.fetchall()

        except Exception as e:
            logging.error(
                f"Erreur lors de la recherche d'avis sur la collection {id_collection} : {e}"
            )
            raise

        liste_avis = (
            [
                Avis(id_avis=row["id_avis_collection_physique"], avis=row["avis"], note=row["note"])
                for row in res
            ]
            if res
            else []
        )

        return liste_avis

    @log
    def chercher_avis_user_sur_collection_coherente(
        self, schema, id_utilisateur, id_collection_coherente
    ):
        """Chercher l'avis d'un utilisateur laissés sur une
        collection cohérente.

        Parameters
        ----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_utilisateur: int
            id de l'utilisateur dont on veut afficher l'avis.

        id_collection_coherente: int
            Identifiant de la collection pour laquel on souhaite récolter
            l'avis de l'utilisateur.

        Returns
        -------
        Liste[Avis]
            liste contenant l'avis trouvés.
        """
        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT id_avis_collection_coherente, avis, note
                        FROM avis_collection_coherente_db
                        WHERE id_collection_coherente =
                        %(id_collection_coherente)s
                        AND id_utilisateur = %(id_utilisateur)s;
                        """,
                        {
                            "id_collection_coherente": id_collection_coherente,
                            "id_utilisateur": id_utilisateur,
                        },
                    )
                    res = cursor.fetchall()

        except Exception as e:
            logging.error(f"Erreur  {id_utilisateur} col {id_collection_coherente} : {e}")
            raise

        liste_avis = (
            [
                Avis(
                    id_avis=row["id_avis_collection_coherente"], avis=row["avis"], note=row["note"]
                )
                for row in res
            ]
            if res
            else []
        )

        return liste_avis

    @log
    def chercher_avis_user_sur_collection_physique(self, schema, id_utilisateur, id_collection):
        """Chercher l'avis d'un utilisateur laissés sur une
        collection physique.

        Parameters
        ----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_utilisateur: str
            id de l'utilisateur dont ont souhaite trouver l'avis

        id_collection: int
            Identifiant de la collection physique pour laquelle on souhaite
            récolter l'avis de l'utilisateur.

        Returns
        -------
        Liste[Avis]
            liste contenant l'avis trouvé.
        """
        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT id_avis_collection_physique, avis, note
                        FROM avis_collection_physique_db
                        WHERE id_collection = %(id_collection)s
                        AND id_utilisateur = %(id_utilisateur)s;
                        """,
                        {"id_collection": id_collection, "id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchall()

        except Exception as e:
            logging.error(
                f"Erreur lors de la recherche d'avis sur la collection {id_collection} : {e}"
            )
            raise

        liste_avis = (
            [
                Avis(id_avis=row["id_avis_collection_physique"], avis=row["avis"], note=row["note"])
                for row in res
            ]
            if res
            else []
        )

        return liste_avis

    @log
    def supprimer_avis_col_coherente(self, id_avis_collection_coherente, schema):
        """Supprime un avis de la base de données

        Parameters:
        -----------

        id_avis_collection_coherente: int
            identifiant de l'avis que l'on souhaite supprimer de la base de
            données

        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        Returns:
        --------
        Bool:
            Return True si la suppression à bien été effectué.

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

    @log
    def supprimer_avis_col_physique(self, id_avis_collection_physique, schema):
        """Supprime un avis de la base de données

        Parameters:
        -----------

        id_avis_collection_physique: int
            identifiant de l'avis que l'on souhaite supprimer de la base de
            données

        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        Returns:
        --------
        Bool:
            Return True si la suppression à bien été effectué.

        """

        res = None

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM avis_collection_physique_db "
                        "WHERE id_avis_collection_physique= "
                        "%(id_avis_collection_physique)s;",
                        {"id_avis_collection_physique": id_avis_collection_physique},
                    )
                    res = cursor.rowcount

        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    def trouver_auteur_avis_sur_manga(self, schema, id_avis, id_manga):
        """
        Permet de trouver le nom d'utilisateur de celui qui à écrit l'avis

        Parameters:
        -----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_avis: int
            identifiant de l'avis dont on souhaite connaitre l'auteur.

        id_manga: int
            identifiant du manga sur lequel se trouve l'avis.

        Returns:
        --------
        username: str
            nom d'utilisateur de l'auteur de l'avis
        """

        username = None

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT nom_utilisateur FROM utilisateur "
                        "JOIN avis USING(id_utilisateur)"
                        "WHERE id_avis= %(id_avis)s"
                        " AND id_manga= %(id_manga)s",
                        {"id_avis": id_avis, "id_manga": id_manga},
                    )
                    username = cursor.fetchone()

        except Exception as e:
            logging.info(e)
            raise

        return username["nom_utilisateur"]

    def trouver_auteur_avis_sur_col_co(
        self, schema, id_avis_collection_coherente, id_collection_coherente
    ):
        """
        Permet de trouver le nom d'utilisateur de celui qui à écrit l'avis

        Parameters:
        -----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_avis_collection_coherente: int
            identifiant de l'avis dont on souhaite connaitre l'auteur.

        id_collection_coherente: int
            identifiant de la collection sur laquelle se trouve l'avis.

        Returns:
        --------
        username: str
            nom d'utilisateur de l'auteur de l'avis
        """
        username = None

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT nom_utilisateur FROM utilisateur "
                        "JOIN avis_collection_coherente_db USING(id_utilisateur)"
                        "WHERE id_avis_collection_coherente= %(id_avis_collection_coherente)s"
                        " AND id_collection_coherente= %(id_collection_coherente)s",
                        {
                            "id_avis_collection_coherente": id_avis_collection_coherente,
                            "id_collection_coherente": id_collection_coherente,
                        },
                    )
                    username = cursor.fetchone()

        except Exception as e:
            logging.info(e)
            raise

        return username["nom_utilisateur"]

    def trouver_auteur_avis_sur_col_phy(self, schema, id_avis_collection_physique, id_collection):
        """
        Permet de trouver le nom d'utilisateur de celui qui à écrit l'avis

        Parameters:
        -----------
        schema: str
            nom du schema que l'on souhaite modifier, schema= "projet_test_dao"
            pour modifier la base de données prévue pour les test, et
            schema= "projet_info_2a" pour modifier la base de données de
            l'application.

        id_avis_collection_physique: int
            identifiant de l'avis dont on souhaite connaitre l'auteur.

        id_collection: int
            identifiant de la collection sur laquelle se trouve l'avis.

        Returns:
        --------
        username: str
            nom d'utilisateur de l'auteur de l'avis
        """

        username = None

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT nom_utilisateur FROM utilisateur "
                        "JOIN avis_collection_physique_db USING(id_utilisateur)"
                        "WHERE id_avis_collection_physique= %(id_avis_collection_physique)s"
                        " AND id_collection= %(id_collection)s",
                        {
                            "id_avis_collection_physique": id_avis_collection_physique,
                            "id_collection": id_collection,
                        },
                    )
                    username = cursor.fetchone()

        except Exception as e:
            logging.info(e)
            raise

        return username["nom_utilisateur"]
