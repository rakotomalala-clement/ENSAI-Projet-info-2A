from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue


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
                "Créer une collection",
                "Modifier une collection",
                "Supprimer une collection",
                "Retour au menu principal",
            ],
        ).execute()

        match choix:
            case "Créer une collection":
                from view.actif.gestion_collection.creer_collection_vue import CreerCollectionVue

                return CreerCollectionVue().choisir_menu()

            case "Modifier une collection":
                # récupérer les noms des collections dont l'utilisateur est
                # Session().nom_utilisateur
                # sous forme de liste qui va etre le choices

                choix_collection = inquirer.select(
                    message="Quelle collection souhaitez-vous modifier?", choices=["a", "b"]
                ).execute()

                print(choix_collection)

                from view.actif.gestion_collection.collection_utilisateur_vue import (
                    CollectionUtilisateurVue,
                )

                return CollectionUtilisateurVue(choix_collection).choisir_menu()

            case "Supprimer une collection":
                choix_collection = inquirer.select(
                    message="Quelle collection souhaitez-vous modifier?", choices=["a", "b"]
                ).execute()

                print(choix_collection)

                from view.actif.gestion_collection.collection_utilisateur_vue import (
                    CollectionUtilisateurVue,
                )

                print(choix_collection)

            case "Retour au menu principal":
                if Session().connecte:
                    return AccueilConnecteVue().choisir_menu()
                else:
                    return AccueilVue().choisir_menu()

        return 0
