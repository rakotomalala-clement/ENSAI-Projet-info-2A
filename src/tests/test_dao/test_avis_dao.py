import os
import pytest

from unittest.mock import patch

from utils.reset_database import ResetDatabase

from business_object.avis import Avis
from dao.avis_dao import DaoAvis


def test_creer_avis_ok():
    """Création de Joueur réussie"""

    # GIVEN
    avis = Avis(1, "cool", 5)

    # WHEN
    creation_ok = DaoAvis().creer_avis(1, 1, avis)

    # THEN
    assert creation_ok
    assert avis.id_avis == 1


def test_creer_avis_col_coherente_ok():
    """Création de Joueur réussie"""

    # GIVEN
    avis = Avis(1, "cool", 5)

    # WHEN
    creation_ok = DaoAvis().creer_avis_collection_coherente(1, 1, avis)

    # THEN
    assert creation_ok
    assert avis.id_avis


if __name__ == "__main__":
    pytest.main([__file__])
