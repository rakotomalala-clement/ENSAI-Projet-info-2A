import os
import logging
import dotenv
from unittest import mock
from utils.log_decorator import log
from utils.singleton import Singleton
from dao.db_connection import DBConnection


class ResetDatabase(metaclass=Singleton):
    """
    Reinitialisation de la base de données
    """

    @log
    def lancer(self, test_dao=False):
        """Lancement de la création de la base de données
        Si test_dao = True : création de la base de données de test"""

        dotenv.load_dotenv()

        if test_dao:
            # Sauvegarde de la valeur actuelle de la variable d'environnement
            original_schema = os.environ.get("POSTGRES_SCHEMA")

            # Modification de la variable d'environnement pour remplacer POSTGRES_SCHEMA par le schéma de test
            with mock.patch.dict(os.environ, {"POSTGRES_SCHEMA": "projet_test_dao"}):
                schema = os.environ.get("POSTGRES_SCHEMA")
                create_schema = f"DROP SCHEMA IF EXISTS {schema} CASCADE; CREATE SCHEMA {schema};"

                # Initialisation de la base de données de test
                with open("data/init_db.sql", encoding="utf-8") as init_db:
                    init_db_as_string = init_db.read()

                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(create_schema)
                            cursor.execute(init_db_as_string)

                except Exception as e:
                    logging.info(e)
                    raise

            # Restoration la valeur initiale de la variable d'environnement
            os.environ["POSTGRES_SCHEMA"] = original_schema

            return True

        else:
            # Initialisation de la base de données du projet
            schema = os.environ.get("POSTGRES_SCHEMA")
            create_schema = f"DROP SCHEMA IF EXISTS {schema} CASCADE; CREATE SCHEMA {schema};"

            with open("data/init_db.sql", encoding="utf-8") as init_db:
                init_db_as_string = init_db.read()

            try:
                with DBConnection(schema).connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(create_schema)
                        cursor.execute(init_db_as_string)
            except Exception as e:
                logging.info(e)
                raise

            return True


if __name__ == "__main__":

    ResetDatabase().lancer(True)
