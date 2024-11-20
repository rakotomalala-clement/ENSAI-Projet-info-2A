from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from service.collection_service import ServiceCollection
from service.avis_service import ServiceAvis


class CollectionUtilisateurVue(VueAbstraite):
    """Menu des modifications possibles sur une collection"""

    def __init__(self, collection):
        self.collection = collection

    def choisir_menu(self):
        """Modification ou suppression d'une collection

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\n", self.collection.titre, "\n" + "-" * 50 + "\n")

        # afficher les mangas de la collection
        liste_manga = ServiceCollection().lister_mangas_collection(
            self.collection.id_collection, "projet_info_2a"
        )
        for manga in liste_manga:
            print(manga.titre)
        print("\n")

        liste_avis = ServiceAvis().afficher_avis_user(self.collection.id_collection)
        if liste_avis:
            for avis in liste_avis:
                print(avis.note, " : ", avis.avis)

        modif_collection = [
            "Ajouter manga",
            "Supprimer un manga",
            "Modifier les informations sur la collection",
            "Supprimer la collection",
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

                ServiceCollection().ajouter_mangas_collection_coherente(
                    self.collection.id_collection, [id_manga], "projet_info_2a"
                )

                return CollectionUtilisateurVue(self.collection).choisir_menu()

            case "Supprimer un manga":
                from service.manga_service import MangaService

                liste_mangas_dans_collection = ServiceCollection().lister_mangas_collection(
                    self.collection.id_collection, "projet_info_2a"
                )

                if liste_mangas_dans_collection == []:
                    print("Il n'y a actuellement aucun manga dans cette collection \n")
                    return CollectionUtilisateurVue(self.collection).choisir_menu()

                liste_nom_mangas_dans_collection = []
                for manga in liste_mangas_dans_collection:
                    liste_nom_mangas_dans_collection.append(manga.titre)

                titre = inquirer.fuzzy(
                    message="Quel manga souhaitez-vous supprimer?",
                    choices=liste_nom_mangas_dans_collection,
                ).execute()

                id_manga = MangaService().trouver_id_par_titre(titre)

                ServiceCollection().supprimer_manga_col_coherente(
                    self.collection.id_collection, id_manga, "projet_info_2a"
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
                    if collection.titre == self.collection.titre:
                        collection_modifie = collection

                return CollectionUtilisateurVue(collection_modifie).choisir_menu()

            case "Modifier les informations sur la collection":
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

            case "Supprimer la collection":

                ServiceCollection().supprimer_collection(
                    self.collection.id_collection, "Coherente", schema="projet_info_2a"
                )

                from view.actif.gestion_collection.gestion_collection_vue import (
                    GestionCollectionVue,
                )

                return GestionCollectionVue().choisir_menu()

            case "Revenir au menu principal":
                if Session().connecte:
                    return AccueilConnecteVue().choisir_menu()
                else:
                    return AccueilVue().choisir_menu()
