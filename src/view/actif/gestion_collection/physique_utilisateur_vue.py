from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from service.collection_service import ServiceCollection
from service.manga_service import MangaService


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
            message="Quelles modifications souhaitez-vous apporter sur votre colection?\n",
            choices=modif_collection,
        ).execute()

        match choix:
            case "Ajouter manga":

                liste_mangas = MangaService().lister_mangas()
                liste_nom_mangas = []
                for manga in liste_mangas:
                    liste_nom_mangas.append(manga.titre)

                titre = inquirer.fuzzy(
                    message="Quel manga souhaitez-vous ajouter?\n", choices=liste_nom_mangas
                ).execute()

                id_manga = MangaService().trouver_id_par_titre(titre)

                ServiceCollection().ajouter_manga_collection_physique(
                    id_utilisateur, titre, 0, 0, "en cours de lecture", "projet_info_2a"
                )

                return PhysiqueUtilisateurVue().choisir_menu()

            case "Supprimer un manga":

                id_collection = ServiceCollection().obtenir_id_collection_par_utilisateur(
                    id_utilisateur, "projet_info_2a"
                )

                if collection_physique == "Aucun manga ajouté":
                    print("Vous n'avez pas encore ajouter de manga.")
                    return PhysiqueUtilisateurVue().choisir_menu()

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

                return PhysiqueUtilisateurVue().choisir_menu()

            case "Modifier les informations d'un manga":

                if collection_physique == "Aucun manga ajouté":
                    print("Vous n'avez pas encore ajouter de manga.")
                    return PhysiqueUtilisateurVue().choisir_menu()

                liste_nom_mangas_collection = []
                for manga in collection_physique:
                    liste_nom_mangas_collection.append(manga.titre_manga)

                titre_choisi = inquirer.fuzzy(
                    message="Quel est le manga dont vous souhaitez modifier les informations?",
                    choices=liste_nom_mangas_collection,
                ).execute()

                manga_choisi = None
                for manga in collection_physique:
                    if manga.titre_manga == titre_choisi:
                        manga_choisi = manga

                choix = inquirer.select(
                    message="Que souhaitez vous faire?",
                    choices=["Ajouter un tome", "Changer le statut de lecture"],
                ).execute()

                match choix:

                    case "Ajouter un tome":

                        tome = inquirer.text(message="Quel tome souhaitez vous ajouter?").execute()
                        try:
                            tome = int(tome)
                        except ValueError:
                            print("Vous avez saisi autre chose que ce qui a été demandé.")
                            return PhysiqueUtilisateurVue().choisir_menu()

                        if tome <= manga_choisi.dernier_tome_acquis:
                            numero_dernier_tome = manga_choisi.dernier_tome_acquis
                            numero_tomes_manquants = manga_choisi.numeros_tomes_manquants
                        else:
                            numero_dernier_tome = tome

                            numero_tomes_manquants = manga_choisi.numeros_tomes_manquants
                            for num_tome in range(tome, manga_choisi.dernier_tome_acquis, -1):
                                numero_tomes_manquants.append(num_tome)

                        ServiceCollection().modifier_collection_physique(
                            id_utilisateur,
                            manga_choisi.titre_manga,
                            numero_dernier_tome,
                            numero_tomes_manquants,
                            manga_choisi.status_manga,
                            "projet_info_2a",
                        )

                        return PhysiqueUtilisateurVue().choisir_menu()

                    case "Changer le statut de lecture":
                        status_manga = inquirer.text(
                            message="Quel est le nouveau statut de la série?"
                        ).execute()

                        ServiceCollection().modifier_collection_physique(
                            id_utilisateur,
                            manga_choisi.titre_manga,
                            manga_choisi.dernier_tome_acquis,
                            manga_choisi.numeros_tomes_manquants,
                            status_manga,
                            "projet_info_2a",
                        )

                return PhysiqueUtilisateurVue().choisir_menu()

            case "Revenir au menu principal":
                if Session().connecte:
                    return AccueilConnecteVue().choisir_menu()
                else:
                    return AccueilVue().choisir_menu()
