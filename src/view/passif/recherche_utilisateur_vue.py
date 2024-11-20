from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from service.Service_Utilisateur import ServiceUtilisateur
from view.passif.collection_coherente_vue import CollectionCoherenteVue
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from view.passif.connexion.session import Session


class RechercheUtilisateurVue(VueAbstraite):
    "Vue de la barre de recherche des utilisateurs"

    def choisir_menu(self):
        """Choix de l'utilisateur à consulter

        Return
        ------
        view
            Retourne l'affichage des collections d'un utilisateur
        """

        print("\n" + "-" * 50 + "\nRecherche d'un utilisateur\n" + "-" * 50 + "\n")

        liste_utilisateurs = ServiceUtilisateur().lister_tous()

        if liste_utilisateurs == []:
            print("il n'y a actuellement aucun utilisateur d'inscrit")
            if Session().connecte:
                return AccueilConnecteVue().choisir_menu()
            else:
                return AccueilVue().choisir_menu()

        liste_nom_utilisateurs = []
        for utilisateur in liste_utilisateurs:
            liste_nom_utilisateurs.append(utilisateur.nom_utilisateur)

        # Ajout de la possibilité de retourner au menu principal
        liste_nom_utilisateurs.append("Retour au menu principal")

        nom_utilisateur_choisi = inquirer.fuzzy(
            message="Veuillez choisir l'utilisateur dont vous souhaitez consulter les collections",
            choices=liste_nom_utilisateurs,
        ).execute()

        if nom_utilisateur_choisi == "Retour au menu principal":
            if Session().connecte:
                return AccueilConnecteVue().choisir_menu()
            else:
                return AccueilVue().choisir_menu()
        else:

            id_utilisateur = (
                ServiceUtilisateur()
                .trouver_utilisateur_par_nom(nom_utilisateur_choisi)
                .id_utilisateur
            )

            from service.collection_service import ServiceCollection

            liste_collections = ServiceCollection().lister_collections_coherentes(
                id_utilisateur, "projet_info_2a"
            )

            liste_nom_collections = ["Collection physique"]

            if not (liste_collections is None):
                for collection in liste_collections:
                    liste_nom_collections.append(collection.titre)

            # Ajout de la possibilité de retourner au menu principal
            liste_nom_collections.append("Retour au menu principal")

            nom_collection_choisi = inquirer.select(
                message="Veuillez choisir la collection à consulter \n",
                choices=liste_nom_collections,
            ).execute()

            if nom_collection_choisi == "Retour au menu principal":
                if Session().connecte:
                    return AccueilConnecteVue().choisir_menu()
                else:
                    return AccueilVue().choisir_menu()

            elif nom_collection_choisi == "Collection physique":
                print("\nCollection physique de", nom_utilisateur_choisi, ":\n")

                collection_physique = ServiceCollection().rechercher_collection_physique(
                    id_utilisateur, "projet_info_2a"
                )

                # afficher les mangas de la collection
                if collection_physique == "Aucun manga ajouté":
                    print(
                        "Aucun manga dans la collection physique de", nom_utilisateur_choisi, "\n"
                    )
                else:
                    for manga in collection_physique:
                        print(manga.titre_manga)
                        print(manga.dernier_tome_acquis)
                        print(manga.numeros_tomes_manquants)
                        print(manga.status_manga)
                        print("\n")
                    print("\n")

                # Affichage des avis sur cette collection
                from service.avis_service import ServiceAvis

                liste_avis = ServiceAvis().afficher_avis_collection_physique(
                    self.collection.id_collection
                )
                if liste_avis is None:
                    print("")
                else:
                    for avis in liste_avis:
                        print("Note: ", avis.note, ", ", avis.avis)

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
                            "Gérer ses avis sur la collection",
                        ],
                    ).execute()

                match choix:

                    case "Gérer ses avis sur la collection":
                        from view.actif.avis.avis_physique_vue import AvisPhysiqueVue

                        return AvisPhysiqueVue(nom_utilisateur_choisi).choisir_menu()

                    case "Retourner au menu de recherche d'utilisateur":
                        return RechercheUtilisateurVue().choisir_menu()

            else:
                # On a besoin de retrouver la collection dont le nom est nom_collection_choisi
                collection_choisi = None
                for collection in liste_collections:
                    if collection.titre == nom_collection_choisi:
                        collection_choisi = collection

                return CollectionCoherenteVue(collection_choisi).choisir_menu()
