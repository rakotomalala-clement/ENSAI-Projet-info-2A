import logging
from typing import List
from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection


from business_object.collection.collection_physique import CollectionPhysique
from business_object.collection.collection_coherente import CollectionCoherente


class DaoCollection(metaclass=Singleton):

    @log
    def creer(self, id_utilisateur, collection, schema, id_manga) -> bool:
        res = None
        created = False

        if collection.type_collection == "Physique":
            collection = CollectionPhysique(
                collection.id_collection,
                collection.titre,
                collection.dernier_tome_acquis,
                collection.numeros_tomes_manquants,
                collection.status_collection,
            )
            query = """
                INSERT INTO collection_physique (id_utilisateur, id_manga, titre_collection, numero_dernier_tome, numeros_tomes_manquants, status_collection)
                VALUES (%(id_utilisateur)s, %(id_manga)s, %(titre_collection)s, %(numero_dernier_tome)s, %(numeros_tomes_manquants)s, %(status_collection)s)
                RETURNING titre_collection;
            """
            params = {
                "id_utilisateur": id_utilisateur,
                "id_manga": id_manga,
                "titre_collection": collection.titre,
                "numero_dernier_tome": collection.dernier_tome_acquis,
                "numeros_tomes_manquants": collection.numeros_tomes_manquants,
                "status_collection": collection.status_collection,
            }

        elif collection.type_collection == "Coherente":
            collection = CollectionCoherente(
                collection.titre,
                collection.description,
                collection.id_collection,
            )
            query = """
                INSERT INTO collection_coherente (id_utilisateur, titre_collection, description_collection)
                VALUES (%(id_utilisateur)s, %(titre_collection)s, %(description_collection)s)
                RETURNING titre_collection;
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
                        collection.titre = res["titre_collection"]
                        created = True

        except Exception as e:
            logging.error(f"Erreur lors de la création de la collection : {e}")
            raise e

        return created

    @log
    def rechercher_collection_coherente_par_user(
        self, id_utilisateur: int, schema
    ) -> List[CollectionCoherente]:
        """Recherche une collection cohérente par ID user dans la base de données."""
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

                collections = []

                for result in results:
                    print(result["id_collection"])
                    collection = CollectionCoherente(
                        id_collection=result["id_collection"],
                        titre=result["titre_collection"],
                        description=result["description_collection"],
                    )
                    collections.append(collection)

                return collections
        except Exception as e:
            logging.error(
                f"Erreur lors de la recherche de la collection avec id user {id_utilisateur}: {e}"
            )
            raise e

    @log
    def ajouter_mangas_a_collection(self, collection_id, liste_mangas, schema) -> bool:
        """Ajoute une liste de mangas à une collection cohérente dans la base de données."""

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:

                    for manga_id in liste_mangas:

                        cursor.execute(
                            """
                                SELECT COUNT(*) FROM collection_coherente_mangas 
                                WHERE id_collection = %s AND id_manga = %s;
                                """,
                            (collection_id, manga_id),
                        )
                        result = cursor.fetchone()
                        count = result["count"] if result else 0

                        if count == 0:
                            cursor.execute(
                                """
                                    INSERT INTO collection_coherente_mangas (id_collection, id_manga)
                                    VALUES (%s, %s);
                                    """,
                                (collection_id, manga_id),
                            )

                    connection.commit()
                    return True
        except Exception as e:
            logging.error(f"Erreur lors de l'ajout des mangas à la collection : {e}")
            return False

    @log
    def supprimer(self, collection, schema):

        table_map = {"Physique": "collection_physique", "Coherente": "collection_coherente"}

        if collection.type_collection not in table_map:
            logging.error(f"Type de collection invalide: {collection.type_collection}")
            return False

        try:
            with DBConnection(schema).connection as connection:
                with connection.cursor() as cursor:

                    query = f"DELETE FROM {table_map[collection.type_collection]} WHERE titre_collection=%(titre)s;"
                    cursor.execute(query, {"titre": collection.titre})

                    return cursor.rowcount > 0
        except Exception as e:
            logging.error(f"Erreur lors de la suppression de la collection : {e}")
            raise e

    @log
    def modifier_collection_coherente(self, collection: CollectionCoherente, schema: str) -> bool:
        """
        Modifie une collection cohérente dans la base de données.

        :param collection: CollectionCoherente, un objet contenant les nouvelles valeurs de la collection.
        :param schema: str, le schéma de la base de données à utiliser.
        :return: bool, True si la mise à jour a réussi, False sinon.
        """
        query = """
        UPDATE collection_coherente
        SET titre_collection = %(titre_collection)s, 
            description_collection = %(description_collection)s
        WHERE id_collection = %(id_collection)s
        RETURNING id_collection;
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
