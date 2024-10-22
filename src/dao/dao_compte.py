# dao_compte.py
from business_object.utilisateur import Utilisateur
from utils.singleton import Singleton
from dao.db_connection import DBConnection
from utils.log_decorator import log
import logging


class DaoCompte(metaclass=Singleton):

    def creer_utilisateur(self, utilisateur: Utilisateur) -> bool:
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO utilisateur (nom_utilisateur, mdp)"
                        " VALUES (%(nom_utilisateur)s, %(mdp)s);",
                        {"nom_utilisateur": utilisateur.nom_utilisateur, "mdp": utilisateur.mdp},
                    )

                    # nouvel_id = cursor.fetchone()[0]
                    # connection.commit()
                    return cursor.rowcount > 0
        except Exception as e:
            logging.error(e)
            raise

    def trouver_utilisateur_par_id(self, id_utilisateur: int) -> Utilisateur:

        select_query = """
        SELECT id_utilisateur, nom_utilisateur, mdp FROM utilisateur WHERE id_utilisateur = %(id_utilisateur)s;
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(select_query, {"id_utilisateur": id_utilisateur})
                    res = cursor.fetchone()
        except Exception as e:
            logging.error(e)
            raise

        if res:
            return Utilisateur(
                id_utilisateur=res["id_utilisateur"],
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
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(select_query, {"nom_utilisateur": nom_utilisateur})
                    res = cursor.fetchone()
        except Exception as e:
            logging.error(e)
            raise

        if res:
            return Utilisateur(
                id_utilisateur=res["id_utilisateur"],
                nom_utilisateur=res["nom_utilisateur"],
                mdp=res["mdp"],
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
            with DBConnection().connection as connection:
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
    def supprimer_utilisateur(self, id_utilisateur: int):
        delete_query = """
        DELETE FROM utilisateurs WHERE id = %s;
        """

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(delete_query, (id_utilisateur,))
                connection.commit()
        return True

    @log
    def fermer_connexion(self):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()
