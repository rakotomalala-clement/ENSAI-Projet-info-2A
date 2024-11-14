from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from view.passif.connexion.session import Session
from view.passif.affichage_manga_vue import AffichageMangaVue
from service.avis_service import ServiceAvis
from service.Service_Utilisateur import ServiceUtilisateur


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

        print("\n" + "-" * 50 + "\nMes avis sur", self.manga.titre, "\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="",
            choices=[
                "Ajouter mon avis",
                "Modifier mon avis",
                "Supprimer mon avis",
                "Retour au menu principal",
            ],
        ).execute()

        id_utilisateur = (
            ServiceUtilisateur()
            .trouver_utilisateur_par_nom(Session().nom_utilisateur)
            .id_utilisateur
        )

        id_manga = self.manga.id_manga

        match choix:
            case "Ajouter mon avis":
                avis = ServiceAvis().afficher_avis_user(id_utilisateur, id_manga)

                if avis is None:

                    note = inquirer.text(
                        message="Veuillez rentrer une note entre 1 et 5",
                    ).execute()

                    while not (int(note) in [1, 2, 3, 4, 5]):
                        print(note, "n'est pas un entier entre 1 et 5")
                        note = inquirer.text(
                            message="Veuillez rentrer une note entre 1 et 5",
                        ).execute()

                    avis = inquirer.text(
                        message="Veuillez entrer votre avis sur ce manga"
                    ).execute()

                    ServiceAvis().ajouter_avis(id_utilisateur, id_manga, avis, int(note))

                    return AffichageMangaVue(self.manga.titre).choisir_menu()
                else:
                    print("Vous avez déjà un avis sur ce manga")
                    return AvisMangaVue(self.manga).choisir_menu()

            case "Modifier mon avis":
                nouvelle_note = inquirer.text(
                    message="Veuillez rentrer une note entre 1 et 5",
                ).execute()

                while not (int(nouvelle_note) in [1, 2, 3, 4, 5]):
                    print(nouvelle_note, "n'est pas un entier entre 1 et 5")
                    nouvelle_note = inquirer.text(
                        message="Veuillez rentrer une note entre 1 et 5",
                    ).execute()

                nouvel_avis = inquirer.text(
                    message="Veuillez entrer votre avis sur ce manga"
                ).execute()

                ServiceAvis().modifier(nouvel_avis, int(nouvelle_note))

                return AffichageMangaVue(self.titre_manga).choisir_menu()

            case "Supprimer mon avis":
                avis = ServiceAvis().afficher_avis_user(id_utilisateur, self.manga.id_manga)
                ServiceAvis().supprimer(avis.id_avis)
                return AffichageMangaVue(self.manga.titre).choisir_menu()

            case "Retour au menu principal":
                if Session().connecte:
                    return AccueilConnecteVue().choisir_menu()
                else:
                    return AccueilVue().choisir_menu()
