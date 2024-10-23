import os
import psycopg2
import dotenv
from psycopg2.extras import RealDictCursor
from utils.singleton import Singleton


class DBConnection(metaclass=Singleton):
    """Classe de connexion à la base de données"""

    def __init__(self, schema=None):
        """Ouverture de la connexion avec un schéma optionnel"""
        dotenv.load_dotenv()

        self.__connection = psycopg2.connect(
            host=os.environ["POSTGRES_HOST"],
            port=os.environ["POSTGRES_PORT"],
            database=os.environ["POSTGRES_DATABASE"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            options=f"-c search_path={schema or os.environ['POSTGRES_SCHEMA']}",
            cursor_factory=RealDictCursor,
        )

    @property
    def connection(self):
        return self.__connection
