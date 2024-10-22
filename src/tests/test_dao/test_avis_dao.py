import os
import pytest

from unittest.mock import patch

from utils.reset_database import ResetDatabase

from business_object.avis import Avis
from dao.avis_dao import DaoAvis


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        ResetDatabase().lancer(test_dao=True)
        yield


def test_creer_ok():
    """Création de Joueur réussie"""

    # GIVEN
    avis = Avis(1, 1, "cool", 5)

    # WHEN
    creation_ok = DaoAvis().creer_avis(avis)

    # THEN
    assert creation_ok
    assert avis.id_avis


if __name__ == "__main__":
    pytest.main([__file__])
