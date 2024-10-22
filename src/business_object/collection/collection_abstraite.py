from abc import ABC


class AbstractCollection(ABC):

    def __init__(self, titre, id_collection=None, type_collection=None):
        self.id_collection = id_collection
        self.titre = titre
        self.type_collection = type_collection
