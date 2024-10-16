import requests
import time


def fetch_all_mangas():
    url = "https://api.jikan.moe/v4/manga"
    page = 1
    all_mangas = []
    count = 0
    while count < 10:
        # Requête GET pour chaque page avec gestion des erreurs
        try:
            response = requests.get(url, params={"page": page})
            response.raise_for_status()  # Lance une exception pour les codes d'erreur HTTP
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête de la page {page}: {e}")
            break

        # Récupération des données JSON
        data = response.json()

        # Gestion de la pagination en utilisant 'last_visible_page' pour arrêter les requêtes
        pagination_info = data.get("pagination", {})
        last_page = pagination_info.get("last_visible_page", 1)

        # Récupère les mangas de la page actuelle
        mangas = data.get("data", [])
        if not mangas:
            print("Fin des pages atteinte ou aucun manga disponible.")
            break

        # Ajouter les mangas récupérés à la liste totale
        all_mangas.extend(mangas)
        print(f"Page {page}/{last_page} récupérée avec succès, {len(mangas)} mangas.")

        # Passage à la page suivante, arrêt si dernière page atteinte
        if page >= last_page:
            print("Toutes les pages ont été récupérées.")
            break

        # Pause de 2 secondes pour respecter la limite de requêtes
        time.sleep(2)  # Ajustez le temps de pause si nécessaire
        page += 1
        count += 1

    # Affiche le nombre total de mangas récupérés
    print(f"Nombre total de mangas récupérés : {len(all_mangas)}")
    return all_mangas


# Appeler la fonction pour récupérer tous les mangas
all_mangas = fetch_all_mangas()

# Afficher les informations des 5 premiers mangas
for manga in all_mangas[:5]:
    print("Titre:", manga.get("title"))

    print("-" * 40)
