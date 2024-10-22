import os
import psycopg2
import dotenv


def test_db_connection():
    dotenv.load_dotenv()

    conn = None
    cursor = None  # Initialise cursor à None
    print("hello ****************")

    try:
        conn = psycopg2.connect(
            host=os.environ["POSTGRES_HOST"],
            port=os.environ["POSTGRES_PORT"],
            database=os.environ["POSTGRES_DATABASE"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            options="-c search_path=projet_test_dao",  # Remplace par ton schéma
        )

        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM utilisateur LIMIT 1;"
        )  # Remplace 'some_table' par une table existante
        print(cursor.fetchall())
    except Exception as e:
        print(f"Database connection error: {e}")
    finally:
        if cursor:  # Vérifie si cursor a été initialisé avant de le fermer
            cursor.close()
        if conn:  # Vérifie si conn a été initialisé avant de le fermer
            conn.close()


if __name__ == "__main__":
    test_db_connection()
