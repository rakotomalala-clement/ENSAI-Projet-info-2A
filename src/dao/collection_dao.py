import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection


from business_object.collection.collection_physique import CollectionPhysique


class DaoCollection(metaclass=Singleton):

    @log
    def creer(self, id_utilisateur, id_manga, collection) -> bool:

        res = None
        if collection.type_collection == "Physique":
            collection = CollectionPhysique(
                collection.id_collection,
                collection.titre,
                collection.dernier_tome_acquis,
                collection.liste_tomes_manquants,
            )

            try:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "INSERT INTO collection_physique(id_utilisateur, id_manga, titre_collection, numero_dernier_tome, numeros_tomes_manquants,status_collection) VALUES        "
                            "(%(id_utilisateur)s, %(id_manga)s, %(titre_collection)s, %(numero_dernier_tome)s, %(numeros_tomes_manquants)s, )             "
                            "  RETURNING id_colelction;                                                ",
                            {
                                "id_utilisateur": id_utilisateur,
                                "id_manga": id_manga,
                                "titre_collection": collection.titre,
                                "numero_dernier_tome": collection.numero_dernier_tome,
                                "numeros_tomes_manquants": collection.numeros_tomes_manquants,
                            },
                        )
                        res = cursor.fetchone()
            except Exception as e:
                logging.info(e)

            created = False
            if res:
                collection.id_joueur = res["id_collection"]
                created = True

            return created
