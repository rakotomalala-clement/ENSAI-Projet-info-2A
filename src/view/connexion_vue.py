from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.accueil_connecte_vue import AccueilConnecteVue


class ConnexionVue(VueAbstraite):
    "Vue de la page de connexion"

    def choisir_menu(self):
        """Connexion

        Return
        ------
        view
            Retourne un menu permettant à l'utilisateur de se connecter
        """

        print("\n" + "-" * 50 + "\nConnexion\n" + "-" * 50 + "\n")

        nom_utilisateur = inquirer.text(message="Veuillez saisir votre nom d'utilisateur").execute()

        mdp = inquirer.text(message="Veuillez saisir votre mot de passe").execute()

        print(nom_utilisateur)
        print(mdp)

        print("Vous êtes connectés")

        return AccueilConnecteVue().choisir_menu()
