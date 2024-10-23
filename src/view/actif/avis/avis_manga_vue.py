from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class AvisMangaVue(VueAbstraite):
    def __init__(self, titre_manga):
        self.titre_manga = titre_manga

    def choisir_menu(self):
        """Affichage des avis sur la collection ou le manga

        Return
        ------
        view
            Retourne la view de l'acceuil
        """

        print("\n" + "-" * 50 + "\nMes avis sur le manga\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="",
            choices=[
                "Ajouter un avis",
                "Modifier un avis",
                "Supprimer un avis",
                "Retour au menu principal",
            ],
        )

        match choix:
            case "Ajouter un avis":
                return 0
            case "Modifier un avis":
                # on devra ensuite afficher les avis et sélectionner lequel on souhaite changer
                return 0
            case "Supprimer un avis":
                return 0
            case "Retour au menu principal":
                
