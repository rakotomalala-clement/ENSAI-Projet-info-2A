from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class CollectionUtilisateurVue(VueAbstraite):
    """Menu des modifications possibles sur une collection"""

    def choisir_menu(self):
        """Choix du menu suivant sachant que l'on a sélectionné une collection

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nAccueil\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Rechercher manga",
                "Rechercher utilisateur",
                "Gérer ses collections",
                "Quitter",
            ],
        ).execute()

        return choix
