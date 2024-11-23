from view.passif.accueil_vue import AccueilVue
import os
import logging
import logging.config
import yaml


if __name__ == "__main__":
    """Initialiser les logs à partir du fichier de config"""

    # Création du dossier logs à la racine si non existant
    os.makedirs("logs", exist_ok=True)

    stream = open("logging_config.yml", encoding="utf-8")
    config = yaml.load(stream, Loader=yaml.FullLoader)
    logging.config.dictConfig(config)

    logging.info("-" * 50)
    logging.info(f"Lancement MangaCollect                          ")
    logging.info("-" * 50)

    AccueilVue().choisir_menu()
