DROP TABLE IF EXISTS collection_coherente_mangas CASCADE;
CREATE TABLE collection_coherente_mangas (
    id_collection INTEGER NOT NULL,
    id_manga INTEGER NOT NULL,
    PRIMARY KEY (id_collection, id_manga),
    FOREIGN KEY (id_collection) REFERENCES collection_coherente(id_collection),
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga)
);