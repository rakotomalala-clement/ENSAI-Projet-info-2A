DROP TABLE IF EXISTS manga CASCADE;
CREATE TABLE manga(
    id_manga    SERIAL PRIMARY KEY,
    titre       VARCHAR(100) UNIQUE NOT NULL,
    auteurs TEXT, 
    genres TEXT,
    statut BOOLEAN,
    nombre_chapitres INTEGER
    
);