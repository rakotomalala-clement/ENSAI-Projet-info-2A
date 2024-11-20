from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from view.passif.connexion.session import Session
from service.avis_service import ServiceAvis
from service.Service_Utilisateur import ServiceUtilisateur


class AvisPhysiqueVue(VueAbstraite):
    def __init__(self, nom_utilisateur):
        self.nom_utilisateur = nom_utilisateur

    def choisir_menu(self):
        """Affichage des avis sur la collection

        Return
        ------
        view
            Retourne la view de l'acceuil
        """

        print(
            "\n" + "-" * 50 + "\nMon avis sur la collection physique de",
            self.nom_utilisateur,
            "\n" + "-" * 50 + "\n",
        )

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

        # l'id_utilisateur du propriétaire de la collection
        from service.collection_service import ServiceCollection

        id_utilisateur_collection = (
            ServiceUtilisateur()
            .trouver_utilisateur_par_nom(Session().nom_utilisateur)
            .id_utilisateur
        )
        id_collection_physique = ServiceCollection().obtenir_id_collection_par_utilisateur(
            id_utilisateur_collection, "projet_info_2a"
        )

        match choix:
            case "Ajouter mon avis":
                avis = ServiceAvis().afficher_avis_collection_physique(id_collection_physique)

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

                    ServiceAvis().ajouter_avis_collection(
                        id_utilisateur, id_collection_physique, "Physique", avis, int(note)
                    )

                    return AvisPhysiqueVue(self.nom_utilisateur).choisir_menu()
                else:
                    print("Vous avez déjà un avis sur ce manga")
                    return AvisPhysiqueVue(self.nom_utilisateur).choisir_menu()

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

                ServiceAvis().modifier_collection_physique(
                    id_utilisateur,
                    id_collection_physique,
                    int(nouvelle_note),
                    nouvel_avis,
                )

                return AvisPhysiqueVue(self.nom_utilisateur).choisir_menu()

            case "Supprimer mon avis":
                avis = ServiceAvis().afficher_avis_collection_physique(id_collection_physique)
                if avis is None:
                    print("Vous n'avez pas encore d'avis sur ce manga")
                    return AvisPhysiqueVue(self.nom_utilisateur).choisir_menu()

                ServiceAvis().supprimer(avis.id_avis)
                return AvisPhysiqueVue(self.nom_utilisateur).choisir_menu()

            case "Retour au menu principal":
                if Session().connecte:
                    return AccueilConnecteVue().choisir_menu()
                else:
                    return AccueilVue().choisir_menu()
