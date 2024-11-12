from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue


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

        print("\n" + "-" * 50 + "\n", self.titre, "\n" + "-" * 50 + "\n")

        # récupérer les noms des mangas de la collection
        # sous forme de liste qui va etre le choices

        # if self.type

        manga_collection = []
        manga_collection.append("Ajouter manga")
        manga_collection.append("Modifier informations collections")
        manga_collection.append("Retour au menu")

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

            case "Revenir au menu principal":
                if Session().connecte:
                    return AccueilConnecteVue().choisir_menu()
                else:
                    return AccueilVue().choisir_menu()

            case "Modifier informations collections":
                return 0

        return 0
