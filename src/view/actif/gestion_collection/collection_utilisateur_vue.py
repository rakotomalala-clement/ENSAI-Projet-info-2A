from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class CollectionUtilisateurVue(VueAbstraite):
    """Menu des modifications possibles sur une collection"""

    def __init__(self, titre, type_collection=None):
        # titre de la collection
        self.titre = titre
        self.type_collection = type_collection

    def choisir_menu(self):
        """Choix du menu suivant sachant que l'on a sélectionné une collection

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\n", self.titre, "\n" + "-" * 50 + "\n")

        # récupérer les noms des mangas de la collection
        # sous forme de liste qui va etre le choices

        # if self.type
        manga_collection = []
        manga_collection.append("Ajouter manga")

        choix = inquirer.select(
            message="Sélectionner un manga pour modifier les informations dessus"
            " ou le supprimer de votre collection ou bien ajoutez-en un à votre collection",
            choices=manga_collection,
        ).execute()

        match choix:
            case "Ajouter manga":
                titre = inquirer.text(
                    message="Donner le nom du manga que vous souhaitez ajouter"
                ).execute()

                print(titre)

        return 0
