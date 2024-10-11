from collection import Collection


class CollectionCohérente(Collection):

    def __init__(self, id_collection: int, titre: str, description: text):
        self.id_collection = id_collection
        self.titre = titre
        self.description = description
