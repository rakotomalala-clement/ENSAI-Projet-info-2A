from abc import ABC


class AbstractCollection(ABC):

    def __init__(
        self,
        id_collection=None,
        titre=None,
        description=None,
        dernier_tome_acquis=None,
        liste_tomes_manquants=[],
        type_collection=None,
    ):
        self.id_collection = id_collection
        self.titre = titre
        self.description = description
        self.dernier_tome_acquis = dernier_tome_acquis
        self.liste_tomes_manquants = liste_tomes_manquants
        self.type_collection = type_collection
