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