from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from view.passif.connexion.session import Session
from view.passif.affichage_manga_vue import AffichageMangaVue
from service.avis_service import ServiceAvis
from service.Service_Utilisateur import ServiceUtilisateur
from service.manga_service import MangaService


class AvisMangaVue(VueAbstraite):
    def __init__(self, manga):
        self.manga = manga

    def choisir_menu(self):
        """Affichage des avis sur la collection ou le manga

        Return
        ------
        view
            Retourne la view de l'acceuil
        """

        print("\n" + "-" * 50 + "\nMes avis sur", self.titre_manga, "\n" + "-" * 50 + "\n")

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
                from service.Service_Utilisateur import ServiceUtilisateur
                id_utilisateur = (
                ServiceUtilisateur()
                .trouver_utilisateur_par_nom(nom_utilisateur_choisi)
                .id_utilisateur
            )

                avis = 

                id_utilisateur = (
                    ServiceUtilisateur()
                    .trouver_utilisateur_par_nom(Session().nom_utilisateur)
                    .id_utilisateur
                )
                id_manga = MangaService().trouver_id_par_titre(self.titre_manga)

                note = inquirer.text(
                    message="Veuillez rentrer une note entre 1 et 5",
                ).execute()

                while not (int(note) in [1, 2, 3, 4, 5]):
                    print(note, "n'est pas un entier entre 1 et 5")
                    note = inquirer.text(
                        message="Veuillez rentrer une note entre 1 et 5",
                    ).execute()

                avis = inquirer.text(message="Veuillez entrer votre avis sur ce manga").execute()

                ServiceAvis().ajouter_avis(id_utilisateur, id_manga, avis, int(note))

                return AffichageMangaVue(self.titre_manga).choisir_menu()

            case "Modifier un avis":
                # on devra ensuite afficher les avis et sélectionner lequel on souhaite changer
                nouvelle_note = inquirer.text(
                    message="Veuillez rentrer une note entre 1 et 5",
                    validate=lambda val: val.isdigit() and 1 <= int(val) <= 5,
                    invalid_message="Ce n'est pas un nombre entier valide entre 1 et 5",
                ).execute()

                nouvel_avis = inquirer.text(message="Veuillez entrer votre avis sur ce manga")

                ServiceAvis().modifier(nouvel_avis, int(nouvelle_note))

                return AffichageMangaVue(self.titre_manga).choisir_menu()

            case "Supprimer un avis":
                return 0
            case "Retour au menu principal":
                if Session().connecte:
                    return AccueilConnecteVue().choisir_menu()
                else:
                    return AccueilVue().choisir_menu()
