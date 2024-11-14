from business_object.collection.collection_abstraite import AbstractCollection


class CollectionPhysique(AbstractCollection):

    def __init__(
        self,
        id_collection=None,
    ):
        super().__init__(
            id_collection=id_collection,
            type_collection="Physique",
        )
