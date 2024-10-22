from collection_asbtraite import AbstractCollection


class CollectionCohérente(AbstractCollection):

    def __init__(self, titre: str, description: str, id_collection: int = None):
        super().__init__(
            id_collection=id_collection,
            titre=titre,
            type_collection="Cohérente",
        )
        self.description = description
