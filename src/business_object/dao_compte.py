# dao_compte.py
import logging
from Utilisateur import Utilisateur
from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object import Utilisateur
from dao.db_connection import DBConnection

class DaoCompte(metaclass=Singleton):

    def creer_table_utilisateur(self):

        create_table_query = """
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id SERIAL PRIMARY KEY,
            nom_utilisateur VARCHAR(100) NOT NULL UNIQUE,
            mot_de_passe VARCHAR(100) NOT NULL
        );
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(create_table_query)
                connection.commit()

    def creer_utilisateur(self, nom_utilisateur: str, mot_de_passe: str):

        insert_query = """
        INSERT INTO utilisateurs (nom_utilisateur, mot_de_passe)
        VALUES (%s, %s) RETURNING id;
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(insert_query, (nom_utilisateur, mot_de_passe))
                nouvel_id = cursor.fetchone()[0]
                connection.commit()

        return Utilisateur(nouvel_id, nom_utilisateur, mot_de_passe)

    def trouver_utilisateur_par_id(self, id_utilisateur: int):

        select_query = """
        SELECT id, nom_utilisateur, mot_de_passe FROM utilisateurs WHERE id = %s;
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(select_query, (id_utilisateur,))
                utilisateur = cursor.fetchone()
                if utilisateur:
                    return Utilisateur(utilisateur[0], utilisateur[1], utilisateur[2])
                return None

    def trouver_utilisateur_par_nom(self, nom_utilisateur: str):

        select_query = """
        SELECT id, nom_utilisateur, mot_de_passe FROM utilisateurs WHERE nom_utilisateur = %s;
        """

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(select_query, (nom_utilisateur,))
                utilisateur = cursor.fetchone()
                if utilisateur:
                    return Utilisateur(utilisateur[0], utilisateur[1], utilisateur[2])
                return None

    def mettre_a_jour_utilisateur(self, id_utilisateur: int, nouveau_nom: str, nouveau_mdp: str):
        update_query = """
        UPDATE utilisateurs
        SET nom_utilisateur = %s, mot_de_passe = %s
        WHERE id = %s;
        """

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(update_query, (nouveau_nom, nouveau_mdp, id_utilisateur))
                connection.commit()

                return self.trouver_utilisateur_par_id(id_utilisateur)

    def supprimer_utilisateur(self, id_utilisateur: int):
        delete_query = """
        DELETE FROM utilisateurs WHERE id = %s;
        """

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(delete_query, (id_utilisateur,))
                connection.commit()
        return True

    def fermer_connexion(self):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.close()
                connection.close()
