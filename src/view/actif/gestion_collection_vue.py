from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class GestionCollectionVue(VueAbstraite):
    "Vue de la page de gestion de ses collections"

    def choisir_menu(self):
        """Gestion des collections

        Return
        ------
        view
            Retourne un menu permettant à l'utilisateur de gérer ses collections
        """

        print("\n" + "-" * 50 + "\nGestionnaire de collection\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Voulez-vous créer ou modifier une de vos collections?",
            choices=[
                "Créer collection",
                "Modifier collection",
            ],
        ).execute()

        match choix:
            case "Créer collection":
                print("coucou")

            case "Modifier collection":
                print("oucouc")

        return 0
