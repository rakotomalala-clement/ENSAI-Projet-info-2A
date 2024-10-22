from collection import Collection


class CollectionPhysique(Collection):

    def __init__(
        self, id_collection, titre, dernier_tome_acquis, liste_tomes_manquants, status_collection
    ):
        super.__init__(
            id_collection=id_collection,
            titre=titre,
            type_collection="Physique",
        )
        self.dernier_tome_acquis = dernier_tome_acquis
        self.liste_tomes_manquants = liste_tomes_manquants
        self.status_collection = status_collection
