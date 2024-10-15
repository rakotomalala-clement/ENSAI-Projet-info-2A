DROP TABLE IF EXISTS collection_coherente CASCADE;
CREATE TABLE collection_coherente(
    id_collection    SERIAL PRIMARY KEY,
    id_utilisateur INTEGER NOT NULL,
    titre_collection VARCHAR(255) UNIQUE NOT NULL,
    description_collection Text,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur) ON DELETE CASCADE
);