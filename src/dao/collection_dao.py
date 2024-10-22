import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection


from business_object.collection.collection_physique import CollectionPhysique


class DaoCollection(metaclass=Singleton):

    @log
    def creer(self, id_utilisateur, id_manga, collection, schema) -> bool:

        res = None
        if collection.type_collection == "Physique":
            collection = CollectionPhysique(
                collection.id_collection,
                collection.titre,
                collection.dernier_tome_acquis,
                collection.numeros_tomes_manquants,
                collection.status_collection,
            )

            try:
                with DBConnection(schema).connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "INSERT INTO collection_physique(id_utilisateur, id_manga, titre_collection, numero_dernier_tome, numeros_tomes_manquants,status_collection) VALUES        "
                            "(%(id_utilisateur)s, %(id_manga)s, %(titre_collection)s, %(numero_dernier_tome)s, %(numeros_tomes_manquants)s,%(status_collection)s )             "
                            "  RETURNING titre_collection;",
                            {
                                "id_utilisateur": id_utilisateur,
                                "id_manga": id_manga,
                                "titre_collection": collection.titre,
                                "numero_dernier_tome": collection.dernier_tome_acquis,
                                "numeros_tomes_manquants": collection.numeros_tomes_manquants,
                                "status_collection": collection.status_collection,
                            },
                        )
                        res = cursor.fetchone()
            except Exception as e:
                logging.info(e)

            if collection.type_collection == "Coherente":
                collection = CollectionPhysique(
                    collection.id_collection,
                    collection.titre,
                    collection.dernier_tome_acquis,
                    collection.numeros_tomes_manquants,
                    collection.status_collection,
                )

                try:
                    with DBConnection(schema).connection as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(
                                "INSERT INTO collection_physique(id_utilisateur, id_manga, titre_collection, numero_dernier_tome, numeros_tomes_manquants,status_collection) VALUES        "
                                "(%(id_utilisateur)s, %(id_manga)s, %(titre_collection)s, %(numero_dernier_tome)s, %(numeros_tomes_manquants)s,%(status_collection)s )             "
                                "  RETURNING titre_collection;",
                                {
                                    "id_utilisateur": id_utilisateur,
                                    "id_manga": id_manga,
                                    "titre_collection": collection.titre,
                                    "numero_dernier_tome": collection.dernier_tome_acquis,
                                    "numeros_tomes_manquants": collection.numeros_tomes_manquants,
                                    "status_collection": collection.status_collection,
                                },
                            )
                            res = cursor.fetchone()
                except Exception as e:
                    logging.info(e)

            created = False

            if res:

                collection.titre = res["titre_collection"]
                created = True

            return created

    @log
    def supprimer(self, id_collection):


