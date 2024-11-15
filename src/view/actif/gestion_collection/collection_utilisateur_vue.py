from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from service.collection_service import ServiceCollection


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

        # récupérer les noms des mangas de la collection
        # Collection.

        # if self.type

        modif_collection = [
            "Ajouter manga",
            "Modifier les informations sur un manga",
            "Modifier les informations sur la collection",
            "Supprimer la collection",
            "Retour au menu",
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

                id_manga = [MangaService().trouver_id_par_titre(titre)]

                ServiceCollection().ajouter_mangas_a_collection(
                    self.collection.id_collection, id_manga, "projet_info_2a"
                )

            case "Modifier les informations sur un manga":
                from view.actif.gestion_collection.manga_collection_vue import MangaCollectionVue

                return MangaCollectionVue().choisir_menu()

            case "Modifier les informations sur la collection":
                return 0

            case "Supprimer la collection":
                from service.Service_Utilisateur import ServiceUtilisateur

                if self.collection.type_collection == "Physique":
                    print("\n Vous ne pouvez pas supprimer votre collection physique")
                    return CollectionUtilisateurVue(self.collection).choisir_menu()

                id_utilisateur = (
                    ServiceUtilisateur()
                    .trouver_utilisateur_par_nom(Session().nom_utilisateur)
                    .id_utilisateur
                )

                ServiceCollection().supprimer_collection(
                    self.collection, id_utilisateur, schema="projet_info_2a"
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

        return 0
