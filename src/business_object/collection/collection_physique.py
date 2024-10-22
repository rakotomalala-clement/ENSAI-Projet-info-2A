from business_object.collection.collection_abstraite import AbstractCollection


class CollectionPhysique(AbstractCollection):

    def __init__(
        self, id_collection, titre, dernier_tome_acquis, numeros_tomes_manquants, status_collection
    ):
        super().__init__(  # Ajout des parenthèses ici
            id_collection=id_collection,
            titre=titre,
            type_collection="Physique",  # Ce paramètre est correct ici
        )
        self.dernier_tome_acquis = dernier_tome_acquis
        self.numeros_tomes_manquants = numeros_tomes_manquants  # Correction ici
        self.status_collection = status_collection
