from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite

# from service.manga_service import MangaService


class RechercheUtilisateurVue(VueAbstraite):
    "Vue de la barre de recherche de mangas"

    def choisir_menu(self):
        """Choix du manga à consulter

        Return
        ------
        view
            Retourne les details associer au manga chioisi
        """

        print("\n" + "-" * 50 + "\nRecherche de l'utilisateur par son nom\n" + "-" * 50 + "\n")

        utilisateur = inquirer.text(
            message="Donner le nom de l'utilisateur à trouver"
        ).execute()

        print(utilisateur)

        return utilisateur
