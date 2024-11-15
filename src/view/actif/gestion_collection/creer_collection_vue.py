from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session


class CreerCollectionVue(VueAbstraite):
    "Vue de la page de création de collection"

    def choisir_menu(self):
        """Création de collection

        Return
        ------
        view
            Retourne un menu permettant à l'utilisateur de créer une collection
        """

        print("\n" + "-" * 50 + "\nCréation de collection\n" + "-" * 50 + "\n")

        nom_collection = inquirer.text(message="Quel est le nom de votre collection?").execute()
        description_collection = inquirer.text(
            message="Donnez une description de la collection"
        ).execute()

        from service.collection_service import ServiceCollection
        from service.Service_Utilisateur import ServiceUtilisateur

        utilisateur = ServiceUtilisateur().trouver_utilisateur_par_nom(Session().nom_utilisateur)
        ServiceCollection().creer_collection(
            id_utilisateur=utilisateur.id_utilisateur,
            type_collection="Cohérente",
            titre=nom_collection,
            description=description_collection,
            dernier_tome_acquis=None,
            numeros_tomes_manquants=None,
            status=None,
            schema="projet_info_2a",
        )

        from view.actif.gestion_collection.gestion_collection_vue import GestionCollectionVue

        return GestionCollectionVue().choisir_menu()
