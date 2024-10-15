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