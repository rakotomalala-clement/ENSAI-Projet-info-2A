from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class AccueilVue(VueAbstraite):
    """Vue d'accueil de l'application"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nAccueil\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Se connecter",
                "Créer un compte",
                "Rechercher manga",
                "Rechercher utilisateur",
                "Quitter",
            ],
        ).execute()

        match choix:
            case "Quitter":
                pass

            case "Se connecter":
                from view.passif.connexion.connexion_vue import ConnexionVue

                return ConnexionVue().choisir_menu()

            case "Créer un compte":
                from view.passif.connexion.inscription_vue import InscriptionVue

                return InscriptionVue().choisir_menu()

            case "Rechercher manga":
                from view.passif.recherche_manga_vue import RechercheMangaVue

                return RechercheMangaVue().choisir_menu()

            case "Rechercher utilisateur":
                from view.passif.recherche_utilisateur_vue import RechercheUtilisateurVue

                return RechercheUtilisateurVue().choisir_menu()


if __name__ == "__main__":
    AccueilVue().choisir_menu()
