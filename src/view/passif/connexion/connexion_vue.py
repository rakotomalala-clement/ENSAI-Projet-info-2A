from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from service.Service_Utilisateur import ServiceUtilisateur


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

        ServiceUtilisateur().connecter_utilisateur(nom_utilisateur, mdp)

        from view.passif.connexion.session import Session

        Session().connexion(nom_utilisateur)

        return AccueilConnecteVue().choisir_menu()
