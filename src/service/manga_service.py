from utils.log_decorator import log
from business_object.manga import Manga
from dao.manga_dao import MangaDao


class MangaService:
    """Classe contenant les méthodes de service de la classe Manga"""

    @log
    def ajouter_manga(self, titre: str, id_jikan: int) -> Manga:
        """Ajout d'un manga à partir de ses attributs.

        Parameters
        ----------
        titre : str
            Titre du manga à ajouter.
        id_jikan : int
            ID associé au manga.

        Returns
        -------
        Manga
            Le manga ajouté, ou None si l'ajout a échoué.
        """
        manga = Manga(titre=titre, id_jikan=id_jikan)
        if MangaDao().ajouter_manga(manga):
            return manga
        return None

    @log
    def lister_mangas(self) -> list[Manga]:
        """Lister des mangas.

        Returns
        -------
        list[Manga]
            La liste des mangas.
        """
        return MangaDao().lister_manga()

    @log
    def trouver_par_titre(self, titre: str) -> Manga:
        """Trouver un manga à partir de son titre.

        Parameters
        ----------
        titre : str
            Titre du manga à rechercher.

        Returns
        -------
        Manga
            Le manga trouvé, ou None si aucun manga ne correspond au titre.
        """
        return MangaDao().trouver_par_titre(titre)

    @log
    def supprimer_manga(self, manga: Manga) -> bool:
        """Supprimer un manga.

        Parameters
        ----------
        manga : Manga
            Le manga à supprimer.

        Returns
        -------
        bool
            True si le manga a été supprimé, False sinon.
        """
        return MangaDao().supprimer_manga(manga)
