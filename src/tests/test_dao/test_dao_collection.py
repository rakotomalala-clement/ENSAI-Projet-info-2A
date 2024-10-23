import os
import pytest
from unittest import mock
from dao.collection_dao import DaoCollection
from utils.reset_database import ResetDatabase
from business_object.collection.collection_physique import CollectionPhysique
from business_object.collection.collection_coherente import CollectionCoherente


# @pytest.fixture(scope="session", autouse=True)
# def setup_test_environment():
#     """Initialisation des données de test."""
#     original_schema = os.environ.get("POSTGRES_SCHEMA")
#     with mock.patch.dict(os.environ, {"POSTGRES_SCHEMA": "projet_test_dao"}):
#         # Réinitialisation de la base de données ou toute autre préparation nécessaire
#         ResetDatabase().lancer(test_dao=True)
#         yield
#     # Restore original schema
#     os.environ["POSTGRES_SCHEMA"] = original_schema


def test_creer_collection_physique():
    """Test de la création d'une collection physique."""
    dao_collection = DaoCollection()
    collection = CollectionPhysique(
        id_collection=None,
        titre="2",
        dernier_tome_acquis=2,
        numeros_tomes_manquants="3 - 4",
        status_collection="t",
    )

    result = dao_collection.creer(
        id_utilisateur=3, collection=collection, schema="projet_test_dao", id_manga=1
    )
    assert result is True


def test_creer_collection_coherente():
    """Test de la création d'une collection cohérente."""
    dao_collection = DaoCollection()
    collection = CollectionCoherente(titre="40", description="description 2", id_collection=None)

    result = dao_collection.creer(
        id_utilisateur=12, collection=collection, schema="projet_test_dao", id_manga=None
    )
    assert result is True


def test_rechercher_collection_coherente_par_user_ok():
    """Test de la recherche des collections cohérentes d'un utilisateur par son ID."""
    dao_collection = DaoCollection()
    id_utilisateur = 12
    print("hello")

    collections = dao_collection.rechercher_collection_coherente_par_user(
        id_utilisateur, schema="projet_test_dao"
    )

    assert collections is not None, "La recherche n'a retourné aucun résultat."
    assert isinstance(collections, list), "Le résultat n'est pas une liste."
    assert len(collections) > 0, "Aucune collection trouvée."

    for collection in collections:
        print(collection)
        assert isinstance(
            collection, CollectionCoherente
        ), "Un élément n'est pas du type CollectionCoherente."

        assert collection.titre is not None, "Le titre de la collection ne doit pas être nul."
        assert collection.description is not None


def test_ajouter_mangas_a_collection():
    """Test de l'ajout de mangas à une collection cohérente."""

    collection_id = 1
    liste_mangas = [1, 4, 3]

    dao_collection = DaoCollection()

    try:
        result = dao_collection.ajouter_mangas_a_collection(
            collection_id, liste_mangas, schema="projet_test_dao"
        )
        assert result is True
    except Exception as e:
        print(f"Erreur rencontrée : {e}")
        assert False, "Le test a échoué en raison d'une exception."


def test_supprimer_collection_coherente():
    """Test de la suppression d'une collection cohérente."""
    dao_collection = DaoCollection()

    collection = CollectionCoherente(
        id_collection=1,
        titre="40",
        description="Description de la collection",
    )

    result = dao_collection.supprimer(collection, schema="projet_test_dao")

    assert result is True, "La collection cohérente n'a pas été supprimée avec succès."


def test_modifier_collection_coherente():
    """Test de la modification d'une collection cohérente."""
    dao_collection = DaoCollection()

    collection = CollectionCoherente(
        id_collection=1,
        titre="Nouveau titre",
        description="Nouvelle description",
    )

    result = dao_collection.modifier_collection_coherente(collection, schema="projet_test_dao")

    assert result is True, "La modification de la collection cohérente a échoué."
