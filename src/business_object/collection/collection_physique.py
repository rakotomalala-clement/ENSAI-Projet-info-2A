from business_object.collection.collection_abstraite import AbstractCollection


class CollectionPhysique(AbstractCollection):

    def __init__(
        self, id_collection, titre, dernier_tome_acquis, numeros_tomes_manquants, status_collection
    ):
        super.__init__(
            id_collection=id_collection,
            titre=titre,
            type_collection="Physique",
        )
        self.dernier_tome_acquis = dernier_tome_acquis
        self.numero_tomes_manquants = numeros_tomes_manquants
        self.status_collection = status_collection
