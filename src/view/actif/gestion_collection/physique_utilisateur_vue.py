from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from service.collection_service import ServiceCollection


class PhysiqueUtilisateurVue(VueAbstraite):
    """Menu des modifications possibles sur une collection"""

    def choisir_menu(self):
        """Modification d'une collection physique

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\n", "Ma collection physique", "\n" + "-" * 50 + "\n")

        print("La suppression de votre collection physique n'est pas possible \n")

        # Ici la collection physique est une liste de mangas

        from service.Service_Utilisateur import ServiceUtilisateur

        id_utilisateur = (
            ServiceUtilisateur()
            .trouver_utilisateur_par_nom(Session().nom_utilisateur)
            .id_utilisateur
        )
        collection_physique = ServiceCollection().rechercher_collection_physique(
            id_utilisateur, "projet_info_2a"
        )

        # afficher les mangas de la collection
        if collection_physique == "Aucun manga ajouté":
            print("Aucun manga ajouté \n")
        else:
            for manga in collection_physique:
                print(manga.titre_manga)
                print(manga.dernier_tome_acquis)
                print(manga.numeros_tomes_manquants)
                print(manga.status_manga)
                print("\n")
            print("\n")

        modif_collection = [
            "Ajouter manga",
            "Supprimer un manga",
            "Modifier les informations d'un manga",
            "Revenir au menu principal",
        ]

        choix = inquirer.select(
            message="Quelles modifications souhaitez-vous apporter sur votre colection?",
            choices=modif_collection,
        ).execute()

        match choix:
            case "Ajouter manga":
                from service.manga_service import MangaService

                liste_mangas = MangaService().lister_mangas()
                liste_nom_mangas = []
                for manga in liste_mangas:
                    liste_nom_mangas.append(manga.titre)

                titre = inquirer.fuzzy(
                    message="Quel manga souhaitez-vous ajouter?", choices=liste_nom_mangas
                ).execute()

                id_manga = MangaService().trouver_id_par_titre(titre)

                # liste_tomes = []
                # tome = inquirer.text(
                #     message="Veuillez entrer un à un les numéros des tomes que vous possédez ou tapez 'STOP' pour arrêter d'en ajouter"
                # ).execute()

                # while tome != "STOP":
                #     try:
                #         int(tome)
                #     except ValueError:
                #         print("Vous avez saisi autre chose que ce qui a été demandé.")
                #         return PhysiqueUtilisateurVue(self.liste_manga).choisir_menu()

                #     liste_tomes.append(int(tome))

                ServiceCollection().ajouter_manga_collection_physique(
                    id_utilisateur, titre, 0, 0, "en cours", "projet_info_2a"
                )

                return PhysiqueUtilisateurVue().choisir_menu()

            case "Supprimer un manga":

                # id_collection = ServiceCollection().methode(id_utilisateur, "projet_info_2a")

                liste_nom_mangas_collection = []
                for manga in collection_physique:
                    liste_nom_mangas_collection.append(manga.titre_manga)

                titre = inquirer.fuzzy(
                    message="Quel manga souhaitez-vous supprimer?",
                    choices=liste_nom_mangas_collection,
                ).execute()

                id_manga = MangaService().trouver_id_par_titre(titre)

                ServiceCollection().supprimer_manga_col_physique(
                    id_collection, id_manga, "projet_info_2a"
                )

            case "Modifier les informations d'un manga":
                nouveau_titre = inquirer.text(
                    message="Quel est le nouveau titre de votre collection"
                ).execute()
                nouvelle_description = inquirer.text(
                    message="Quelle est la nouvelle description de votre collection"
                ).execute()

                ServiceCollection().modifier_collection_coherente(
                    self.collection.id_collection,
                    nouveau_titre,
                    nouvelle_description,
                    "projet_info_2a",
                )

                # On veut recharger notre collection une fois modifier
                from service.Service_Utilisateur import ServiceUtilisateur

                id_utilisateur = (
                    ServiceUtilisateur()
                    .trouver_utilisateur_par_nom(Session().nom_utilisateur)
                    .id_utilisateur
                )

                liste_collections = ServiceCollection().lister_collections_coherentes(
                    id_utilisateur, "projet_info_2a"
                )

                collection_modifie = None
                for collection in liste_collections:
                    if collection.titre == nouveau_titre:
                        collection_modifie = collection

                return CollectionUtilisateurVue(collection_modifie).choisir_menu()

            # case "Supprimer la collection":

            #     ServiceCollection().supprimer_collection(
            #         self.collection.id_collection, "Coherente", schema="projet_info_2a"
            #     )

            #     from view.actif.gestion_collection.gestion_collection_vue import (
            #         GestionCollectionVue,
            #     )

            #     return GestionCollectionVue().choisir_menu()

            # case "Revenir au menu principal":
            #     if Session().connecte:
            #         return AccueilConnecteVue().choisir_menu()
            #     else:
            #         return AccueilVue().choisir_menu()
