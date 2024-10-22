import requests
import time
from service.manga_service import MangaService
import os
import dotenv


class RecuperateurManga:
    def __init__(self, base_url):
        self.base_url = base_url

    def recuperer_data_manga(self, start_id=1, end_id=5):

        dotenv.load_dotenv()

        for id_manga in range(start_id, end_id + 1):
            # Construction de l'URL pour chaque manga (via son id)
            url = f"{self.base_url}/{id_manga}"

            # Requete "GET"
            response = requests.get(url)

            # Vérification du succès de la requete
            if response.status_code == 200:

                data = response.json()
                manga = data.get("data")

                # Gestion du cas où la valeur du champ est nulle
                if manga:
                    title = manga.get("title") or "information non renseignée"
                    authors = manga.get("authors", [])
                    author_names = " - ".join(
                        author.get("name") or "information non renseignée" for author in authors
                    )
                    genres = manga.get("genres", [])
                    genres_names = " - ".join(
                        genre.get("name") or "information non renseignée" for genre in genres
                    )

                    # Status
                    status = manga.get("status")
                    if status == "Publishing":
                        status = "en cours de publication"
                    elif status == "Finished":
                        status = "terminé"
                    else:
                        status = "information non renseignée"

                    chapters = manga.get("chapters") or "0"

                    # Ajout du manga dans la base de données
                    status_ajout = MangaService().ajouter_manga(
                        title, author_names, genres_names, status, chapters
                    )
                    print("Ajout du manga ", id_manga, " : ", status_ajout)

            else:
                print(
                    f"Erreur lors de la récupération du manga ID {id_manga} :", response.status_code
                )

            # Attendre 1 sec pour respecter les contraintes de l'API
            time.sleep(1)


if __name__ == "__main__":

    RecuperateurManga("https://api.jikan.moe/v4/manga").recuperer_data_manga()
