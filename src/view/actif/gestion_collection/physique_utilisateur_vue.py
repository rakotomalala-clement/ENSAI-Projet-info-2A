from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from view.passif.connexion.session import Session
from view.passif.accueil_vue import AccueilVue
from view.actif.accueil_connecte_vue import AccueilConnecteVue
from service.collection_service import ServiceCollection


class PhysiqueUtilisateurVue(VueAbstraite):
    """Menu des modifications possibles sur une collection"""

    def __init__(self, liste_manga):
        # Ici la collection physique est simplement une liste de mangas
        self.liste_manga = liste_manga

    def choisir_menu(self):
        """Modification d'une collection physique

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\n", "Ma collection physique", "\n" + "-" * 50 + "\n")

        print("La suppression de votre collection physique n'est pas possible \n")

        # afficher les mangas de la collection
        if self.liste_manga == "Aucun manga ajouté":
            print("Aucun manga ajouté \n")
        else:
            for manga in self.liste_manga:
                print(manga.titre_manga)
                print(manga.dernier_tome_acquis)
                print(manga.numeros_tomes_manquants)
                print(manga.status_manga)
                print("\n")
            print("\n")

        

        return 0
