import os
import logging
import dotenv
from unittest import mock

from utils.log_decorator import log
from utils.singleton import Singleton
from dao.db_connection import DBConnection
from service.Service_Utilisateur import ServiceUtilisateur


class ResetDatabase(metaclass=Singleton):
    """
    Reinitialisation de la base de données
    """

    @log
    def lancer(self, test_dao=False):
        """Lancement de la réinitialisation des données
        Si test_dao = True : réinitialisation des données de test"""

        dotenv.load_dotenv()

        if test_dao:
            # Sauvegarder la valeur actuelle de la variable d'environnement
            original_schema = os.environ.get("POSTGRES_SCHEMA")

            # Patch the environment variable to override POSTGRES_SCHEMA for test schema
            with mock.patch.dict(os.environ, {"POSTGRES_SCHEMA": "projet_test_dao"}):
                schema = os.environ.get("POSTGRES_SCHEMA")
                pop_data_path = "data/pop_db_test.sql"
                create_schema = f"DROP SCHEMA IF EXISTS {schema} CASCADE; CREATE SCHEMA {schema};"

                # Initialize and populate the test database
                with open("data/init_db.sql", encoding="utf-8") as init_db:
                    init_db_as_string = init_db.read()

                with open(pop_data_path, encoding="utf-8") as pop_db:
                    pop_db_as_string = pop_db.read()

                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(create_schema)
                            cursor.execute(init_db_as_string)
                            cursor.execute(pop_db_as_string)
                except Exception as e:
                    logging.info(e)
                    raise

                # Perform user modifications in the test schema
                utilisateur_service = ServiceUtilisateur()
                for u in utilisateur_service.lister_tous(inclure_mdp=True):

                    print(utilisateur_service.modifier(u))
                    print("mdp : ", u.mot_de_passe)

            # Restorer la valeur initiale de la variable d'environnement
            os.environ["POSTGRES_SCHEMA"] = original_schema

            return True

        else:

            schema = os.environ.get("POSTGRES_SCHEMA")
            create_schema = f"DROP SCHEMA IF EXISTS {schema} CASCADE; CREATE SCHEMA {schema};"

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

            return True


if __name__ == "__main__":
    # Run with the test schema
    print(ResetDatabase().lancer(True))

   # ResetDatabase().lancer()
