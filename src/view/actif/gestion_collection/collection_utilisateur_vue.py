# from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class CollectionUtilisateurVue(VueAbstraite):
    """Menu des modifications possibles sur une collection"""

    def __init__(self, titre):
        # titre de la collection
        self.titre = titre

    def choisir_menu(self):
        """Choix du menu suivant sachant que l'on a sélectionné une collection

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\n", self.titre, "\n" + "-" * 50 + "\n")

        return 0
