# from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session


class RechercheCollection(VueAbstraite):
    "Vue de la barre de recherche de mangas"

    def choisir_menu(self):
        """Choix du manga à consulter

        Return
        ------
        view
            Retourne les details associer au manga chioisi
        """

        print(
            "\n" + "-" * 50 + "\nCollection de", Session().nom_utilisateur, "\n" + "-" * 50 + "\n"
        )

        # liste des collections de l'utilisateur

        return 0
