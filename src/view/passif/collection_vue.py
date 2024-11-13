# from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite

# from view.passif.accueil_vue import AccueilVue
# from view.actif.accueil_connecte_vue import AccueilConnecteVue

# from view.passif.connexion.session import Session


class CollectionVue(VueAbstraite):
    "Vue de l' affichage d'une collection"

    def __init__(self, collection):
        self.collection = collection

    def choisir_menu(self):
        """Affichage de la collection souhaité

        Return
        ------
        view
            Retourne les details associer à la collection choisi
        """

        print("\n" + "-" * 50 + "\nCollection:", self.collection.titre, "\n" + "-" * 50 + "\n")

        if self.collection.type_collection == "Cohérente":
            print(self.collection.description)

        return 0
