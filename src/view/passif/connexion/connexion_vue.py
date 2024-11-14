from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from view.passif.accueil_vue import AccueilVue
from service.Service_Utilisateur import ServiceUtilisateur
from view.passif.connexion.session import Session


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

        # Demander à l'utilisateur son nom d'utilisateur
        nom_utilisateur = inquirer.text(message="Veuillez saisir votre nom d'utilisateur").execute()

        # Si aucune connexion automatique ou échec, demander le mot de passe
        mdp = inquirer.secret(message="Veuillez saisir votre mot de passe").execute()

        # Vérifier les informations de connexion de l'utilisateur
        utilisateur = ServiceUtilisateur().connecter_utilisateur(nom_utilisateur, mdp)

        if utilisateur:
<<<<<<< HEAD
            # Créer une session pour l'utilisateur
            Session().connexion(nom_utilisateur)

=======
            Session().nom_utilisateur = nom_utilisateur
            Session().connecte = True
>>>>>>> 45430640a807b5212e2b6d8acd0bc53ecfe9bb4c
            return AccueilConnecteVue().choisir_menu()
        else:
            return AccueilVue().choisir_menu()
