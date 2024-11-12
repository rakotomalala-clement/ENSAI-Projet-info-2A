from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from view.passif.accueil_vue import AccueilVue
from service.Service_Utilisateur import ServiceUtilisateur
from view.passif.connexion.remember_me import RememberMe
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

        # Vérifier si des informations sont enregistrées pour cet utilisateur dans "Remember Me"
        user_data = RememberMe.load_user_data(nom_utilisateur)

        if user_data:
            # Si des informations sont trouvées, connexion automatique avec le mot de passe stocké
            print(f"Connexion automatique avec {nom_utilisateur}")
            stored_hashed_password = user_data["password"]  # Récupérer le mot de passe haché

            # Vérifier si le mot de passe de l'utilisateur correspond au mot de passe haché
            mdp = inquirer.secret(message="Veuillez saisir votre mot de passe").execute()
            if RememberMe.check_password(stored_hashed_password.encode("utf-8"), mdp):
                utilisateur = ServiceUtilisateur().connecter_utilisateur(nom_utilisateur, mdp)

                if utilisateur:
                    Session().connexion(nom_utilisateur)
                    return AccueilConnecteVue().choisir_menu()
                else:
                    print("Erreur de connexion automatique, mot de passe incorrect.")
            else:
                print("Mot de passe incorrect pour la connexion automatique.")

        # Si aucune connexion automatique ou échec, demander le mot de passe
        mdp = inquirer.secret(message="Veuillez saisir votre mot de passe").execute()

        # Vérifier les informations de connexion de l'utilisateur
        utilisateur = ServiceUtilisateur().connecter_utilisateur(nom_utilisateur, mdp)

        if utilisateur:
            # Créer une session pour l'utilisateur
            Session().connexion(nom_utilisateur)

            # Demander à l'utilisateur s'il souhaite activer "Remember Me"
            remember = inquirer.confirm(
                message="Souhaitez-vous rester connecté (Remember Me) ?", default=False
            ).execute()
            if remember:
                RememberMe.save_user_data(nom_utilisateur, mdp)
                print("Informations sauvegardées pour la prochaine connexion.")

            return AccueilConnecteVue().choisir_menu()
        else:
            # Si la connexion échoue, rediriger vers l'écran d'accueil sans connexion
            return AccueilVue().choisir_menu()