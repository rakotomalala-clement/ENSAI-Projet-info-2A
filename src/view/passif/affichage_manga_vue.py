from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue


class AffichageMangaVue(VueAbstraite):
    "Vue des informations sur le manga"

    def __init__(self, titre):
        self.titre = titre

    def choisir_menu(self):
        """Affichage des details du manga

        Return
        ------
        view
            Retourne la view de l'acceuil
        """

        print("\n" + "-" * 50 + "\nDétails du manga\n" + "-" * 50 + "\n")

        print(self.titre)

        # Instanciation de notre objet Manga
        from service.manga_service import MangaService

        manga = MangaService().trouver_par_titre(self.titre)

        # Si le nom du manga n'existe pas
        if not manga:
            print("Le manga recherché n'est pas dans notre base de données")
            if Session().connecte:
                return AccueilConnecteVue().choisir_menu()
            else:
                return AccueilVue().choisir_menu()

        auteurs = manga.auteurs
        status = manga.status

        print("auteur(s): ", auteurs)
        print("Etat de la diffusion du manga: ", status)

        # Insertion des avis
        from service.avis_service import ServiceAvis

        id_manga = manga.id_manga
        print(ServiceAvis().afficher_autre_avis(id_manga))

        if Session().connecte:
            possibilites = ["Gérer ses avis sur ce manga", "Revenir au menu principal", "Quitter"]
        else:
            possibilites = ["Revenir au menu principal", "Quitter"]

        choix = inquirer.select(message="", choices=possibilites).execute()

        match choix:
            case "Gérer ses avis sur ce manga":
                from view.actif.avis.avis_manga_vue import AvisMangaVue

                return AvisMangaVue(self.titre).choisir_menu()

            case "Revenir au menu principal":

                # Vérifie si l'utilisateur est connecté ou non
                if Session().connecte:
                    return AccueilConnecteVue().choisir_menu()
                else:
                    return AccueilVue().choisir_menu()

            case "Quitter":
                pass
