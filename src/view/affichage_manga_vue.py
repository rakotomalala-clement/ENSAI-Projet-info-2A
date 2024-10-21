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

        auteur1 = manga.auteurs[0]
        status = manga.status

        print(auteur1)
        print(status)

        return self.titre
