import pytest
from business_object.avis import Avis
from dao.avis_dao import DaoAvis

DaoAvis().supprimer_avis(
    schema="projet_test_dao",
    id_avis=DaoAvis().trouver_id_avis_par_id_manga_utilisateur(
        schema="projet_test_dao", id_manga=1, id_utilisateur=12
    ),
)
DaoAvis().supprimer_avis_col_coherente(id_avis_collection_coherente=5, schema="projet_test_dao")


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


def test_chercher_avis():
    """Recherche des avis laisser par un utilisateur sur un manga"""

    # GIVEN

    # WHEN
    listeavis = DaoAvis().chercher_avis(id_utilisateur=1, id_manga=4)

    # THEN
    assert isinstance(listeavis, list)
    for a in listeavis:
        assert isinstance(a, Avis)


def test_modifier_avis_ok():
    avis = Avis(note=5, avis="cool")
    avis_originelle = DaoAvis().creer_avis(
        "projet_test_dao", id_utilisateur=1, id_manga=1, avis_manga=avis
    )

    modification = DaoAvis().modifier_avis(
        "projet_test_dao",
        avis=Avis(id_avis=avis_originelle.id_avis, avis="Superbe manga !", note=4),
    )

    assert avis_originelle.avis != modification.avis
    assert avis_originelle.note != modification.note


if __name__ == "__main__":
    pytest.main([__file__])
