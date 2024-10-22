import os
import dotenv

# Charger les variables d'environnement à partir du fichier .env
dotenv.load_dotenv()

# Vérifiez que les variables d'environnement sont correctement chargées
print("Chargement des variables d'environnement :")
print("POSTGRES_HOST:", os.environ.get("POSTGRES_HOST"))
print("POSTGRES_PORT:", os.environ.get("POSTGRES_PORT"))
print("POSTGRES_DATABASE:", os.environ.get("POSTGRES_DATABASE"))
print("POSTGRES_USER:", os.environ.get("POSTGRES_USER"))
print("POSTGRES_PASSWORD:", os.environ.get("POSTGRES_PASSWORD"))
print("POSTGRES_SCHEMA:", os.environ.get("POSTGRES_SCHEMA"))
