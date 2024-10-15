DROP TABLE IF EXISTS utilisateur CASCADE;
CREATE TABLE utilisateur(
    id_utilisateur    SERIAL PRIMARY KEY,
    nom_utilisateur       VARCHAR(50) UNIQUE NOT NULL,
    mdp          VARCHAR(50) NOT NULL
);