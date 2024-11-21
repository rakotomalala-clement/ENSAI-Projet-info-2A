# dao_compte.py

from business_object.utilisateur import Utilisateur
from utils.singleton import Singleton
from dao.db_connection import DBConnection
from utils.log_decorator import log
import logging
import re
from dao.db_connection import DBConnection
import os


class DaoCompte(metaclass=Singleton):

    def _valider_mot_de_passe(self, mot_de_passe: str) -> bool:
        """Vérifie la validité du mot de passe selon des critères de sécurité."""
        if len(mot_de_passe) < 8:
            print("Le mot de passe doit contenir au moins 8 caractères.")
            return False

        if not re.search(r"[A-Z]", mot_de_passe):
            print("Le mot de passe doit contenir au moins une majuscule.")
            return False

        if not re.search(r"\d", mot_de_passe):
            print("Le mot de passe doit contenir au moins un chiffre.")
            return False

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", mot_de_passe):
            print("Le mot de passe doit contenir au moins un caractère spécial.")
            return False

        return True

    def creer_utilisateur(self, utilisateur: Utilisateur) -> bool:
        try:

            if len(utilisateur.nom_utilisateur.encode("utf-8")) > 50:
                print("Nom très long")
                return False
            if not self._valider_mot_de_passe(utilisateur.mdp):
                return False
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO utilisateur (nom_utilisateur, mdp)"
                        " VALUES (%(nom_utilisateur)s, %(mdp)s) RETURNING id_utilisateur ;",
                        {"nom_utilisateur": utilisateur.nom_utilisateur, "mdp": utilisateur.mdp},
                    )

                    # nouvel_id = cursor.fetchone()[0]
                    # connection.commit()
                    res = cursor.fetchone()
                    if res:
                        utilisateur.id_utilisateur = res["id_utilisateur"]
                        return True
                    return False

        except Exception as e:
            logging.error(e)
            raise

    def trouver_utilisateur_par_id(self, id_utilisateur: int) -> Utilisateur:

        select_query = """
        SELECT id_utilisateur, nom_utilisateur, mdp FROM utilisateur WHERE id_utilisateur = %(id_utilisateur)s;
        """
        try:
            with DBConnection("projet_info_2a").connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(select_query, {"id_utilisateur": id_utilisateur})
                    res = cursor.fetchone()
        except Exception as e:
            logging.error(e)
            raise

        if res:
            return Utilisateur(
                nom_utilisateur=res["nom_utilisateur"],
                mdp=res["mdp"],
            )
        return None

    @log
    def trouver_utilisateur_par_nom(self, nom_utilisateur: str) -> Utilisateur:

        select_query = """
        SELECT id_utilisateur, nom_utilisateur, mdp FROM utilisateur WHERE nom_utilisateur = %(nom_utilisateur)s;
        """
        try:
            with DBConnection("projet_info_2a").connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(select_query, {"nom_utilisateur": nom_utilisateur})
                    res = cursor.fetchone()
        except Exception as e:
            logging.error(e)
            raise

        if res:
            return Utilisateur(
                nom_utilisateur=res["nom_utilisateur"],
                mdp=res["mdp"],
                id_utilisateur=res["id_utilisateur"],
            )
        return None

    def mettre_a_jour_utilisateur(
        self, id_utilisateur: int, nom_utilisateur: str, mdp: str
    ) -> bool:

        update_query = """
        UPDATE utilisateur
        SET nom_utilisateur = %(nom_utilisateur)s, mdp = %(mdp)s
        WHERE id_utilisateur = %(id_utilisateur)s;
        """
        try:
            with DBConnection("projet_info_2a").connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        update_query,
                        {
                            "nom_utilisateur": nom_utilisateur,
                            "mdp": mdp,
                            "id_utilisateur": id_utilisateur,
                        },
                    )
                    return cursor.rowcount > 0
        except Exception as e:
            logging.error(e)
            raise

    @log
    def supprimer_utilisateur(self, id_utilisateur: int) -> bool:
        delete_query = """
        DELETE FROM utilisateur WHERE id_utilisateur = %(id_utilisateur)s;
        """

        with DBConnection("projet_info_2a").connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(delete_query, {"id_utilisateur": id_utilisateur})
                connection.commit()
        return True

    def lister_tous(self) -> list[Utilisateur]:

        try:
            with DBConnection("projet_info_2a").connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                              "
                        "  FROM utilisateur;                        "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_utilisateurs = []

        if res:
            for row in res:
                utilisateur = Utilisateur(
                    nom_utilisateur=row["nom_utilisateur"],
                    mdp=row["mdp"],
                )

                liste_utilisateurs.append(utilisateur)

        return liste_utilisateurs
