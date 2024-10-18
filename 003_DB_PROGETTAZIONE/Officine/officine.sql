-- DOMAIN --------------------------------------------------------------------------------------------------

CREATE DOMAIN PosInteger AS INTEGER
    CHECK (VALUE >= 0);

CREATE DOMAIN Stringa_255 AS VARCHAR(255);

CREATE DOMAIN Stringa_100 AS VARCHAR(100);

CREATE DOMAIN Stringa_50 AS VARCHAR(50);

CREATE DOMAIN Stringa_10 AS VARCHAR(10);

CREATE DOMAIN CodicePostale AS CHAR(5);


-- SCHEMA --------------------------------------------------------------------------------------------------

CREATE SCHEMA officine
    CREATE TABLE Nazione
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        nome Stringa_100 NOT NULL
    }
    
    CREATE TABLE Regione
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        nome Stringa_100 NOT NULL,
        TAB_Nazione_id PosInteger NOT NULL,
        FOREIGN KEY (TAB_Nazione_id) REFERENCES Nazione(id)
    }
    
    CREATE TABLE Città
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        nome Stringa_100 NOT NULL,
        TAB_Regione_id PosInteger NOT NULL,
        FOREIGN KEY (TAB_Regione_id) REFERENCES Regione(id)
    }

    CREATE TABLE Indirizzo
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
        via Stringa_225 NOT NULL,
        num_civ Stringa_10 NOT NULL,
        città Stringa_100 NOT NULL,
        provincia Stringa_100 NOT NULL,
        cod_pos CodicePostale NOT NULL
    }
    
    CREATE TABLE Officina
    {
        id Posinteger primary key AUTO_INCREMENT,
        nome Stringa_50 not null,
        indirizzo Stringa_100 not null,
        id_TAB_Città PosInteger not null,
    }
    
    CREATE TABLE Incarico
    {
        id INT PRIMARY KEY AUTO_INCREMENT
        nome VARCHAR(50) NOT NULL
    }

    CREATE TABLE Rel_Staff
    {
        id_TAB_Officina INT,
        id_TAB_ INT,
        FOREIGN KEY (id_TAB_Officina, id_TAB_Persona)
    }
    
    CREATE TABLE Staff_Direzione
    {
        ID_Rel_Staff/id_Officina
        id_Direttore
    }

    CREATE TABLE Staff_Dipendenti
    {
        ID_Rel_Staff/id_Officina
        id_Dipendente
    }
    
    CREATE TABLE Direttore
    {
        nascita date not null,
    }
    
    CREATE TABLE Dipendente
    {
        nascita date not null,
    }
    
    CREATE TABLE Cliente
    {
        nascita date not null,
    }
    
    CREATE TABLE Persona
    {
        
    }

    CREATE TABLE Riparazione
    {
        id Posinteger 
    }

    CREATE TABLE Riparazione_Termini
    {
        
    }

    CREATE TABLE Veicolo
    {
        
    }

    CREATE TABLE Veicolo_Tipo
    {
        
    }

    CREATE TABLE Veicolo_Marca
    {
        
    }

    CREATE TABLE Veicolo_Modello
    {
        
    }