from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.connexion_vue import ConnexionVue
from service.Service_Utilisateur import ServiceUtilisateur
from view.passif.accueil_vue import AccueilVue


class InscriptionVue(VueAbstraite):
    "Vue de l'inscription de l'utilisateur et crée sa collection physique"

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

        if len(nom_utilisateur.encode("utf-8")) > 50:
            print("Nom trop long")
            return AccueilVue().choisir_menu()

        mdp = inquirer.secret(
            message="Veuillez saisir un mot de passe selon les condition suivantes: \n"
            + "Au moins 8 caractères \n"
            + "Au moins une majuscule \n"
            + "Au moins un chiffre \n"
            + "Au moins un caractère spécial \n"
        ).execute()

        # Si le mot de passe n'est pas valide
        if not ServiceUtilisateur()._valider_mot_de_passe(mdp):
            return AccueilVue().choisir_menu()

        ServiceUtilisateur().sinscrire(nom_utilisateur, mdp)

        # On va maintenant crée la collection physique lié au nouvel inscrit
        from service.collection_service import ServiceCollection

        id_utilisateur = (
            ServiceUtilisateur().trouver_utilisateur_par_nom(nom_utilisateur).id_utilisateur
        )

        ServiceCollection().creer_collection(
            id_utilisateur=id_utilisateur,
            type_collection="Physique",
            titre="Collection physique",  # ne sert à rien
            description=f"collection_physique de {nom_utilisateur}",  # ne sert à rien
            schema="projet_info_2a",
        )

        return ConnexionVue().choisir_menu()
