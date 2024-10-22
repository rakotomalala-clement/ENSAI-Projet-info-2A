from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class ModificationSelectionCollectionVue(VueAbstraite):
    "Permet de sélectionner la collection à modifier"

    def choisir_menu(self):
        """Selection de la collection à modifier

        Return
        ------
        view
            Retourne la collection choisie ainsi que
            des options de modifications pour cette dernière
        """

        print("\n" + "-" * 50 + "\nSélection de collection\n" + "-" * 50 + "\n")

        # on veut que les choices se fassent en fonction des collections de notre utilisateur
        # on va utiliser Session
        # faire une liste

        # from view.passif.connexion.session import Session
        # Session().nom_utilisateur

        choix = inquirer.select(
            message="Voulez-vous créer ou modifier une de vos collections?",
            choices=["a"],
        ).execute()

        match choix:
            case "a":
                return 0
