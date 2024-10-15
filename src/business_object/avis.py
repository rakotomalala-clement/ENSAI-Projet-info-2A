class Avis:
    """Modélisation de l'objet Avis

    La classe Avis caractérise les avis que les utilisateur actif pourrons
    écrire afin de commenter et noter un manga ou une collection.

    Parameters:
    -----------

    avis: str
        Chaine de caractère écrite par un utilisateur pour commenter un manga
        ou une collection

    note: int
        Entier compris entre 1 et 5 qui permet a l'utilisateur de quantifier
        son niveau de satisfaction sur un manga ou une collection

    """

    def __init__(self, id_avis: int, avis: str, note: int):
        self.avis = avis
        self.note = note
        self.id_avis = id_avis

    def __str__(self):
        """Permet d'afficher les informations d'un avis'"""
        return f"Note : {self.note}, Avis : {self.avis}"
