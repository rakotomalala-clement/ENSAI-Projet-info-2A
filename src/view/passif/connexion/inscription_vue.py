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

        mdp = inquirer.secret(message="Veuillez saisir un mot de passe").execute()

        ServiceUtilisateur().sinscrire(nom_utilisateur, mdp)

        # On va maintenant crée la collection physique lié au nouvel inscrit
        from service.collection_service import ServiceCollection

        id_utilisateur = (
            ServiceUtilisateur().trouver_utilisateur_par_nom(nom_utilisateur).id_utilisateur
        )

        ServiceCollection().creer_collection(
            id_utilisateur=id_utilisateur,
            type_collection="Physique",
            titre="Collection physique",
            description=f"collectio_physique de {nom_utilisateur}",
            dernier_tome_acquis=None,
            numeros_tomes_manquants=None,
            status=None,
            schema="projet_info_2a",
        )

        return ConnexionVue().choisir_menu()
