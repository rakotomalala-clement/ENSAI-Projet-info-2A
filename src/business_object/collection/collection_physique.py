from business_object.collection.collection_abstraite import AbstractCollection


class CollectionPhysique(AbstractCollection):

    def __init__(
        self,
        titre,
        dernier_tome_acquis,
        numeros_tomes_manquants,
        status_collection,
        id_collection=None,
    ):
        super().__init__(
            titre=titre,
            id_collection=id_collection,
            type_collection="Physique",
        )
        self.dernier_tome_acquis = dernier_tome_acquis
        self.numeros_tomes_manquants = numeros_tomes_manquants
        self.status_collection = status_collection
