from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session
from view.passif.accueil_vue import AccueilVue
from view.actif_accueil_connecte import AccueilConnecteVue


class AffichageMangaVue(VueAbstraite):
    "Vue des informations sur la collection"

    def __init__(self, titre):
        self.titre = titre

    def choisir_menu(self):
        """Affichage des details de la collection

        Return
        ------
        view
            Retourne la view de l'acceuil
        """

        print("\n" + "-" * 50 + "\nDétails de la collection\n" + "-" * 50 + "\n")

        # collection.TimeoutError

        # possibilites = mangas de la collection
        # possibilites.append("Gestion Avis")
        # possibilites.append("Retour au menu")
