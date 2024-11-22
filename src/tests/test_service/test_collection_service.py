import pytest
from service.collection_service import ServiceCollection
from business_object.collection.collection_physique import CollectionPhysique
from business_object.collection.collection_coherente import CollectionCoherente


@pytest.fixture(scope="session")
def collections_service():
    collection1 = CollectionCoherente(titre="Collection Test 1", description="Description test 1")
    collection2 = CollectionCoherente(titre="Collection Test 2", description="Description test 2")
    collection_physique = CollectionPhysique()
    return collection1, collection2, collection_physique


@pytest.fixture(scope="session")
def service_collection():
    return ServiceCollection()


def test_creer_collection_coherente_ok(service_collection, collections_service):
    collection1, _, _ = collections_service
    result = service_collection.creer_collection(
        id_utilisateur=1,
        type_collection="Coherente",
        titre=collection1.titre,
        description=collection1.description,
        schema="projet_test_dao",
    )
    collection1.id_collection = result
    assert result is not None


def test_creer_collection_physique_ok(service_collection, collections_service):
    _, _, collection_physique = collections_service
    result = service_collection.creer_collection(
        id_utilisateur=1,
        type_collection="Physique",
        titre=None,
        description=None,
        schema="projet_test_dao",
    )
    collection_physique.id_collection = result
    assert result is not None


def test_ajouter_mangas_collection_coherente_ok(service_collection, collections_service):
    collection1, _, _ = collections_service
    liste_mangas = [1, 2, 3]
    result = service_collection.ajouter_mangas_collection_coherente(
        collection_id=collection1.id_collection, liste_mangas=liste_mangas, schema="projet_test_dao"
    )
    assert result is True


def test_ajouter_manga_collection_physique_ok(service_collection):
    result = service_collection.ajouter_manga_collection_physique(
        id_utilisateur=1,
        titre_manga="Black Clover",
        numero_dernier_tome=23,
        numeros_tomes_manquants=[1, 5],
        status_manga="Terminé",
        schema="projet_test_dao",
    )
    assert result is True


def test_lister_collections_coherentes_ok(service_collection):
    collections = service_collection.lister_collections_coherentes(
        id_utilisateur=1, schema="projet_test_dao"
    )
    assert collections is not None
    assert isinstance(collections, list)
    assert len(collections) > 0


def test_lister_mangas_collection_ok(service_collection, collections_service):
    collection1, _, _ = collections_service
    mangas = service_collection.lister_mangas_collection(
        id_collection=collection1.id_collection, schema="projet_test_dao"
    )
    assert mangas is not None
    assert isinstance(mangas, list)


def test_rechercher_collections_et_mangas_par_user_ok(service_collection):
    result = service_collection.rechercher_collections_et_mangas_par_user(
        id_utilisateur=1, schema="projet_test_dao"
    )
    assert result is not None
    assert isinstance(result, dict)
    assert len(result) > 0


def test_supprimer_collection_coherente_ok(service_collection, collections_service):
    collection1, _, _ = collections_service
    result = service_collection.supprimer_collection(
        id_collection=collection1.id_collection,
        type_collection="Coherente",
        schema="projet_test_dao",
    )
    assert result is True


def test_supprimer_collection_physique_ok(service_collection, collections_service):
    _, _, collection_physique = collections_service
    result = service_collection.supprimer_collection(
        id_collection=collection_physique.id_collection,
        type_collection=collection_physique.type_collection,
        schema="projet_test_dao",
    )
    assert result is True
