class Manga:
    """
    Classe représentant un manga de l'API

    Attributs
    ----------
    id_manga : int
        identifiant du manga
    titre : str
        titre du manga
    id_jikan : int
        identifiant jikan du manga
    """

    def __init__(self, titre, auteurs, genres, status, nombre_chapitres, id_manga=None):
        """Constructeur"""
        self.id_manga = id_manga
        self.titre = titre
        self.auteurs = auteurs
        self.genres = genres
        self.status = status
        self.nombre_chapitres = nombre_chapitres

    def __str__(self):
        """Permet d'afficher les informations du manga"""
        return f"Le titre du manga est ({self.titre})"
