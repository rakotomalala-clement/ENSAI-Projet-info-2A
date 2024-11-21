import pytest
from business_object.avis import Avis
from dao.avis_dao import DaoAvis
from dao.collection_dao import DaoCollection


def test_trouver_id_avis_par_id_manga_utilisateur_true():
    """Recherche par l'id d'un manga/utilisateur l'id d'un avis existant."""
    id_manga = 4
    id_utilisateur = 12
    id_avis = DaoAvis().trouver_id_avis_par_id_manga_utilisateur(
        "projet_test_dao", id_manga, id_utilisateur
    )
    assert id_avis == 2


def test_trouver_id_avis_par_id_manga_utilisateur_false():
    """Recherche l'id d'un avis par l'id d'un manga/utilisateur non existant."""
    id_manga = 111111
    id_utilisateur = 11111111
    id_avis = DaoAvis().trouver_id_avis_par_id_manga_utilisateur(
        "projet_test_dao", id_manga, id_utilisateur
    )
    assert id_avis is None


def test_trouver_id_avis_collection_coherent_par_id_collection_co_utilisateur_true():
    """Recherche de l'id d'un avis sur  une collection coherente existant
    par l'id de la collection et de l'utilisateur."""
    id_collection_coherente = 2
    id_utilisateur = 12
    id_avis_col_co = DaoAvis().trouver_id_avis_par_id_col_coherente_utilisateur(
        "projet_test_dao",
        id_collection_coherente=id_collection_coherente,
        id_utilisateur=id_utilisateur,
    )
    assert id_avis_col_co == 971


def test_trouver_id_avis_collection_coherent_par_id_collection_co_utilisateur_false():
    """Recherche de l'id d'un avis sur  une collection coherente non existant
    par l'id de la collection et de l'utilisateur."""
    id_collection_coherente = 1234
    id_utilisateur = 1234
    id_avis_col_co = DaoAvis().trouver_id_avis_par_id_col_coherente_utilisateur(
        "projet_test_dao",
        id_collection_coherente=id_collection_coherente,
        id_utilisateur=id_utilisateur,
    )
    assert id_avis_col_co is None


def test_trouver_id_avis_collection_physique_par_id_collection_phy_utilisateur_true():
    """Recherche de l'id d'un avis sur  une collection physique existant
    par l'id de la collection et de l'utilisateur."""
    id_collection_physique = 1
    id_utilisateur = 12
    id_avis_col_phy = DaoAvis().trouver_id_avis_par_id_manga_utilisateur_col_physique(
        "projet_test_dao",
        id_collection=id_collection_physique,
        id_utilisateur=id_utilisateur,
    )
    assert id_avis_col_phy == 971


def test_trouver_id_avis_collection_physique_par_id_collection_phy_utilisateur_false():
    """Recherche de l'id d'un avis sur  une collection physique existant
    par l'id de la collection et de l'utilisateur."""
    id_collection_physique = 1234
    id_utilisateur = 1234
    id_avis_col_phy = DaoAvis().trouver_id_avis_par_id_manga_utilisateur_col_physique(
        "projet_test_dao",
        id_collection=id_collection_physique,
        id_utilisateur=id_utilisateur,
    )
    assert id_avis_col_phy is None


def test_creer_avis_ok():
    """Création d'avis réussie."""
    # GIVEN
    avis = Avis(note=4, avis="cool cool")
    # WHEN
    creation_ok = DaoAvis().creer_avis(
        id_utilisateur=12, id_manga=1, avis=avis, schema="projet_test_dao"
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


def test_afficher_avis_collection_coherente_ok():
    "chercher avis sur collection cohérente ok"
    nb_avis_col_co = 2
    avis_col_co = DaoAvis().chercher_avis_sur_collection_coherente(
        schema="projet_test_dao", id_collection_coherente=1
    )
    assert nb_avis_col_co == len(avis_col_co)


def test_afficher_avis_user_sur_collection_coherente_ok():
    "chercher l'avis d'un utilisateur sur collection cohérente ok"
    id_avis = DaoAvis().trouver_id_avis_par_id_col_coherente_utilisateur(
        id_utilisateur=12,
        id_collection_coherente=1,
        schema="projet_test_dao",
    )
    avis_col_co = DaoAvis().chercher_avis_user_sur_collection_coherente(
        schema="projet_test_dao", id_utilisateur=12, id_collection_coherente=1
    )
    assert id_avis == avis_col_co.id_avis


def test_modifier_avis_col_co_ok():
    """Modification d'un avis d'un collection coherente existant."""

    # WHEN
    modification = DaoAvis().modifier_avis_collection_co(
        "projet_test_dao",
        avis=Avis(
            id_avis=DaoAvis().trouver_id_avis_par_id_col_coherente_utilisateur(
                schema="projet_test_dao", id_collection_coherente=1, id_utilisateur=12
            ),
            avis="moyen",
            note=3,
        ),
        id_collection=1,
        id_utilisateur=12,
    )

    # THEN
    assert modification is True


def test_creer_avis_col_physique_ok():
    """Création d avis de collection physique réussie"""

    # GIVEN
    avis = Avis(note=5, avis="excelent synopsis")

    # WHEN
    creation_ok = DaoAvis().creer_avis_collection_physique(
        id_utilisateur=43, id_collection=1, avis_collection_physique=avis, schema="projet_test_dao"
    )
    # THEN
    assert creation_ok


def test_afficher_avis_collection_physique_ok():
    "chercher avis sur collection physique ok"
    nb_avis_col_phy = 2
    avis_col_phy = DaoAvis().chercher_avis_sur_collection_physique(
        schema="projet_test_dao", id_collection=1
    )
    assert nb_avis_col_phy == len(avis_col_phy)


def test_afficher_avis_user_sur_collection_physique_ok():
    "chercher avis d'un utilisateur sur collection physique ok"
    id_avis = DaoAvis().trouver_id_avis_par_id_manga_utilisateur_col_physique(
        id_utilisateur=43, id_collection=1, schema="projet_test_dao"
    )
    avis_col_phy = DaoAvis().chercher_avis_user_sur_collection_physique(
        schema="projet_test_dao", id_utilisateur=43, id_collection=1
    )
    assert id_avis == avis_col_phy.id_avis


def test_modifier_avis_col_phy_ok():
    """Modification d'un avis d'une collection physique existant."""

    # WHEN
    modification = DaoAvis().modifier_avis_collection_phy(
        "projet_test_dao",
        avis=Avis(
            id_avis=DaoAvis().trouver_id_avis_par_id_manga_utilisateur_col_physique(
                schema="projet_test_dao", id_collection=1, id_utilisateur=43
            ),
            avis="moyen",
            note=3,
        ),
        id_collection=1,
        id_utilisateur=43,
    )
    # THEN
    assert modification is True


def test_modifier_avis_ok():
    """Modification d'un avis existant."""

    # WHEN
    modification = DaoAvis().modifier_avis(
        "projet_test_dao",
        avis=Avis(
            id_avis=DaoAvis().trouver_id_avis_par_id_manga_utilisateur(
                schema="projet_test_dao", id_manga=1, id_utilisateur=12
            ),
            avis="ok",
            note=3,
        ),
        id_manga=1,
        id_utilisateur=12,
    )

    # THEN
    assert modification is True, "La modification de l'avis devrait retourner True"


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


def test_chercher_avis():
    """Recherche de l'avis laissés par un utilisateur sur un manga."""
    avis = Avis(note=5, avis="test_", id_avis=2)
    avis_a_verifier = DaoAvis().chercher_avis("projet_test_dao", id_utilisateur=12, id_manga=4)
    assert [avis] == avis_a_verifier


def test_chercher_avis_sur_manga():
    """Recherche de l'ensemble des avis laissés  sur un manga."""
    nb_avis_sur_manga_4 = 2
    avis_sur_4 = DaoAvis().chercher_avis_sur_manga("projet_test_dao", id_manga=4)
    assert nb_avis_sur_manga_4 == len(avis_sur_4)


def test_supprimer_avis_col_coherente_ok():
    """suppression d'un avis sur collection coherente"""
    suppression = DaoAvis().supprimer_avis_col_coherente(
        id_avis_collection_coherente=DaoAvis().trouver_id_avis_par_id_col_coherente_utilisateur(
            "projet_test_dao", 1, 12
        ),
        schema="projet_test_dao",
    )
    assert suppression


def test_supprimer_avis_col_physique_ok():
    """suppression d'un avis sur collection coherente"""
    suppression = DaoAvis().supprimer_avis_col_physique(
        id_avis_collection_physique=DaoAvis().trouver_id_avis_par_id_manga_utilisateur_col_physique(
            schema="projet_test_dao", id_collection=1, id_utilisateur=43
        ),
        schema="projet_test_dao",
    )
    assert suppression


if __name__ == "__main__":
    pytest.main([__file__])
