from utils.log_decorator import log
from business_object.manga import Manga
from dao.manga_dao import MangaDao


class MangaService:
    """Classe contenant les méthodes de service de la classe Manga"""

    @log
    def ajouter_manga(self, titre, id_jikan) -> Manga:
        """Ajout d'un manga à partir de ses attributs"""

        return

    @log
    def lister_mangas(self) -> list[Manga]:
        """Lister des mangas"""
        mangas = MangaDao().lister_mangas()
        return mangas

    @log
    def trouver_par_titre(self, titre) -> Manga:
        """Trouver un manga à partir de son titre"""
        return MangaDao().trouver_par_titre(titre)

    @log
    def supprimer_manga(self, manga) -> bool:
        """Supprimer le compte d'un joueur"""
        return MangaDao().supprimer_manga(manga)
