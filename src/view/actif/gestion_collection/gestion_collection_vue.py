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
                "Modifier/Supprimer une collection",
                "Retour au menu principal",
            ],
        ).execute()

        match choix:
            case "Créer une collection":
                from view.actif.gestion_collection.creer_collection_vue import CreerCollectionVue

                return CreerCollectionVue().choisir_menu()

            case "Modifier/Supprimer une collection":
                # récupérer les noms des collections dont l'utilisateur est
                # Session().nom_utilisateur
                # sous forme de liste qui va etre le choices

                from service.collection_service import ServiceCollection
                from service.Service_Utilisateur import ServiceUtilisateur

                id_utilisateur = ServiceUtilisateur().trouver_utilisateur_par_nom(
                    Session().id_utilisateur
                )
                liste_collections = ServiceCollection().rechercher_collection_coherente_par_user(
                    id_utilisateur, "projet_info_2a"
                )
                liste_nom_collections = []
                for collection in liste_collections:
                    liste_nom_collections.append(collection.titre)

                nom_collection_choisi = inquirer.select(
                    message="Quelle collection souhaitez-vous modifier/supprimer?",
                    choices=liste_collections,
                ).execute()

                from view.actif.gestion_collection.collection_utilisateur_vue import (
                    CollectionUtilisateurVue,
                )

                collection_choisi = ""
                for collection in liste_collections:
                    if collection.titre == nom_collection_choisi:
                        collection_choisi = collection

                return CollectionUtilisateurVue(collection_choisi).choisir_menu()

            case "Retour au menu principal":
                if Session().connecte:
                    return AccueilConnecteVue().choisir_menu()
                else:
                    return AccueilVue().choisir_menu()

        return 0
