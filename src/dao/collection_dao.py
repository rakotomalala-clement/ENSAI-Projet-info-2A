import logging
from typing import List
from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

import psycopg2.extras
from business_object.collection.collection_physique import CollectionPhysique
from business_object.collection.collection_coherente import CollectionCoherente
from business_object.manga import Manga
from business_object.collection.mangas_dans_collection import MangaDansCollection
from dao.manga_dao import MangaDao


class DaoCollection(metaclass=Singleton):

    @log
    def creer(self, id_utilisateur, collection, schema) -> bool:
        res = None
        created = False

        if collection.type_collection == "Physique":

            query = """
                INSERT INTO collection_physique (id_utilisateur)
                VALUES (%(id_utilisateur)s)
                RETURNING id_collection;
            """
            params = {
                "id_utilisateur": id_utilisateur,
            }

        elif collection.type_collection == "Coherente":

            query = """
                INSERT INTO collection_coherente (id_utilisateur, titre_collection, description_collection)
                VALUES (%(id_utilisateur)s, %(titre_collection)s, %(description_collection)s)
                RETURNING id_collection;
            """
            params = {
                "id_utilisateur": id_utilisateur,
                "titre_collection": collection.titre,
                "description_collection": collection.description,
            }
        else:
            logging.error("Type de collection inconnu.")
            return False

        try:
            with DBConnection(schema).connection as connection:

                with connection.cursor() as cursor:

                    cursor.execute(query, params)

                    res = cursor.fetchone()

                    if res:
                        # Utilisation éventuelle de l'id_collection
                        collection.id_collection = res["id_collection"]
                        created = True

        except Exception as e:
            logging.info(f"Erreur lors de la création de la collection : {e}")

        return created

    @log
    def lister_collections_coherentes(
        self, id_utilisateur: int, schema
    ) -> List[CollectionCoherente]:
        """Recherche les collections cohérentes créées par l'utilisateur identifié par son id."""
        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT id_collection, id_utilisateur, titre_collection, description_collection
                        FROM collection_coherente
                        WHERE id_utilisateur = %s;
                        """,
                        (id_utilisateur,),
                    )

                    results = cursor.fetchall()
                    collections = [
                        CollectionCoherente(
                            id_collection=result["id_collection"],
                            titre=result["titre_collection"],
                            description=result["description_collection"],
                        )
                        for result in results
                    ]

                return collections
        except Exception as e:
            logging.error(
                f"Erreur lors de la recherche de la collection avec id user {id_utilisateur}: {e}"
            )

    @log
    def lister_mangas_collection(self, id_collection, schema: str):
        """Récupération des mangas associés à une collection cohérente"""
        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:

                    cursor.execute(
                        """
                        SELECT id_manga FROM collection_coherente_mangas
                        WHERE id_collection = %s;
                        """,
                        (id_collection,),
                    )

                    result = cursor.fetchall()

                    mangas = []
                    if result:
                        for row in result:
                            id_manga = row["id_manga"]

                            cursor.execute(
                                """
                                SELECT * FROM manga
                                WHERE id_manga = %s;
                                """,
                                (id_manga,),
                            )
                            manga_details = cursor.fetchone()

                            # Si des détails sont trouvés, créer un objet Manga et l'ajouter à la liste
                            if manga_details:
                                manga = Manga(
                                    id_manga=manga_details["id_manga"],
                                    titre=manga_details["titre"],
                                    auteurs=manga_details["auteurs"],
                                    genres=manga_details["genres"],
                                    status=manga_details["status_manga"],
                                    nombre_chapitres=manga_details["chapitres"],
                                )
                                mangas.append(manga)

                    connection.commit()
                    return mangas

        except Exception as e:
            logging.info(f"Erreur : {e}")
            return []

    @log
    def rechercher_collection_physique(
        self, id_utilisateur: int, schema
    ) -> List[MangaDansCollection]:
        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                    cursor.execute(
                        """
                        SELECT cpm.id_manga, cpm.titre_manga, cpm.numero_dernier_tome, cpm.numeros_tomes_manquants,cpm.status_manga
                        FROM collection_physique cp
                        JOIN collection_physique_mangas cpm ON cp.id_collection = cpm.id_collection
                        WHERE cp.id_utilisateur = %s;

                        """,
                        (id_utilisateur,),
                    )

                    results = cursor.fetchall()

                if not results:
                    return "Aucun manga ajouté"

                collection = [
                    MangaDansCollection(
                        manga=result[0],
                        collection=result[1],
                        dernier_tome_acquis=result[1],
                        numeros_tomes_manquants=result[2],
                        status_manga=result[3],
                    )
                    for result in results
                ]
                return collection
        except Exception as e:
            logging.error(
                f"Erreur lors de la recherche de la collection avec id user {id_utilisateur}: {e}"
            )
            raise e

    @log
    def ajouter_mangas_collection_coherente(self, collection_id, liste_mangas, schema) -> bool:
        """Ajoute une liste de mangas à une collection cohérente dans la base de données."""

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:

                    cursor.execute(
                        """
                        SELECT id_manga
                        FROM collection_coherente_mangas
                        WHERE id_collection = %s;
                        """,
                        (collection_id,),
                    )
                    existing_mangas = {row["id_manga"] for row in cursor.fetchall()}

                    mangas_a_ajouter = [
                        manga_id for manga_id in liste_mangas if manga_id not in existing_mangas
                    ]

                    if mangas_a_ajouter:

                        insert_query = """
                            INSERT INTO collection_coherente_mangas (id_collection, id_manga)
                            VALUES (%s, %s);
                        """
                        for manga_id in mangas_a_ajouter:
                            cursor.execute(insert_query, (collection_id, manga_id))

                connection.commit()
                return True

        except Exception as e:
            logging.error(f"Erreur lors de l'ajout des mangas à la collection : {e}")
            return False

    # méthode  utilisée dans la méthode : ajouter_manga_collection_physique
    def obtenir_id_collection_par_utilisateur(id_utilisateur, schema):
        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT id_collection
                        FROM collection_physique
                        WHERE id_utilisateur = %s;
                        """,
                        (id_utilisateur,),
                    )
                    result = cursor.fetchone()
                    print("******************")
                    print(result)
                    return result["id_collection"] if result else None
        except Exception as e:
            logging.error(f"Erreur lors de la récupération de l'ID de collection : {e}")
            return None

    @log
    def ajouter_manga_collection_physique(
        self,
        id_utilisateur,
        titre_manga,
        numero_dernier_tome,
        numeros_tomes_manquants,
        status_manga,
        schema,
    ) -> bool:

        try:
            # Étape 1: Récupérer l'id_collection correspondant à l'id_utilisateur
            id_collection = DaoCollection.obtenir_id_collection_par_utilisateur(
                id_utilisateur, schema
            )

            if not id_collection:
                logging.error(f"Aucune collection trouvée pour l'utilisateur {id_utilisateur}")
                return False
            # Etape 2 : Récuperer l'id_manga via son titre
            id_manga = MangaDao().trouver_id_par_titre(schema, titre_manga)

            # Étape 3: Ajouter le manga à la collection physique
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO collection_physique_mangas (id_collection,id_manga, titre_manga, numero_dernier_tome, numeros_tomes_manquants, status_manga)
                        VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_collection_physique_mangas;
                        """,
                        (
                            id_collection,
                            id_manga,
                            titre_manga,
                            numero_dernier_tome,
                            numeros_tomes_manquants,
                            status_manga,
                        ),
                    )

                connection.commit()
                return True

        except Exception as e:
            logging.error(f"Erreur lors de l'ajout des mangas à la collection : {e}")
            return False

    @log
    def supprimer(self, collection, schema) -> bool:

        table_map = {"Physique": "collection_physique", "Coherente": "collection_coherente"}

        if collection.type_collection not in table_map:
            logging.error("Type de collection invalide pour la suppression.")
            return False

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:

                    query = f"DELETE FROM {table_map[collection.type_collection]} WHERE id_collection=%(id_collection)s;"
                    cursor.execute(
                        query,
                        {
                            "id_collection": collection.id_collection,
                        },
                    )

                    return cursor.rowcount > 0
        except Exception as e:
            logging.error(f"Erreur lors de la suppression de la collection : {e}")
            return False

    @log
    def modifier_collection_coherente(self, collection: CollectionCoherente, schema: str) -> bool:

        query = """
        UPDATE collection_coherente
        SET titre_collection = %(titre_collection)s,
            description_collection = %(description_collection)s
        WHERE id_collection = %(id_collection)s;
        """

        params = {
            "titre_collection": collection.titre,
            "description_collection": collection.description,
            "id_collection": collection.id_collection,
        }

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, params)
                    res = cursor.fetchone()

                    if res:

                        return True
                    else:
                        logging.warning(
                            f"Aucune collection trouvée avec l'id {collection.id_collection}."
                        )
                        return False

        except Exception as e:
            logging.error(f"Erreur lors de la modification de la collection cohérente : {e}")
            return False

    @log
    def modifier_collection_physique(
        self, manga: MangaDansCollection, id_collection, id_manga, schema: str
    ) -> bool:

        # on modifie pas le titre du manga, sinon --> suppression du manga
        query = """

        UPDATE collection_physique_mangas
        SET 
            numero_dernier_tome = %(numero_dernier_tome)s,
            numeros_tomes_manquants = %(numeros_tomes_manquants)s,
            status_manga = %(status_manga)s
        WHERE id_manga = %(id_manga)s AND id_collection = %(id_collection)s;
    """

        params = {
            "id_manga": id_manga,
            "numero_dernier_tome": manga.dernier_tome_acquis,
            "numeros_tomes_manquants": manga.numeros_tomes_manquants,
            "status_manga": manga.status_manga,
            "id_collection": id_collection,
        }

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, params)

                    # Vérifiez combien de lignes ont été affectées
                    if cursor.rowcount > 0:
                        return True
                    else:
                        logging.warning(
                            f"Aucun manga trouvé avec l'id {id_manga} dans la collection {id_collection}."
                        )
                        return False

        except Exception as e:
            logging.error(f"Erreur lors de la mise à jour du manga : {e}")
            return False
