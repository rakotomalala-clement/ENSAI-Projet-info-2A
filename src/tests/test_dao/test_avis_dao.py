# import os
import pytest

# from unittest.mock import patch

# from utils.reset_database import ResetDatabase

from business_object.avis import Avis
from dao.avis_dao import DaoAvis


# @pytest.fixture(scope="session", autouse=True)
# def setup_test_environment():
#    """Initialisation des données de test"""
#    with patch.dict(os.environ, {"SCHEMA": "projet_info_dao"}):
#        ResetDatabase().lancer()
#        yield


# avis_manga = Avis(note=5, avis="Superbe manga !")

DaoAvis().supprimer_avis(18, "projet_test_dao")


def test_creer_avis_ok():
    """Création d'avis réussie"""

    # GIVEN
    avis = Avis(note=5, avis="cool")

    # WHEN
    creation_ok = DaoAvis().creer_avis(
        id_utilisateur=12, id_manga=1, avis=avis, schema="projet_test_dao"
    )

    # THEN
    assert creation_ok


def test_creer_avis_col_coherente_ok():
    """Création d avis sur collection cohérente"""

    # GIVEN
    avis = Avis(note=5, avis="cool")

    # WHEN
    creation_ok = DaoAvis().creer_avis_collection_coherente(
        id_utilisateur=12,
        id_collection_coherente=1,
        avis_collection_coherente=avis,
        schema="projet_test_dao",
    )

    # THEN
    assert creation_ok


def test_creer_avis_col_physique_ok():
    """Création d ais de collection physique réussie"""

    # GIVEN
    avis = Avis(note=5, avis="excelent")

    # WHEN
    creation_ok = DaoAvis().creer_avis_collection_physique(
        id_utilisateur=12, id_collection=1, avis_collection_physique=avis, schema="projet_test_dao"
    )

    # THEN
    assert creation_ok


"""
def test_chercher_avis():
    Recherche des avis laisser par un utilisateur sur un manga

    # GIVEN

    # WHEN
    listeavis = DaoAvis().chercher_avis(id_utilisateur=1, id_manga=4)

    # THEN
    assert isinstance(listeavis, list)
    for a in listeavis:
        assert isinstance(a, Avis)
"""


if __name__ == "__main__":

    pytest.main([__file__])
