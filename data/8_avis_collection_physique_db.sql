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

