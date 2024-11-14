# ENSAI-Projet-info-2A groupe 21

## :arrow_forward: Required Software

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python 3.10](https://www.python.org/)
- [Git](https://git-scm.com/)
- A [PostgreSQL](https://www.postgresql.org/) database

---

This project involves the development of an application dedicated to managing and sharing manga collections. Its main goal is to provide users with the ability to create personalized collections, exchange reviews on their favorite manga, and view collections shared by other members of the community. The application offers several essential features, such as user management (registration, login, logout, account deletion), as well as manga searches via the Jikan API, which is an API for MyAnimeList.net. Jikan retrieves information from the site to fill the functional gaps of the official MyAnimeList.net API, enabling detailed information on each title.

Additionally, the application allows users to create, update, and delete thematic collections (lists of favorite manga, recommended series) and physical collections (owned manga, recently acquired volumes, series status). Users can also write, edit, and delete reviews of manga while accessing critiques shared by the community.

The architecture of the application is based on an object-oriented programming (OOP) approach, ensuring a modular and scalable organization. Each feature is modeled by distinct classes, facilitating the integration of new options in the future. Moreover, the application must comply with the technical constraints of the API, including request rate limits, by optimizing external call management.

This application features a very basic graphical interface for navigating between different menus.

How to install it?

## :arrow_forward: Clone the Repository

- [ ] Open **Git Bash**
- [ ] Create a folder `P:/Cours2A/UE3-Projet-info` and navigate to it
  - `mkdir -p /p/Cours2A/UE3-Projet-info && cd $_`
- [ ] Clone this repository
  - `git clone https://github.com/rakotomalala-clement/ENSAI-Projet-info-2A.git`

---

## :arrow_forward: Open the Repository with VSCode

- [ ] Open **Visual Studio Code**
- [ ] File > Open Folder
- [ ] Click once on *ENSAI-Projet-info-2A* and select `Select Folder`

### Launch the Application

You can now run the application, the web service, or the unit tests:

- `python src/__main__.py` (then start by re-initializing the database)
- `python src/app.py` (to be tested)
- `pytest -v`