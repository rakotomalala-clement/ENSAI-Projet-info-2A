import pytest
from business_object.avis import Avis
from dao.avis_dao import DaoAvis


def test_trouver_id_avis_par_id_manga_utilisateur_true():
    """Recherche par l'id d'un manga/utilisateur l'id d'un avis existant."""
    id_manga = 1
    id_utilisateur = 12
    id_avis = DaoAvis().trouver_id_avis_par_id_manga_utilisateur(
        "projet_test_dao", id_manga, id_utilisateur
    )
    assert id_avis == 26


def test_trouver_id_avis_par_id_manga_utilisateur_false():
    """Recherche l'id d'un avis par l'id d'un manga/utilisateur non existant."""
    id_manga = 111111
    id_utilisateur = 11111111
    id_avis = DaoAvis().trouver_id_avis_par_id_manga_utilisateur(
        "projet_test_dao", id_manga, id_utilisateur
    )
    assert id_avis is None


def test_creer_avis_ok():
    """Création d'avis réussie."""
    # GIVEN
    avis = Avis(note=4, avis="cool cool")
    # WHEN
    creation_ok = DaoAvis().creer_avis(
        id_utilisateur=35, id_manga=3, avis=avis, schema="projet_test_dao"
    )
    # THEN
    assert creation_ok


def test_creer_avis_col_coherente_ok():
    """Création d'avis sur collection cohérente."""
    # GIVEN
    avis = Avis(note=4, avis="coool")
    # WHEN
    creation = DaoAvis().creer_avis_collection_coherente(
        id_utilisateur=12,
        id_collection_coherente=1,
        avis_collection_coherente=avis,
        schema="projet_test_dao",
    )
    # THEN
    assert creation


def test_creer_avis_col_physique_ok():
    """Création d'avis de collection physique réussie."""
    # GIVEN
    avis = Avis(note=5, avis="excellent")
    # WHEN
    creation_ok = DaoAvis().creer_avis_collection_physique(
        id_utilisateur=12, id_collection=13, avis_collection_physique=avis, schema="projet_test_dao"
    )
    # THEN
    assert creation_ok


def test_chercher_avis_sur_manga():
    """Recherche des avis laissés sur un manga."""
    avis = Avis(note=5, avis="cool", id_avis=26)
    avis_a_verifier = DaoAvis().chercher_avis_sur_manga("projet_test_dao", id_manga=1)
    assert avis in avis_a_verifier


def test_chercher_avis():
    """Recherche des avis laissés par un utilisateur sur un manga."""
    avis = Avis(note=5, avis="cool", id_avis=19)
    avis_a_verifier = DaoAvis().chercher_avis("projet_test_dao", id_utilisateur=12, id_manga=1)
    assert avis == avis_a_verifier


def test_modifier_avis_ok():
    """Modification d'un avis existant."""

    # WHEN
    modification = DaoAvis().modifier_avis(
        "projet_test_dao",
        avis=Avis(id_avis=25, avis="Superbe !", note=5),
        id_manga=3,
        id_utilisateur=35,
    )

    # THEN
    assert modification is True, "La modification de l'avis devrait retourner True"


if __name__ == "__main__":
    pytest.main([__file__])
