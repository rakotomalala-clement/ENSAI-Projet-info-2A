class MangaDansCollection:
    def __init__(
        self, manga, dernier_tome_acquis, numeros_tomes_manquants, status_manga
    ):
        self.manga = manga
        self.dernier_tome_acquis = dernier_tome_acquis
        self.numeros_tomes_manquants = numeros_tomes_manquants
        self.status_manga = status_manga
