from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from service.Service_Utilisateur import ServiceUtilisateur
from view.passif.recherche_collection_vue import RechercheCollectionVue
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from view.passif.connexion.session import Session


class RechercheUtilisateurVue(VueAbstraite):
    "Vue de la barre de recherche des utilisateurs"

    def choisir_menu(self):
        """Choix de l'utilisateur à consulter

        Return
        ------
        view
            Retourne l'affichage des collections d'un utilisateur
        """

        print("\n" + "-" * 50 + "\nRecherche d'un utilisateur'\n" + "-" * 50 + "\n")

        liste_utilisateurs = ServiceUtilisateur().lister_tous()

        if liste_utilisateurs == []:
            print("il n'y a actuellement aucun utilisateur d'inscrit")
            if Session().connecte:
                return AccueilConnecteVue().choisir_menu()
            else:
                return AccueilVue().choisir_menu()

        liste_nom_utilisateurs = []
        for utilisateur in liste_utilisateurs:
            liste_nom_utilisateurs.append(utilisateur.nom_utilisateur)

        # Ajout de la possibilité de retourner au menu principal
        liste_nom_utilisateurs.append("Retour au menu principal")

        nom_utilisateur_choisi = inquirer.select(
            message="Veuillez choisir l'utilisateur dont vous souhaitez consulter les collections",
            choices=liste_nom_utilisateurs,
        ).execute()

        if nom_utilisateur_choisi == "Retour au menu principal":
            if Session().connecte:
                return AccueilConnecteVue().choisir_menu()
            else:
                return AccueilVue().choisir_menu()
        else:
            return RechercheCollectionVue(nom_utilisateur_choisi).choisir_menu()
