# from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session


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

        return 0
