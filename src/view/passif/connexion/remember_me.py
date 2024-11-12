import hashlib
import os
import json


class RememberMe:
    FILE_PATH = "remember_me.json"  # Fichier de sauvegarde des utilisateurs

    @staticmethod
    def generate_salt():
        """Génére un sel unique pour chaque mot de passe"""
        return os.urandom(16)  # Le sel est un nombre aléatoire de 16 octets

    @staticmethod
    def hash_password(password, salt):
        """Hache le mot de passe avec SHA-256 et un sel"""
        # Hachage du mot de passe avec le sel
        hasher = hashlib.sha256()
        hasher.update(salt + password.encode("utf-8"))  # Combinaison du sel et du mot de passe
        return hasher.hexdigest()  # Retourne le mot de passe haché sous forme de chaîne

    @staticmethod
    def check_password(stored_hashed_password, stored_salt, input_password):
        """Vérifie si le mot de passe saisi correspond au mot de passe haché et au sel stocké"""
        input_hashed_password = RememberMe.hash_password(input_password, stored_salt)
        return input_hashed_password == stored_hashed_password

    @staticmethod
    def load_user_data(username):
        """Charge les informations de l'utilisateur depuis 'remember_me.json'"""
        if os.path.exists(RememberMe.FILE_PATH):
            with open(RememberMe.FILE_PATH, "r") as f:
                users_data = json.load(f)
                return users_data.get(username, None)
        return None

    @staticmethod
    def save_user_data(username, password):
        """Sauvegarde les informations de l'utilisateur dans 'remember_me.json'"""
        users_data = {}

        # Vérifier si le fichier existe déjà
        if os.path.exists(RememberMe.FILE_PATH):
            with open(RememberMe.FILE_PATH, "r") as f:
                users_data = json.load(f)

        # Générer un sel unique pour cet utilisateur
        salt = RememberMe.generate_salt()

        # Hacher le mot de passe avec le sel
        hashed_password = RememberMe.hash_password(password, salt)

        # Ajouter ou mettre à jour les informations de l'utilisateur
        users_data[username] = {
            "password": hashed_password,
            "salt": salt.hex(),  # Stocke le sel en hexadécimal
        }

        # Sauvegarder les informations mises à jour
        with open(RememberMe.FILE_PATH, "w") as f:
            json.dump(users_data, f, indent=4)
