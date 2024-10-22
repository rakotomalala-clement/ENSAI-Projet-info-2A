from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class MangaCollectionVue(VueAbstraite):
    """Menu des modifications possibles sur un manga au sein d'une collection"""

    def __init__(self, type_collection, titre_manga=None):
        # titre de la collection
        self.type_collection = type_collection
        self.titre_manga = titre_manga
        # le type de la collection

    def choisir_menu(self):
        """Choix du menu suivant sachant que l'on a sélectionné un manga dans une collection

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\n", self.titre_manga, "\n" + "-" * 50 + "\n")

        if self.type_collection == "cohérente":
            possibilites = [
                "Changer le statut de lecture du manga",
                "Ajouter un tome au manga",
                "Supprimer le manga",
                "Quitter",
            ]
        else:
            possibilites = ["Supprimer le manga", "Quitter"]

        choix = inquirer.select(
            message="Choississez une action à réaliser",
            choices=possibilites,
        ).execute()

        match choix:
            case "Changer le statut de lecture du manga":
                return 0
            case "Ajouter un tome au manga":
                return 0
            case "Supprimer le manga":
                return 0
            case "Quitter":
                pass
