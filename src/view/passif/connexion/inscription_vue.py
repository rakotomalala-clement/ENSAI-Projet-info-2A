from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.connexion_vue import ConnexionVue
from service.Service_Utilisateur import ServiceUtilisateur


class InscriptionVue(VueAbstraite):
    "Vue de la barre de recherche de mangas"

    def choisir_menu(self):
        """Inscription

        Return
        ------
        view
            Retourne un menu permettant à l'utilisateur de s'inscrire
        """

        print("\n" + "-" * 50 + "\nInscription\n" + "-" * 50 + "\n")

        nom_utilisateur = inquirer.text(message="Veuillez saisir votre nom d'utilisateur").execute()

        mdp = inquirer.text(message="Veuillez saisir un mot de passe").execute()

        # faire une verif que le nom d'utilisateur n'existe pas déjà
        ServiceUtilisateur().sinscrire(nom_utilisateur, mdp)

        return ConnexionVue().choisir_menu()
