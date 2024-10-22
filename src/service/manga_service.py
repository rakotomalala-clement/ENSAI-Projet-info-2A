from utils.log_decorator import log
from business_object.manga import Manga
from dao.manga_dao import MangaDao


class MangaService:
    """Classe contenant les méthodes de service de la classe Manga"""

    @log
    def ajouter_manga(self, titre, auteurs, genres, status, nombre_chapitres) -> Manga:
        """Ajout d'un manga à partir de ses attributs.

        Parameters
        ----------
        titre : str
            Titre du manga à ajouter.
        auteurs : str
            Auteurs du manga.
        genres : str
            Genres du manga.
        status : str
            Statut du manga (publishing ou finished).
        chapitres : int
            Nombre de chapitres du manga.

        Returns
        -------
        Manga
            Le manga ajouté, ou None si l'ajout a échoué.

        """
        # Création de l'objet Manga avec tous les attributs fournis
        manga = Manga(
            titre=titre,
            auteurs=auteurs,
            genres=genres,
            status=status,
            nombre_chapitres=nombre_chapitres,
        )

        # Utiliser le DAO pour ajouter le manga
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
    def trouver_id_par_titre(self, titre: str) -> int:
        """Trouver l'id d'un manga à partir de son titre.

        Parameters
        ----------
        titre : str
            Titre du manga à rechercher.

        Returns
        -------
        id_manga : int
            L'id du manga trouvé, ou None si aucun manga ne correspond au titre.
        """
        return MangaDao().trouver_id_par_titre(titre)

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
