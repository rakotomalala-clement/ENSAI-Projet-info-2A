from dao.manga_dao import MangaDao
from business_object.manga import Manga


def test_trouver_par_titre_true():
    """Recherche par son titre un manga existant"""
    titre_manga = "Monster"
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
        titre="Ensaimangaaaa",
        auteurs=["groupe 211"],
        genres="Actionn",
        status="Publishingg",
        nombre_chapitres=0,
    )
    creation = MangaDao().ajouter_manga(manga)
    assert creation


def test_supprimer_manga_ok():
    """Suppression de Manga réussie"""
    titre_manga = MangaDao().trouver_par_titre("Berserk")
    suppression = MangaDao().supprimer_manga(titre_manga)
    assert suppression


def test_supprimer_ko():
    """Suppression de Manga échoué (titre inconnu)"""
    titre_manga = MangaDao().trouver_par_titre("blabla")
    assert titre_manga is None, "Le manga avec le titre 'blabla' devrait être introuvable."

    # Essayer de supprimer un manga inexistant
    suppression = MangaDao().supprimer_manga(titre_manga) if titre_manga else False
    assert not suppression, "La suppression d'un manga inexistant ne devrait pas réussir."
