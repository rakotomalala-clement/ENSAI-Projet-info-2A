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

                return "2"

            case "Créer un compte":

                return "3"

            case "Rechercher manga":

                return "4"

            case "Rechercher collection":

                return "5"


if __name__ == "__main__":
    print(AccueilVue().choisir_menu())
