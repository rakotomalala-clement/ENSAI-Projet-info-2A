from collection import Collection


class CollectionCohérente(Collection):

    def __init__(self, titre: str, description: str, id_collection: int = None):
        super().__init__(
            id_collection=id_collection,
            titre=titre,
            description=description,
            type_collection="Cohérente",
        )
