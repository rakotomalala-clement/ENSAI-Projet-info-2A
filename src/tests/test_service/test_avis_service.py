import pytest

from service.avis_service import ServiceAvis


def test_validation_avis_invalide_ok():
    avis = "tu es une merde"
    invalide = ServiceAvis().Validation_avis(message_avis=avis)
    assert invalide is False


def test_validation_avis_valide_ok():
    avis = "convenable"
    invalide = ServiceAvis().Validation_avis(message_avis=avis)
    assert invalide is True


if __name__ == "__main__":

    pytest.main([__file__])

"""
from dao.avis_dao import DaoAvis

from business_object.avis import Avis

DaoAvis().supprimer_avis(
    schema="projet_test_dao",
    id_avis=DaoAvis().trouver_id_avis_par_id_manga_utilisateur(
        schema="projet_test_dao", id_manga=1, id_utilisateur=12
    ),
)
DaoAvis().supprimer_avis_col_coherente(
    id_avis_collection_coherente=DaoAvis().trouver_id_avis_par_id_col_coherente_utilisateur(
        "projet_test_dao", id_collection_coherente=1, id_utilisateur=12
    ),
    schema="projet_test_dao",
)
DaoAvis().supprimer_avis_col_physique(
    id_avis_collection_physique=DaoAvis().trouver_id_avis_par_id_manga_utilisateur_col_physique(
        schema="projet_test_dao", id_collection=1, id_utilisateur=12
    ),
    schema="projet_test_dao",
)


def test_ajouter_avis_ok():
    Création d'un avis réussie

    # GIVEN
    note, avis = 5, "super cool"

    # WHEN
    nouveau_avis = ServiceAvis().ajouter_avis(12, 1, avis, note, "projet_test_dao")

    # THEN
    assert nouveau_avis.avis == avis
    assert nouveau_avis.note == note


def test_ajouter_avis_collection_physique():

    note_p, avis_p = 5, "super cool comme collection physique"

    avis_collection_physique = ServiceAvis().ajouter_avis_collection(
        id_utilisateur=12,
        id_collection=1,
        type_collection="physique",
        avis=avis_p,
        note=note_p,
        schema="projet_test_dao",
    )

    assert avis_collection_physique.avis == avis_p


def test_ajouter_avis_collection_coherente():

    note_c, avis_c = 5, "super cool comme collection cohérente"

    avis_collection_coherente = ServiceAvis().ajouter_avis_collection(
        id_utilisateur=12,
        id_collection=1,
        type_collection="coherente",
        avis=avis_c,
        note=note_c,
        schema="projet_test_dao",
    )

    assert avis_collection_coherente.avis == avis_c




"""
