from dao.manga_dao import MangaDao
from business_object.manga import Manga


def test_trouver_par_titre_true():
    """Recherche par son titre un manga existant"""
    titre_manga = "Monster"
    manga = MangaDao().trouver_par_titre(titre_manga)
    assert manga is not None, f"Le manga avec le titre '{titre_manga}' devrait exister."


def test_trouver_par_titre_false():
    """Recherche par son titre un manga n'existant pas"""
    titre_manga = "blabla"
    manga = MangaDao().trouver_par_titre(titre_manga)
    assert manga is None, f"Le manga avec le titre '{titre_manga}' ne devrait pas exister."


def test_trouver_id_par_titre_true():
    """Recherche par son titre l'id d'un manga existant"""
    titre_manga = "Monster"
    id_manga = MangaDao().trouver_id_par_titre(titre_manga)
    assert id_manga is not None, f"L'id du manga avec le titre '{titre_manga}' devrait exister."


def test_trouver_id_par_titre_false():
    """Recherche par son titre l'id d'un manga n'existant pas"""
    titre_manga = "blabla"
    id_manga = MangaDao().trouver_id_par_titre(titre_manga)
    assert id_manga is None, f"L'id du manga avec le titre '{titre_manga}' ne devrait pas exister."


def test_lister_manga():
    """Vérifie que la méthode renvoie une liste de Manga de taille supérieure ou égale à 1"""
    mangas = MangaDao().lister_manga()
    assert isinstance(mangas, list), "Le résultat de la méthode devrait être une liste."
    assert len(mangas) >= 1, "La liste des mangas devrait contenir au moins un élément."
    for j in mangas:
        assert isinstance(
            j, Manga
        ), "Chaque élément de la liste devrait être une instance de Manga."


def test_ajouter_manga_true():
    """Ajout d'un manga réussie et vérifie la suppression après le test"""
    manga = Manga(
        titre="Ensaimangaaaa",
        auteurs=["groupe 211"],
        genres="Actionn",
        status="Publishingg",
        nombre_chapitres=0,
    )
    creation = MangaDao().ajouter_manga(manga)
    assert creation, "L'ajout du manga devrait réussir."

    # Nettoyage : suppression du manga ajouté pour éviter de polluer la base de données.
    suppression = MangaDao().supprimer_manga(manga)
    assert suppression, "Le manga ajouté devrait être supprimé après le test."


def test_supprimer_manga_ok():
    """Suppression de Manga réussie"""
    manga = MangaDao().trouver_par_titre("Berserk")
    assert manga is not None, "Le manga 'Berserk' devrait exister avant la suppression."

    suppression = MangaDao().supprimer_manga(manga)
    assert suppression, "La suppression du manga 'Berserk' devrait réussir."


def test_supprimer_ko():
    """Suppression de Manga échoué (titre inconnu)"""
    titre_manga = "blabla"
    manga = MangaDao().trouver_par_titre(titre_manga)
    assert manga is None, "Le manga avec le titre 'blabla' devrait être introuvable."

    # Essayer de supprimer un manga inexistant
    suppression = MangaDao().supprimer_manga(manga) if manga else False
    assert not suppression, "La suppression d'un manga inexistant ne devrait pas réussir."
