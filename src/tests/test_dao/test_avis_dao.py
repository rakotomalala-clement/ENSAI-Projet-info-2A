import os
import pytest

from unittest.mock import patch

from utils.reset_database import ResetDatabase

from business_object.avis import Avis
from dao.avis_dao import DaoAvis

def test_creer_avis_ok():
    """Création d'avis réussie"""

    # GIVEN
    avis = Avis(note=5, avis="cool")

    # WHEN
    creation_ok = DaoAvis().creer_avis(id_utilisateur=1, id_manga=1, avis_manga=avis)

    # THEN
    assert creation_ok



def test_creer_avis_col_coherente_ok():
    Création de Joueur réussie

    # GIVEN
    avis = Avis(note=5, avis="cool", id_avis=1)

    # WHEN
    creation_ok = DaoAvis().creer_avis_collection_coherente(
        id_utilisateur=1, id_collection=1, avis_collection_coherente=avis
    )

    # THEN
    assert creation_ok
    assert avis.id_avis


def test_creer_avis_col_physique_ok():
    Création de Joueur réussie

    # GIVEN
    avis = Avis(note=5, avis="cool", id_avis=1)

    # WHEN
    creation_ok = DaoAvis().creer_avis_collection_physique(
        id_utilisateur=1, id_collection=1, avis_collection_physique=avis
    )

    # THEN
    assert creation_ok
    assert avis.id_avis


def test_chercher_avis():
    Recherche des avis laisser par un utilisateur sur un manga

    # GIVEN

    # WHEN
    listeavis = DaoAvis().chercher_avis(id_utilisateur=1, id_manga=4)

    # THEN
    assert isinstance(listeavis, list)
    for a in listeavis:
        assert isinstance(a, Avis)

def test_modifier_avis_ok():
    avis = Avis(note=5, avis="cool")
    avis_originelle = DaoAvis().creer_avis("projet_test_dao", id_utilisateur=1, id_manga=1, avis_manga=avis)
    
    modification = DaoAvis().modifier_avis("projet_test_dao", avis=Avis(id_avis=avis_originelle.id_avis, avis="Superbe manga !", note=4))
    
    assert avis_originelle.avis != modification.avis
    assert avis_originelle.note != modification.note





"""

if __name__ == "__main__":
    pytest.main([__file__])
