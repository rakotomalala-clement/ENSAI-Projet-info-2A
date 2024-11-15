from business_object.collection.collection_abstraite import AbstractCollection


class CollectionCoherente(AbstractCollection):

    def __init__(self, titre: str, description: str, id_collection: int = None):
        super().__init__(
            id_collection=id_collection,
            type_collection="Coherente",
        )
        self.titre = titre
        self.description = description
