import os
import pytest
from unittest.mock import patch
from utils.reset_database import ResetDatabase
from dao.collection_dao import DaoCollection
from business_object.collection.collection_physique import CollectionPhysique


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        ResetDatabase().lancer(test_dao=True)
        yield


def test_creer_ok():
    """Création de Joueur réussie"""

    # GIVEN
    collection = CollectionPhysique(
        id_collection=None,
        titre="collection pc 1",
        dernier_tome_acquis=2,
        liste_tomes_manquants="3 - 4",
        status_collection="Terminé",
    )

    # WHEN
    creation_ok = DaoCollection().creer(1, 1, collection)

    # THEN
    assert creation_ok
    assert collection.titre == "collection pc 1"
