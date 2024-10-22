# from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class AffichageMangaVue(VueAbstraite):
    "Vue des informations sur le manga"

    def __init__(self, titre):
        self.titre = titre

    def choisir_menu(self):
        """Affichage des details du manga

        Return
        ------
        view
            Retourne la view de l'acceuil
        """

        print("\n" + "-" * 50 + "\nDétails du manga\n" + "-" * 50 + "\n")

        print(self.titre)

        # Instanciation de notre objet Manga
        from service.manga_service import MangaService

        manga = MangaService().trouver_par_titre(self.titre)

        auteurs = manga.auteurs
        status = manga.status

        print(auteurs)
        print(status)

        return self.titre
