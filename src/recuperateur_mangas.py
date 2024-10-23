import requests
import time
from service.manga_service import MangaService
import os
import dotenv


class RecuperateurManga:
    def __init__(self, base_url):
        self.base_url = base_url

    def recuperer_data_manga(self):

        dotenv.load_dotenv()

        page = 61
        while True:
            # Construction de l'URL pour chaque page de résultats
            url = f"{self.base_url}?page={page}"

            # Requête "GET"
            response = requests.get(url)

            # Vérification du succès de la requête
            if response.status_code == 200:

                data = response.json()
                mangas = data.get("data")

                # Si plus de mangas dans la réponse, arrêter la boucle
                if not mangas:
                    print("Plus de mangas à récupérer.")
                    break

                # Parcours des mangas de la page actuelle
                for manga in mangas:
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
                    print("Ajout du manga ", manga.get("mal_id"), " : ", status_ajout)

            else:
                print(f"Erreur lors de la récupération de la page {page} :", response.status_code)
                break

            # Passer à la page suivante
            page += 1

            # Attendre 1 seconde pour respecter les contraintes de l'API
            time.sleep(1)


if __name__ == "__main__":

    RecuperateurManga("https://api.jikan.moe/v4/manga").recuperer_data_manga()
