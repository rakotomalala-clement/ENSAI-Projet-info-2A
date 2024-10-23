from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.connexion_vue import ConnexionVue
from service.Service_Utilisateur import ServiceUtilisateur
from view.passif.accueil_vue import AccueilVue


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

        for autre_utilisateur in ServiceUtilisateur().lister_tous():
            if nom_utilisateur == autre_utilisateur.nom_utilisateur:
                print("Ce nom d'utilisateur existe déjà")
                return AccueilVue().choisir_menu()

        mdp = inquirer.text(message="Veuillez saisir un mot de passe").execute()

        ServiceUtilisateur().sinscrire(nom_utilisateur, mdp)

        return ConnexionVue().choisir_menu()
