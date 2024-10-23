from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class CreerCollectionVue(VueAbstraite):
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
            choices=["Collection physique", "Collection cohérente"],
        ).execute()

        nom_collection = inquirer.text(message="Quel est le nom de votre collection?").execute()

        match choix:
            case "Collection physique":
                print("cococo", nom_collection)

                from view.actif.accueil_connecte_vue import AccueilConnecteVue

                return AccueilConnecteVue().choisir_menu()

            case "Collection cohérente":
                print("cecece")

                from view.actif.accueil_connecte_vue import AccueilConnecteVue

                return AccueilConnecteVue().choisir_menu()

        return 0
