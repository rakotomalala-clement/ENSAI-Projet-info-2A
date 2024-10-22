from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class GestionCollectionVue(VueAbstraite):
    "Vue de la page de création de collection"

    def choisir_menu(self):
        """Création de collection

        Return
        ------
        view
            Retourne un menu permettant à l'utilisateur de créer une collection
        """

        print("\n" + "-" * 50 + "\nCréation de collection\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Voulez-vous créer une collection physique ou cohérente?",
            choices=["Collection physique, Collection cohérente"],
        ).execute()

        match choix:
            case "Collection physique":
                print("cococo")

            case "Collection cohérente":
                print("cecece")

        return 0
