from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from service.collection_service import ServiceCollection


class CollectionCoherenteVue(VueAbstraite):
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
            print("Mangas de la collection:")

            liste_mangas = ServiceCollection().lister_mangas_collection(
                self.collection.id_collection, "projet_info_2a"
            )
            for manga in liste_mangas:
                print(manga.titre)

        choix = inquirer.select(
            message="Choississez une action à réaliser",
            choices=[
                "Gérer ses avis sur la collection",
                "Retourner au menu de recherche d'utilisateur",
            ],
        ).execute()

        match choix:
            case "Gérer ses avis sur la collection":
                return 0

            case "Retourner au menu de recherche d'utilisateur":
                from view.passif.recherche_utilisateur_vue import RechercheUtilisateurVue

                return RechercheUtilisateurVue().choisir_menu()
