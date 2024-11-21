import pytest
from unittest import mock
from dao.collection_dao import DaoCollection
from dao.manga_dao import MangaDao
from business_object.collection.collection_physique import CollectionPhysique
from business_object.collection.collection_coherente import CollectionCoherente


@pytest.fixture(scope="session")
def collections():
    collection1 = CollectionCoherente(
        titre="Mangas Préférés", description="Liste de mes mangas préférés"
    )
    collection2 = CollectionCoherente(
        titre="Mangas Vacances", description="Liste de mangas à lire ces vacances"
    )
    collection3 = CollectionPhysique()
    return collection1, collection2, collection3


def test_creer_collection_physique_ok(capsys, collections):
    """Test de la création d'une collection physique."""
    with capsys.disabled():
        print("*********************** TEST création collection physique OK *****************")
        dao_collection = DaoCollection()
        _, _, collection = collections

        result = dao_collection.creer(
            id_utilisateur=1, collection=collection, schema="projet_test_dao"
        )
    assert result is True


# def test_creer_collection_physique_ko(capsys):
#     with capsys.disabled():
#         print("*********************** TEST création collection physique KO *****************")

#         """Création d'une collection physique échouée (id_utilisateur n'existe pas)"""
#         dao_collection = DaoCollection()
#         collection = CollectionPhysique()

#         result = dao_collection.creer(
#             id_utilisateur=500, collection=collection, schema="projet_test_dao"
#         )

#     assert result is False


def test_ajouter_manga_collection_physique_ok():
    dao_collection = DaoCollection()
    result1 = dao_collection.ajouter_manga_collection_physique(
        id_utilisateur=1,
        titre_manga="Black Clover",
        numero_dernier_tome=28,
        numeros_tomes_manquants=[1, 2, 3, 4],
        status_manga="En cours de publication",
        schema="projet_test_dao",
    )

    result2 = dao_collection.ajouter_manga_collection_physique(
        id_utilisateur=1,
        titre_manga="Hunter x Hunter",
        numero_dernier_tome=37,
        numeros_tomes_manquants=[1, 2, 3, 30, 5],
        status_manga="En cours de publication",
        schema="projet_test_dao",
    )

    assert result1 is True
    assert result2 is True


# def test_creer_collection_coherente_ok(collections):
#     """Test de la création d'une collection cohérente."""
#     dao_collection = DaoCollection()
#     collection1, collection2, _ = collections

#     result1 = dao_collection.creer(
#         id_utilisateur=1, collection=collection1, schema="projet_test_dao"
#     )
#     result2 = dao_collection.creer(
#         id_utilisateur=1, collection=collection2, schema="projet_test_dao"
#     )

#     assert result1 is True
#     assert result2 is True


# def test_lister_collections_coherentes_ok():
#     """Test de la recherche des collections cohérentes d'un utilisateur par son ID."""
#     dao_collection = DaoCollection()
#     id_utilisateur = 1

#     collections = dao_collection.lister_collections_coherentes(
#         id_utilisateur, schema="projet_test_dao"
#     )

#     assert collections is not None
#     assert isinstance(collections, list)
#     assert len(collections) > 0


# def test_rechercher_collection_physique_ok():
#     """Test de la recherche de la collection physique d'un utilisateur qui existe et qui
#     contient au moins un manga"""
#     dao_collection = DaoCollection()
#     id_utilisateur = 1

#     mangas_collection = dao_collection.rechercher_collection_physique(
#         id_utilisateur, schema="projet_test_dao"
#     )

#     assert mangas_collection is not None
#     assert isinstance(mangas_collection, list)
#     assert len(mangas_collection) > 0


# def test_ajouter_mangas_collection_coherente(collections):
#     """Test de l'ajout de mangas à une collection cohérente."""
#     collection1, _, _ = collections
#     collection_id = collection1.id_collection
#     liste_mangas = [1, 4, 3]

#     dao_collection = DaoCollection()

#     result = dao_collection.ajouter_mangas_collection_coherente(
#         collection_id, liste_mangas, schema="projet_test_dao"
#     )
#     assert result is True


# def test_modifier_collection_coherente(collections):
#     """Test de la modification d'une collection cohérente."""
#     dao_collection = DaoCollection()
#     collection1, _, _ = collections
#     collection = CollectionCoherente(
#         id_collection=collection1.id_collection,
#         titre="Mangas été",
#         description="Liste de mangas à lire pendant l'été ",
#     )

#     result = dao_collection.modifier_collection_coherente(collection, schema="projet_test_dao")

#     assert result is True


# def test_recuperer_mangas_collection_coherente_ok(collections):

#     dao_collection = DaoCollection()
#     collection1, _, _ = collections

#     result = dao_collection.lister_mangas_collection(
#         collection1.id_collection, schema="projet_test_dao"
#     )

#     assert len(result) > 0


# def test_supprimer_manga_col_coherente_ok(collections, capsys):
#     with capsys.disabled():
#         collection1, _, _ = collections
#         dao_collection = DaoCollection()
#         dao_manga = MangaDao()

#         liste_mangas = dao_collection.lister_mangas_collection(
#             collection1.id_collection, schema="projet_test_dao"
#         )

#         id_manga = dao_manga.trouver_id_par_titre(
#             schema="projet_test_dao", titre=liste_mangas[0].titre
#         )

#         result = dao_collection.supprimer_manga_col_coherente(
#             collection1.id_collection, id_manga, schema="projet_test_dao"
#         )
#     assert result is True


# def test_supprimer_collection_coherente_ok(collections):
#     """Test de la suppression d'une collection cohérente."""
#     dao_collection = DaoCollection()
#     collection1, collection2, _ = collections

#     collection1 = CollectionCoherente(
#         id_collection=collection1.id_collection,
#         titre=None,
#         description=None,
#     )
#     collection2 = CollectionCoherente(
#         id_collection=collection2.id_collection,
#         titre=None,
#         description=None,
#     )

#     result1 = dao_collection.supprimer(collection1, schema="projet_test_dao")
#     result2 = dao_collection.supprimer(collection2, schema="projet_test_dao")

#     assert result1 is True
#     assert result2 is True


# def test_modifier_collection_physique(collections):
#     """Test de la modification d'une collection physique (numeros tomes manquants)."""
#     dao_collection = DaoCollection()
#     dao_manga = MangaDao()
#     _, _, collection = collections
#     liste_mangas = dao_collection.rechercher_collection_physique(1, schema="projet_test_dao")

#     liste_mangas[0].numeros_tomes_manquants = [1, 2, 20]
#     id_manga = dao_manga.trouver_id_par_titre(
#         schema="projet_test_dao", titre=liste_mangas[0].titre_manga
#     )

#     result = dao_collection.modifier_collection_physique(
#         liste_mangas[0], collection.id_collection, id_manga, schema="projet_test_dao"
#     )

#     assert result is True


# def test_supprimer_manga_col_physique_ok(collections):
#     _, _, collection = collections
#     dao_collection = DaoCollection()
#     dao_manga = MangaDao()

#     liste_mangas = dao_collection.rechercher_collection_physique(1, schema="projet_test_dao")
#     id_manga = dao_manga.trouver_id_par_titre(
#         schema="projet_test_dao", titre=liste_mangas[0].titre_manga
#     )

#     result = dao_collection.supprimer_manga_col_physique(
#         collection.id_collection, id_manga, schema="projet_test_dao"
#     )
#     assert result is True


# def test_supprimer_collection_physique_ok(collections):
#     """Test de la suppression d'une collection cohérente."""
#     dao_collection = DaoCollection()
#     _, _, collection3 = collections

#     collection = CollectionPhysique(
#         id_collection=collection3.id_collection,
#     )

#     result = dao_collection.supprimer(collection, schema="projet_test_dao")

#     assert result is True
