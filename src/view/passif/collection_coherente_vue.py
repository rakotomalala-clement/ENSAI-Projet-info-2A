from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from service.collection_service import ServiceCollection
from service.avis_service import ServiceAvis


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

        liste_avis = ServiceAvis().afficher_avis_user(self.collection.id_collection)
        if liste_avis is None:
            print("")
        else:
            for avis in liste_avis:
                print("Note: ", avis.note, ", ", avis.avis)

        print(self.collection.description)
        print("\nMangas de la collection:\n")

        liste_mangas = ServiceCollection().lister_mangas_collection(
            self.collection.id_collection, "projet_info_2a"
        )
        for manga in liste_mangas:
            print(manga.titre)
        print("\n")

        from view.passif.connexion.session import Session

        if Session().connecte:
            choix = inquirer.select(
                message="Choississez une action à réaliser",
                choices=[
                    "Gérer ses avis sur la collection",
                    "Retourner au menu de recherche d'utilisateur",
                ],
            ).execute()
        else:
            choix = inquirer.select(
                message="Choississez une action à réaliser",
                choices=[
                    "Retourner au menu de recherche d'utilisateur",
                ],
            ).execute()

        match choix:
            case "Gérer ses avis sur la collection":
                return 0

            case "Retourner au menu de recherche d'utilisateur":
                from view.passif.recherche_utilisateur_vue import RechercheUtilisateurVue

                return RechercheUtilisateurVue().choisir_menu()
