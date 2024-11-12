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
        manga_collection = []
        manga_collection.append("Ajouter manga")
        manga_collection.append("Modifier informations collections")
        manga_collection.append("Supprimer la collection")
        manga_collection.append("Retour au menu")

        choix = inquirer.select(
            message="Sélectionner un manga pour modifier les informations dessus"
            " ou le supprimer de votre collection ou bien ajoutez-en un à votre collection",
            choices=manga_collection,
        ).execute()

        match choix:
            case "Ajouter manga":
                from service.manga_service import MangaService

                liste_mangas = MangaService().lister_mangas()
                for indice_manga in range(8):
                    print(liste_mangas[indice_manga].titre)

                titre = inquirer.text(
                    message="Donner le nom du manga que vous souhaitez ajouter"
                ).execute()

                id_manga = [MangaService().trouver_id_par_titre(titre).id_manga]

                ServiceCollection().ajouter_mangas_a_collection(
                    self.collection.id_collection, id_manga, "projet_info_2a"
                )

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

            case "Modifier informations collections":
                return 0

        return 0
