from collection import Collection


class CollectionPhysique(Collection):

    def __init__(self, titre, dernier_tome_acquis, liste_tomes_manquants):
        super.__init__(
            titre=titre,
            dernier_tome_acquis=dernier_tome_acquis,
            liste_tomes_manquants=liste_tomes_manquants,
            type_collection="Physique",
        )
