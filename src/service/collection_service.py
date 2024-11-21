from typing import List
from utils.log_decorator import log
import logging
from dao.collection_dao import DaoCollection
from business_object.collection.collection_physique import CollectionPhysique
from business_object.collection.collection_coherente import CollectionCoherente
from business_object.collection.mangas_dans_collection import MangaDansCollection
from dao.manga_dao import MangaDao


class ServiceCollection:

    def __init__(self):
        self.dao_collection = DaoCollection()

    def creer_collection(
        self,
        id_utilisateur,
        type_collection,
        titre,
        description,
        schema,
    ) -> int:
        if type_collection == "Physique":
            collection = CollectionPhysique()

        elif type_collection == "Coherente":
            collection = CollectionCoherente(titre=titre, description=description)

        else:
            logging.error("Type de collection inconnu.")
            return False

        self.dao_collection.creer(id_utilisateur, collection, schema)
        return collection.id_collection

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
            collections = self.dao_collection.lister_collections_coherentes(id_utilisateur, schema)

            result_dict = {}

            for collection in collections:
                mangas = self.dao_collection.lister_mangas_collection(
                    collection.id_collection, schema
                )

                result_dict[collection.id_collection] = [collection, mangas]

            return result_dict

        except Exception as e:
            logging.error(
                f"Erreur lors de la récupération des collections et des mangas pour l'utilisateur {id_utilisateur}: {e}"
            )
            return {}

    def rechercher_collection_physique(self, id_utilisateur: int, schema: str):

        return self.dao_collection.rechercher_collection_physique(id_utilisateur, schema)

    def lister_collections_physiques(
        self, id_utilisateur: int, schema: str
    ) -> List[CollectionPhysique]:

        return self.dao_collection.rechercher_collection_physique(id_utilisateur, schema)

    def ajouter_mangas_collection_coherente(
        self, collection_id: int, liste_mangas: List[int], schema: str
    ) -> bool:

        return self.dao_collection.ajouter_mangas_collection_coherente(
            collection_id, liste_mangas, schema
        )

    # l'ajout d'un manga qui existe déjà dans la collection génère un retour False
    def ajouter_manga_collection_physique(
        self,
        id_utilisateur,
        titre_manga,
        numero_dernier_tome,
        numeros_tomes_manquants,
        status_manga,
        schema,
    ):
        return self.dao_collection.ajouter_manga_collection_physique(
            id_utilisateur,
            titre_manga,
            numero_dernier_tome,
            numeros_tomes_manquants,
            status_manga,
            schema,
        )

    @log
    def supprimer_collection(self, id_collection, type_collection, schema: str) -> bool:

        if type_collection == "Coherente":
            collection = CollectionCoherente(
                id_collection=id_collection, titre=None, description=None
            )
        elif type_collection == "Physique":
            collection = CollectionPhysique(id_collection=id_collection)

        return self.dao_collection.supprimer(collection, schema)

    def supprimer_manga_col_physique(self, id_collection, id_manga, schema) -> bool:
        return self.dao_collection.supprimer_manga_col_physique(id_collection, id_manga, schema)

    def supprimer_manga_col_coherente(self, id_collection, id_manga, schema) -> bool:
        return self.dao_collection.supprimer_manga_col_coherente(id_collection, id_manga, schema)

    def modifier_collection_coherente(
        self, id_collection: int, titre: str, description: str, schema: str
    ) -> bool:
        collection = CollectionCoherente(
            id_collection=id_collection, titre=titre, description=description
        )
        return self.dao_collection.modifier_collection_coherente(collection, schema)

    def modifier_collection_physique(
        self,
        id_utilisateur: int,
        titre_manga: str,
        dernier_tome_acquis: int,
        numeros_tomes_manquants: str,
        status_manga: str,
        schema: str,
    ) -> bool:
        id_manga = MangaDao().trouver_id_par_titre(schema, titre_manga)
        id_collection = DaoCollection().obtenir_id_collection_par_utilisateur(
            id_utilisateur, schema
        )
        manga_collection = MangaDansCollection(
            titre_manga=titre_manga,
            dernier_tome_acquis=dernier_tome_acquis,
            numeros_tomes_manquants=numeros_tomes_manquants,
            status_manga=status_manga,
        )
        return self.dao_collection.modifier_collection_physique(
            manga_collection, id_collection, id_manga, schema
        )

    def obtenir_id_collection_par_utilisateur(self, id_utilisateur, schema):
        return self.dao_collection.obtenir_id_collection_par_utilisateur(id_utilisateur, schema)
