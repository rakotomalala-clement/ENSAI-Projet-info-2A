# from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite

# from view.passif.accueil_vue import AccueilVue
# from view.actif.accueil_connecte_vue import AccueilConnecteVue

# from view.passif.connexion.session import Session


class RechercheCollectionVue(VueAbstraite):
    "Vue de la barre de recherche des collections de l'utilisateur sélectionné"

    def __init__(self, nom_utilisateur):
        self.nom_utilisateur = nom_utilisateur

    def choisir_menu(self):
        """Choix de la collection à consulter

        Return
        ------
        view
            Retourne les details associer à la collection choisi
        """

        print("\n" + "-" * 50 + "\nCollection de", self.nom_utilisateur, "\n" + "-" * 50 + "\n")

        # liste des collections de l'utilisateur

        # from service.  import
        # liste_collections = servicecollection(nom_utilisateur).liter_collection()

        """
        if liste_collections == []:
            print("l'utilisateur", self.nom_utilisateur, "n'a pour le moment aucune collection")
            if Session().connecte:
                return AccueilConnecteVue().choisir_menu()
            else:
                return AccueilVue().choisir_menu()

        liste_nom_collections = []
        for collection in liste_collections:
            liste_nom_collections.append(collection.titre)

        nom_collection_choisi = inquirer.select(
            message="Veuillez choisir la collection à consulter",
            choices=liste_nom_collections,
        ).execute()
        """

        return 0
