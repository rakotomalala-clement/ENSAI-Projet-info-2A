from abc import ABC


class AbstractCollection(ABC):

    def __init__(
        self,
        id_collection=None,
        titre=None,
        type_collection=None,
    ):
        self.id_collection = id_collection
        self.titre = titre
        self.type_collection = type_collection
