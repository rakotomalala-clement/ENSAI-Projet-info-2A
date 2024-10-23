from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from view.passif.connexion.session import Session
from service.avis_service import ServiceAvis
from service.Service_Utilisateur import ServiceUtilisateur
from service.manga_service import MangaService


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
        ).execute()

        match choix:
            case "Ajouter un avis":

                id_utilisateur = (
                    ServiceUtilisateur()
                    .trouver_utilisateur_par_nom(Session().nom_utilisateur)
                    .id_utilisateur
                )
                id_manga = MangaService().trouver_id_par_titre(self.titre_manga)
                ServiceAvis().ajouter_avis(id_utilisateur, id_manga, "super", 3)

                return 0
            case "Modifier un avis":
                # on devra ensuite afficher les avis et sélectionner lequel on souhaite changer
                return 0
            case "Supprimer un avis":
                return 0
            case "Retour au menu principal":
                if Session().connecte:
                    return AccueilConnecteVue().choisir_menu()
                else:
                    return AccueilVue().choisir_menu()
