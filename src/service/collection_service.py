from typing import List
from utils.log_decorator import log
import logging
from dao.collection_dao import DaoCollection
from business_object.collection.collection_physique import CollectionPhysique
from business_object.collection.collection_coherente import CollectionCoherente


class ServiceCollection:

    def __init__(self):
        self.dao_collection = DaoCollection()

    def creer_collection(
        self,
        id_utilisateur,
        type_collection,
        titre,
        description,
        dernier_tome_acquis,
        numeros_tomes_manquants,
        status,
        schema,
        id_manga,
    ) -> bool:
        if type_collection == "Physique":
            collection = CollectionPhysique(
                titre,
                dernier_tome_acquis,
                numeros_tomes_manquants,
                status,
            )

        elif type_collection == "Coherente":
            collection = CollectionCoherente(titre=titre, description=description)

        else:
            logging.error("Type de collection inconnu.")
            return False

        return self.dao_collection.creer(id_utilisateur, collection, schema, id_manga)

    def lister_collections_coherentes(
        self, id_utilisateur: int, schema: str
    ) -> List[CollectionCoherente]:

        return self.dao_collection.lister_collections_coherentes(id_utilisateur, schema)

    @log
    def lister_mangas_collection(self, id_collection: int, schema: str):
        """Récupère les mangas associés à une collection cohérente en utilisant le DAO"""
        try:
            mangas = self.dao_collection.lister_mangas_collection(id_collection, schema)

            return mangas

        except Exception as e:
            logging.error(
                f"Erreur lors de la récupération des mangas pour la collection {id_collection}: {e}"
            )
            return []

    @log
    def rechercher_collections_et_mangas_par_user(self, id_utilisateur: int, schema: str) -> dict:
        """Recherche les collections cohérentes créées par l'utilisateur et leurs mangas associés, sous forme de dictionnaire.
        Exemple : (la clé du dictionnaire correspond à l'id collection)
                dict = {
                1: [
                    CollectionCoherente(id_collection=1, titre="Collection 1", description="Description 1"),
                    [
                        Manga(id_manga=101, titre="Manga 1"),
                        Manga(id_manga=102, titre="Manga 2")
                    ]
                ],
                2: [
                    CollectionCoherente(id_collection=2, titre="Collection 2", description="Description 2"),
                    [
                        Manga(id_manga=103, titre="Manga 3"),
                        Manga(id_manga=104, titre="Manga 4")
                    ]
                ],

            }

        """
        try:
            # on récupère toutes les collections cohérentes de l'utilisateur
            collections = self.dao_collection.lister_collections_coherentes(id_utilisateur, schema)

            result_dict = {}

            # on récupère les mangas associés à chaque collection cohérente
            for collection in collections:
                mangas = self.dao_collection.lister_mangas_collection(
                    collection.id_collection, schema
                )

                # on ajoute la collection et sa liste de mangas dans le dictionnaire avec l'id de la collection COMME CLE
                result_dict[collection.id_collection] = [collection, mangas]

            return result_dict

        except Exception as e:
            logging.error(
                f"Erreur lors de la récupération des collections et des mangas pour l'utilisateur {id_utilisateur}: {e}"
            )
            return {}

    def rechercher_collection_physique(
        self, id_utilisateur: int, id_manga: int, schema: str
    ) -> List[CollectionPhysique]:

        return self.dao_collection.rechercher_collection_physique(id_utilisateur, id_manga, schema)

    def lister_collections_physiques(
        self, id_utilisateur: int, schema: str
    ) -> List[CollectionPhysique]:

        return self.dao_collection.lister_collections_physiques(id_utilisateur, schema)

    def ajouter_mangas(self, collection_id: int, liste_mangas: List[int], schema: str) -> bool:

        return self.dao_collection.ajouter_mangas(collection_id, liste_mangas, schema)

    @log
    def supprimer_collection(self, id_collection, type_collection, schema: str) -> bool:

        if type_collection == "Coherente":
            collection = CollectionCoherente(id_collection=id_collection)
        elif type_collection == "Physique":
            collection = CollectionPhysique(id_collection=id_collection)
        else:
            logging.error("Type de collection inconnu pour la suppression.")
            return False

        return self.dao_collection.supprimer(collection, schema)

    def modifier_collection_coherente(
        self, id_collection: int, titre: str, description: str, schema: str
    ) -> bool:
        collection = CollectionCoherente(
            id_collection=id_collection, titre=titre, description=description
        )
        return self.dao_collection.modifier_collection_coherente(collection, schema)

    def modifier_collection_physique(
        self,
        id_collection: int,
        titre: str,
        dernier_tome_acquis: int,
        numeros_tomes_manquants: str,
        status_collection: str,
        schema: str,
    ) -> bool:
        collection = CollectionPhysique(
            id_collection=id_collection,
            titre=titre,
            dernier_tome_acquis=dernier_tome_acquis,
            numeros_tomes_manquants=numeros_tomes_manquants,
            status_collection=status_collection,
        )
        return self.dao_collection.modifier_collection_physique(collection, schema)
