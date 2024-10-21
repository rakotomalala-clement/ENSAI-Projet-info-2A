from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class GestionCollectionVue(VueAbstraite):
    "Vue de la page de gestion de ses collections"

    def choisir_menu(self):
        """Gestion des collections

        Return
        ------
        view
            Retourne un menu permettant à l'utilisateur de se connecter
        """

        print("\n" + "-" * 50 + "\nGestionnaire de collection\n" + "-" * 50 + "\n")

        nom_collection = inquirer.text(
            message="Veuillez saisir le nom de la collection à accéder"
        ).execute()

        print(nom_collection)

        return 0
