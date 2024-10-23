from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session
from view.passif.accueil_vue import AccueilVue


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

        print("auteur(s): ", auteurs)
        print("Etat de la diffusion du manga: ", status)

        if Session().connecte:
            possibilites = ["Gérer ses avis sur ce manga", "Revenir au menu principal", "Quitter"]
        else:
            possibilites = ["Revenir au menu principal", "Quitter"]

        choix = inquirer.select(message="", choices=possibilites).execute()

        match choix:
            case "Gérer ses avis sur ce manga":
                return 0
            case "Revenir au menu principal":
                return AccueilVue().choisir_menu()
            case "Quitter":
                pass
