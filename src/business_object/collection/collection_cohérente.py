from collection import Collection


class CollectionCohérente(Collection):

    def __init__(self, id_collection: int, titre: str, description: str):
        super().__init__(
            id_collection=id_collection,
            titre=titre,
            description=description,
            type_collection="Cohérente",
        )
