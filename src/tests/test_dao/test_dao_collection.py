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
        titre="1",
        dernier_tome_acquis=2,
        numeros_tomes_manquants="3 - 4",
        status_collection="t",
    )

    result = dao_collection.creer(
        id_utilisateur=1, collection=collection, schema="projet_test_dao", id_manga=1
    )
    assert result is True


def test_creer_collection_coherente():
    """Test de la création d'une collection cohérente."""
    dao_collection = DaoCollection()
    collection = CollectionCoherente(id_collection=None, titre="1", description="description 1")

    result = dao_collection.creer(id_utilisateur=1, collection=collection, schema="projet_test_dao")
    assert result is True
