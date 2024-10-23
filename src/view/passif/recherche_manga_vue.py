from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.affichage_manga_vue import AffichageMangaVue
from service.manga_service import MangaService


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

        print("Voici une liste de mangas que vous pouvez rechercher")

        liste_mangas = MangaService().lister_mangas()
        for indice_manga in range(3):
            print(liste_mangas[indice_manga].titre)

        titre = inquirer.text(
            message="Donner le nom du manga que vous souhaitez rechercher"
        ).execute()

        return AffichageMangaVue(titre).choisir_menu()


if __name__ == "__main__":
    RechercheMangaVue().choisir_menu()
