CREATE TYPE strutturato AS ENUM
(
    'Ricercatore', 
    'Professore Associato', 
    'Professore Ordinario'
);

CREATE TYPE lavoroProgetto AS ENUM
(
    'Ricerca e Sviluppo', 
    'Dimostrazione', 
    'Management', 
    'Altro'
);

CREATE TYPE lavoroNonProgettuale AS ENUM
(
    'Didattica', 
    'Ricerca', 
    'Missione', 
    'Incontro Dipartimentale', 
    'Incontro Accademico', 
    'Altro'
);

CREATE TYPE causaAssenza AS ENUM
(
    'Chiusura Universitaria',
    'Maternità',
    'Malattia'
);

-- Creazione dei domini
CREATE DOMAIN PosInteger AS INTEGER CHECK 
(
    VALUE >= 0
);
CREATE DOMAIN StringaM AS VARCHAR(100);

CREATE DOMAIN NumeroOre AS INTEGER CHECK
(
    VALUE BETWEEN 0 AND 8
);

CREATE DOMAIN Denaro AS REAL CHECK 
(
    VALUE >= 0
);

-- Creazione dello schema e delle tabelle
CREATE SCHEMA accademia;

    CREATE TABLE accademia.persona 
    (
        id PosInteger PRIMARY KEY,
        nome StringaM NOT NULL,
        cognome StringaM NOT NULL,
        posizione Strutturato NOT NULL,
        stipendio Denaro NOT NULL 
    );

    CREATE TABLE accademia.progetto 
    (
        id PosInteger PRIMARY KEY,               
        nome StringaM NOT NULL,                 
        inizio DATE NOT NULL,                   
        fine DATE,                        
        budget Denaro NOT NULL, 
        CONSTRAINT Progetto_inizio_fine CHECK (inizio < fine)
    );

    CREATE TABLE accademia.wp 
    (
        progetto PosInteger,
        id PosInteger,
        nome StringaM NOT NULL,
        inizio DATE NOT NULL,
        fine DATE,
        PRIMARY KEY (progetto, id), 
        CONSTRAINT WP_inizio_fine CHECK (inizio < fine),
        UNIQUE (progetto, nome),
        CONSTRAINT fk_progetto FOREIGN KEY (progetto) REFERENCES accademia.progetto(id)
    );

    CREATE TABLE accademia.attivitaProgetto 
    (
        id PosInteger PRIMARY KEY,
        persona PosInteger,
        progetto PosInteger,
        wp PosInteger,
        giorno DATE NOT NULL,
        tipo LavoroProgetto NOT NULL,
        oreDurata NumeroOre NOT NULL,
        CONSTRAINT fk_persona_ap FOREIGN KEY (persona) REFERENCES accademia.persona(id), 
        CONSTRAINT fk_progetto_wp FOREIGN KEY (progetto, wp) REFERENCES accademia.wp(progetto, id)
    );

    CREATE TABLE accademia.attivitàNonProgettuale
    (
        id PosInteger PRIMARY KEY,
        nome StringaM NOT NULL,
        cognome StringaM NOT NULL,
        posizione Strutturato NOT NULL,
        stipendio Denaro NOT NULL,
        CONSTRAINT fk_persona_anp FOREIGN KEY (persona) REFERENCES accademia.persona(id)
    );

    CREATE TABLE accademia.assenza 
    (
        id PosInteger PRIMARY KEY,
        persona PosInteger NOT NULL,
        tipo CausaAssenza NOT NULL,
        giorno DATE NOT NULL,
        UNIQUE (persona, giorno),
        CONSTRAINT fk_persona_assenza FOREIGN KEY (persona) REFERENCES accademia.persona(id)
    );

-- Query di esempio
SELECT DISTINCT P.nome, P.cognome, A.giorno, PR.nome AS nome_progetto, A.tipo AS causa_assenza, 
       AP.oreDurata AS ore_attivita_progetto
FROM accademia.persona P
    JOIN accademia.attivitaProgetto AP 
        ON P.id = AP.persona
    JOIN accademia.progetto PR 
        ON AP.progetto = PR.id
    JOIN accademia.assenza A 
        ON P.id = A.persona
WHERE AP.giorno = A.giorno;
