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

        liste_mangas = MangaService().lister_mangas()
        liste_nom_mangas = []
        for manga in liste_mangas:
            liste_nom_mangas.append(manga.titre)

        titre = inquirer.fuzzy(
            message="Quel manga souhaitez-vous consulter?", choices=liste_nom_mangas
        ).execute()

        return AffichageMangaVue(titre).choisir_menu()


if __name__ == "__main__":
    RechercheMangaVue().choisir_menu()
