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