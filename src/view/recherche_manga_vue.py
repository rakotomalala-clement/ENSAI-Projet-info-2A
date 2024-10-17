from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite

# from service.manga_service import MangaService


class RechercheMangaVue(VueAbstraite):
    "Vue de la barre de recherche de mangas"

    def choisir_menu(self):
        """Choix du manga à consulter

        Return
        ------
        view
            Retourne les details associer au manga chioisi
        """

        print("\n" + "-" * 50 + "\nRecherche de manga par titre\n" + "-" * 50 + "\n")

        titre = inquirer.text(
            message="Donner le nom du manga que vous souhaitez rechercher"
        ).execute()

        print(titre)

        return titre
