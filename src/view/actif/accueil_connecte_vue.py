from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class AccueilConnecteVue(VueAbstraite):
    """Vue d'accueil de l'application"""

    def choisir_menu(self):
        """Choix du menu suivant sachant que l'on est connecté

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nAccueil\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Rechercher manga",
                "Rechercher utilisateur",
                "Gérer ses collections",
                "Quitter",
            ],
        ).execute()

        match choix:
            case "Quitter":
                pass

            case "Rechercher manga":
                from view.passif.recherche_manga_vue import RechercheMangaVue

                return RechercheMangaVue().choisir_menu()

            case "Rechercher utilisateur":
                from view.passif.recherche_utilisateur_vue import RechercheUtilisateurVue

                return RechercheUtilisateurVue().choisir_menu()

            case "Gérer ses collections":
                from view.actif.gestion_collection.gestion_collection_vue import (
                    GestionCollectionVue,
                )

                return GestionCollectionVue().choisir_menu()
