from unittest.mock import MagicMock

from service.manga_service import MangaService

from dao.manga_dao import MangaDao

from business_object.manga import Manga


liste_manga = [
    Manga(
        id_manga=99999999999,
        titre="Berserk",
        auteurs=["Miura", "Kentarou"],
        genres="Adventure",
        status="Publishing",
        nombre_chapitres=None,
    ),
]


def test_ajouter_manga():
    """ "Création de Joueur réussie"""

    # GIVEN

    # WHEN

    # THEN
    assert


def test_ajouter_manga_echec():
    """Création de Manga échouée
    (car la méthode JoueurDao().creer retourne False)"""

    # GIVEN

    # WHEN

    # THEN
    assert
