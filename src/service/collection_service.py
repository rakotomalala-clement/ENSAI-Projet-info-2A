from typing import List
from dao.collection_dao import DaoCollection
from business_object.collection.collection_physique import CollectionPhysique
from business_object.collection.collection_coherente import CollectionCoherente


class ServiceCollection:

    def __init__(self):
        self.dao_collection = DaoCollection()

    def creer_collection(
        self,
        id_utilisateur: int,
        type_collection,
        titre,
        description,
        dernier_tome_acquis,
        numeros_tomes_manquants,
        status,
        schema: str,
        id_manga=None,
    ) -> bool:
        if type_collection == "Physique":
            collection = CollectionPhysique(
                titre,
                dernier_tome_acquis,
                numeros_tomes_manquants,
                status,
            )
        
        else:
            collection = CollectionCoherente(titre, description)

        return self.dao_collection.creer(id_utilisateur, collection, schema, id_manga)

    def rechercher_collection_coherente_par_user(
        self, id_utilisateur: int, schema: str
    ) -> List[CollectionCoherente]:

        return self.dao_collection.rechercher_collection_coherente_par_user(id_utilisateur, schema)

    def rechercher_collection_physique_par_user_manga(
        self, id_utilisateur: int, id_manga: int, schema: str
    ) -> List[CollectionPhysique]:

        return self.dao_collection.rechercher_collection_physique_par_user_manga(
            id_utilisateur, id_manga, schema
        )

    def rechercher_collection_physique_par_user(
        self, id_utilisateur: int, schema: str
    ) -> List[CollectionPhysique]:

        return self.dao_collection.rechercher_collection_physique_par_user(id_utilisateur, schema)

    def ajouter_mangas_a_collection(
        self, collection_id: int, liste_mangas: List[int], schema: str
    ) -> bool:

        return self.dao_collection.ajouter_mangas_a_collection(collection_id, liste_mangas, schema)

    def supprimer_collection(self, collection, id_utilisateur: int, schema: str) -> bool:

        return self.dao_collection.supprimer(collection, id_utilisateur, schema)

    def modifier_collection_coherente(self, collection: CollectionCoherente, schema: str) -> bool:

        return self.dao_collection.modifier_collection_coherente(collection, schema)

    def modifier_collection_physique(self, collection: CollectionPhysique, schema: str) -> bool:

        return self.dao_collection.modifier_collection_physique(collection, schema)
