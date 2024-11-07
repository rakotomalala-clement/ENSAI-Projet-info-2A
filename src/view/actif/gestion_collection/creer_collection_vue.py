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

        from business_object.collection.collection_coherente import CollectionCoherente

        collection = CollectionCoherente(nom_collection, description_collection)

        utilisateur = ServiceUtilisateur().trouver_utilisateur_par_nom(Session().nom_utilisateur)
        ServiceCollection().creer_collection(
            utilisateur.id_utilisateur, collection, "projet_info_2a"
        )

        return 0
