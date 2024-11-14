from abc import ABC


class AbstractCollection(ABC):

    def __init__(self, id_collection=None, type_collection=None):
        self.id_collection = id_collection
        self.type_collection = type_collection
