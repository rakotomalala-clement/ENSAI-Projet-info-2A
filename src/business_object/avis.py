class Avis:
    """Modélisation de l'objet Avis

    La classe Avis caractérise les avis que les utilisateurs actifs peuvent
    écrire afin de commenter et noter un manga ou une collection.

    Parameters:
    -----------
    note : int
        Entier compris entre 1 et 5 qui permet à l'utilisateur de quantifier
        son niveau de satisfaction sur un manga ou une collection.
    avis : str
        Chaîne de caractères écrite par un utilisateur pour commenter un manga
        ou une collection.
    id_avis : int, optional
        Identifiant unique de l'avis. Si non spécifié, sa valeur est None.
    """

    def __init__(self, note: int, avis: str, id_avis: int = None):

        if not isinstance(avis, str):
            raise TypeError("avis doit être un str")
        if not isinstance(note, int):
            raise TypeError("note doit être un entier")
        if note < 1 or note > 5:
            raise ValueError("La note doit être comprise entre 1 et 5.")

        self.note = note
        self.avis = avis
        self.id_avis = id_avis

    def __eq__(self, other):
        if isinstance(other, Avis):
            return (
                self.id_avis == other.id_avis
                and self.avis == other.avis
                and self.note == other.note
            )
        return False

    def __str__(self):
        """Permet d'afficher les informations d'un avis."""
        return f"Note : {self.note}, Avis : {self.avis}"


# Test de la classe Avis

# Test de la création d'un avis valide
# try:
#    avis1 = Avis(note=4, avis="Un manga très intéressant et bien illustré.")
#    print(
#        avis1
#    )  # Devrait afficher : "Note : 4, Avis : Un manga très intéressant et bien illustré."
# except ValueError as e:
#    print(f"Erreur : {e}")

# Test de la création d'un avis avec une note invalide
# try:
#    avis2 = Avis(note=6, avis="Excellent manga mais note incorrecte.")
# except ValueError as e:
#    print(
#        f"Erreur : {e}"
#    )  # Devrait afficher une erreur : "La note doit être comprise entre 1 et 5."

# Test de la création d'un avis avec un identifiant
# avis3 = Avis(note=3, avis="Sympa, mais sans plus.", id_avis=101)
# print(avis3)  # Devrait afficher : "Note : 3, Avis : Sympa, mais sans plus."
