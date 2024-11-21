from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session
from service.avis_service import ServiceAvis
from service.Service_Utilisateur import ServiceUtilisateur


class AvisCoherentVue(VueAbstraite):
    def __init__(self, collection):
        self.collection = collection

    def choisir_menu(self):
        """Affichage des avis sur la collection

        Return
        ------
        view
            Retourne la view de l'acceuil
        """

        print(
            "\n" + "-" * 50 + "\nMon avis sur la collection",
            self.collection.titre,
            "\n" + "-" * 50 + "\n",
        )

        choix = inquirer.select(
            message="\n",
            choices=[
                "Ajouter mon avis",
                "Modifier mon avis",
                "Supprimer mon avis",
                "Retourner au menu de recherche d'utilisateur",
            ],
        ).execute()

        id_utilisateur = (
            ServiceUtilisateur()
            .trouver_utilisateur_par_nom(Session().nom_utilisateur)
            .id_utilisateur
        )

        avis = ServiceAvis().afficher_avis_user_sur_collection_coherente(
            id_utilisateur, self.collection.id_collection
        )

        match choix:
            case "Ajouter mon avis":

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
                        message="Veuillez entrer votre avis sur cette collection"
                    ).execute()

                    ServiceAvis().ajouter_avis_collection(
                        id_utilisateur, self.collection.id_collection, "Coherente", avis, int(note)
                    )

                    return AvisCoherentVue(self.collection).choisir_menu()
                else:
                    print("Vous avez déjà un avis sur cette collection")
                    return AvisCoherentVue(self.collection).choisir_menu()

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
                    message="Veuillez entrer votre avis sur cette collection"
                ).execute()

                ServiceAvis().modifier_collection_cohérente(
                    self.collection.id_collection, id_utilisateur, nouvel_avis, nouvelle_note
                )

                return AvisCoherentVue(self.collection).choisir_menu()

            case "Supprimer mon avis":
                avis = ServiceAvis().afficher_avis_collection_coherente(
                    self.collection.id_collection
                )
                if avis is None:
                    print("Vous n'avez pas encore d'avis sur cette collection")
                    return AvisCoherentVue(self.collection).choisir_menu()

                ServiceAvis().supprimer(avis.id_avis)
                return AvisCoherentVue(self.collection).choisir_menu()

            case "Retourner au menu de recherche d'utilisateur":
                from view.passif.recherche_utilisateur_vue import RechercheUtilisateurVue

                return RechercheUtilisateurVue().choisir_menu()
