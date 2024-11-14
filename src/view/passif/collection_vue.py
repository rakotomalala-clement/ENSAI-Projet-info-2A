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

        # liste_avis = ServiceAvis().
        # if liste_avis is None:
        #     print("")
        # else:
        #     for avis in liste_avis:
        #         print("Note: ", avis.note, ", ", avis.avis)

        if self.collection.type_collection == "Cohérente":
            print(self.collection.description)
            print("Mangas de ma collection:")
            from collection_service import ServiceCollection

            # liste_mangas = ServiceCollection().
            # for manga in liste_mangas:
            # print(manga.titre)

        else:
            # On veut prendre une collection physique
            # Dans cette collection physique,

        return 0
