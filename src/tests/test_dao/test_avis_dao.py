import pytest
from business_object.avis import Avis
from dao.avis_dao import DaoAvis

<<<<<<< HEAD
DaoAvis().supprimer_avis(
    schema="projet_test_dao",
    id_avis=DaoAvis().trouver_id_avis_par_id_manga_utilisateur(
        schema="projet_test_dao", id_manga=1, id_utilisateur=12
    ),
)
DaoAvis().supprimer_avis_col_coherente(
    id_avis_collection_coherente=DaoAvis().trouver_id_avis_par_id_col_coherente_utilisateur(
        "projet_test_dao", 1, 12
    ),
    schema="projet_test_dao",
)
DaoAvis().supprimer_avis_col_physique(
    id_avis_collection_physique=DaoAvis().trouver_id_avis_par_id_manga_utilisateur_col_physique(
        schema="projet_test_dao", id_collection=1, id_utilisateur=43
    ),
    schema="projet_test_dao",
)
=======

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
>>>>>>> ec1c0aa147163376a43da26678ee77412a30050a


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
<<<<<<< HEAD
    """Création d avis de collection physique réussie"""

    # GIVEN
    avis = Avis(note=5, avis="excelent synopsis")

    # WHEN
    creation_ok = DaoAvis().creer_avis_collection_physique(
        id_utilisateur=43, id_collection=1, avis_collection_physique=avis, schema="projet_test_dao"
=======
    """Création d'avis de collection physique réussie."""
    # GIVEN
    avis = Avis(note=5, avis="excellent")
    # WHEN
    creation_ok = DaoAvis().creer_avis_collection_physique(
        id_utilisateur=12, id_collection=13, avis_collection_physique=avis, schema="projet_test_dao"
>>>>>>> ec1c0aa147163376a43da26678ee77412a30050a
    )
    # THEN
    assert creation_ok


<<<<<<< HEAD
def test_supprimer_ok():
    """Suppression d'un avis réussie"""

    # GIVEN

    # WHEN
    suppression_ok = DaoAvis().supprimer_avis(
        schema="projet_test_dao",
        id_avis=DaoAvis().trouver_id_avis_par_id_manga_utilisateur(
            schema="projet_test_dao", id_manga=1, id_utilisateur=12
        ),
    )

    # THEN
    assert suppression_ok
=======
def test_chercher_avis_sur_manga():
    """Recherche des avis laissés sur un manga."""
    avis = Avis(note=5, avis="cool", id_avis=26)
    avis_a_verifier = DaoAvis().chercher_avis_sur_manga("projet_test_dao", id_manga=1)
    assert avis in avis_a_verifier
>>>>>>> ec1c0aa147163376a43da26678ee77412a30050a


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
