import os
import pytest
from unittest.mock import patch
from utils.reset_database import ResetDatabase
from dao.manga_dao import MangaDao
from business_object.manga import Manga


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        ResetDatabase().lancer(test_dao=True)
        yield


def test_trouver_par_titre_true():
    """Recherche par son titre un manga existant"""
    titre_manga = "Naruto"
    manga = MangaDao().trouver_par_titre(titre_manga)
    assert manga is not None


def test_trouver_par_titre_false():
    """Recherche par son titre un manga n'existant pas"""
    titre_manga = "blabla"
    manga = MangaDao().trouver_par_titre(titre_manga)
    assert manga is None


def test_lister_manga():
    """Vérifie que la méthode renvoie une liste de Manga de taille supérieure ou égale à 1"""
    mangas = MangaDao().lister_manga()
    assert isinstance(mangas, list)
    for j in mangas:
        assert isinstance(j, Manga)
    assert len(mangas) >= 1


def test_ajouter_manga_true():
    """Ajout d'un manga réussie"""
    manga = Manga(
        id_manga=1000,
        titre="Ensaimanga",
        auteurs=["groupe 21"],
        genres="Action",
        status="Publishing",
        nombre_chapitres=0,
    )
    creation = MangaDao().ajouter_manga(manga)
    assert creation


def test_supprimer_manga_ok():
    """Suppression de Manga réussie"""
    manga = Manga(
        id_manga=2,
        titre="Berserk",
        auteurs=["Miura", "Kentarou"],
        genres="Adventure",
        status="Publishing",
        nombre_chapitres=0,
    )
    suppression = MangaDao().supprimer_manga(manga)
    assert suppression


def test_supprimer_ko():
    """Suppression de Manga échoué (id inconnu)"""
    manga = Manga(
        id_manga=99999999999,
        titre="Berserk",
        auteurs=["Miura", "Kentarou"],
        genres="Adventure",
        status="Publishing",
        nombre_chapitres=0,
    )
    suppression = MangaDao().supprimer_manga(manga)
    assert not suppression
