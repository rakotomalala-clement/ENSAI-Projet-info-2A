DROP SCHEMA IF EXISTS projet_info_2A CASCADE;
CREATE SCHEMA projet_info_2A;

DROP TABLE IF EXISTS utilisateur CASCADE;
CREATE TABLE utilisateur(
    id_utilisateur    SERIAL PRIMARY KEY,
    nom_utilisateur       VARCHAR(50) UNIQUE NOT NULL,
    mdp          VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS manga CASCADE;
CREATE TABLE manga(
    id_manga    SERIAL PRIMARY KEY,
    titre       VARCHAR(100) UNIQUE NOT NULL,
    auteurs TEXT, 
    genres TEXT,
    status_manga VARCHAR(50),
    chapitres INTEGER
    
);

DROP TABLE IF EXISTS avis CASCADE;
CREATE TABLE avis(
    id_utilisateur INTEGER NOT NULL,
    id_manga INTEGER NOT NULL,
    avis          TEXT,
    note          INTEGER,
    PRIMARY KEY (id_utilisateur, id_manga),
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur) ON DELETE CASCADE,
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga) ON DELETE CASCADE
);

DROP TABLE IF EXISTS collection_coherente CASCADE;
CREATE TABLE collection_coherente(
    id_collection    SERIAL PRIMARY KEY,
    id_utilisateur INTEGER NOT NULL,
    titre_collection VARCHAR(255) UNIQUE NOT NULL,
    description_collection Text,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur) ON DELETE CASCADE
);

DROP TABLE IF EXISTS collection_coherente_mangas CASCADE;
CREATE TABLE collection_coherente_mangas (
    id_collection INTEGER NOT NULL,
    id_manga INTEGER NOT NULL,
    PRIMARY KEY (id_collection, id_manga),
    FOREIGN KEY (id_collection) REFERENCES collection_coherente(id_collection),
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga)
);

DROP TABLE IF EXISTS collection_physique CASCADE;
CREATE TABLE collection_physique(
    id_utilisateur INTEGER NOT NULL,
    id_manga INTEGER NOT NULL,
    titre_collection VARCHAR(50) UNIQUE NOT NULL,
    numero_dernier_tome  INTEGER,
    numeros_tomes_manquants TEXT,
    status_collection VARCHAR(10),
    PRIMARY KEY (id_utilisateur, id_manga),
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur) ON DELETE CASCADE,
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga) ON DELETE CASCADE
);

DROP TABLE IF EXISTS avis_collection_coherente_db CASCADE;
CREATE TABLE avis_collection_coherente_db(
    id_utilisateur INTEGER NOT NULL  ,
    id_collection_coherente INTEGER NOT NULL,
    avis       TEXT UNIQUE,
    note          INTEGER CHECK (note BETWEEN 1 AND 5),
    PRIMARY KEY (id_utilisateur, id_collection_coherente),
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur) ON DELETE CASCADE,
    FOREIGN KEY (id_collection_coherente) REFERENCES collection_coherente(id_collection) ON DELETE CASCADE
);

DROP TABLE IF EXISTS avis_collection_physique_db CASCADE;
CREATE TABLE avis_collection_physique_db(
    id_utilisateur_avis INTEGER NOT NULL  , --L'utilisateur qui donne avis sur la collection
    id_utilisateur_collection INTEGER NOT NULL,  -- L'utilisateur qui a créé la collection
    id_manga INTEGER NOT NULL,
    avis       TEXT UNIQUE,
    note          INTEGER CHECK (note BETWEEN 1 AND 5),
    PRIMARY KEY (id_utilisateur_avis, id_utilisateur_collection, id_manga),
    FOREIGN KEY (id_utilisateur_avis) REFERENCES utilisateur(id_utilisateur) ON DELETE CASCADE,
    FOREIGN KEY (id_utilisateur_collection, id_manga) REFERENCES collection_physique(id_utilisateur, id_manga) ON DELETE CASCADE
);
