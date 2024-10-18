-- DOMAIN --------------------------------------------------------------------------------------------------

CREATE DOMAIN PosInteger AS INTEGER
    CHECK (VALUE >= 0);

CREATE DOMAIN Stringa_500 AS VARCHAR(500));

CREATE DOMAIN Stringa_255 AS VARCHAR(255);

CREATE DOMAIN Stringa_100 AS VARCHAR(100);

CREATE DOMAIN Stringa_50 AS VARCHAR(50);

CREATE DOMAIN Stringa_20 AS VARCHAR(20);

CREATE DOMAIN Stringa_10 AS VARCHAR(10);

CREATE DOMAIN CodicePostale AS CHAR(5);

CREATE DOMAIN Datetime AS VARCHAR(19)
    CHECK (VALUE REGEXP '^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$');

CREATE DOMAIN Codicefiscale AS VARCHAR(16)
    CHECK (VALUE REGEXP '^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$');

CREATE DOMAIN datanascita AS DATE
    CHECK (VALUE REGEXP '^\d{4}-\d{2}-\d{2}$');

CREATE DOMAIN censura AS INT
    CHECK (VALUE < 70);

CREATE DOMAIN Cat_level AS INTEGER
    CHECK (VALUE > 0)

CREATE DOMAIN Voto AS INTEGER
    CHECK (VALUE BETWEEN 1 AND 5);

   

-- SCHEMA --------------------------------------------------------------------------------------------------

CREATE SCHEMA Tutubi
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
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        via Stringa_225 NOT NULL,
        num_civ Stringa_10 NOT NULL,
        città Stringa_100 NOT NULL,
        provincia Stringa_100 NOT NULL,
        cod_pos CodicePostale NOT NULL
    }

    CREATE TABLE Utente
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        username Stringa_50 NOT NULL,
        nome Stringa_100 NOT NULL,
        cognome Stringa_100 NOT NULL,
        iscrizione Datetime NOT NULL,
        CF Codicefiscale NOT NULL,
        datanascita datanascita NOT NULL,
        set_censura censura NOT NULL

        TAB_città_nascita PosInteger NOT NULL
        TAB_indirizzo PosInteger NOT NULL
        FOREIGN KEY (TAB_città_nascita) REFERENCES Città(id)
        FOREIGN KEY (TAB_Indirizzo) REFERENCES Indirizzo(id)
        
    }

    CREATE TABLE Hashtag
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
        hashtag Stringa_50 NOT NULL
    }

    CREATE TABLE Codec
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
        nome Stringa_10 NOT NULL
        tipo_file Stringa_20 NOT NULL
        descrizione Stringa
    }

    CREATE TABLE Formato
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
        formato Stringa_10 NOT NULL
    }

    CREATE TABLE Categoria
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
        id_Cat_Up INT
        id_Cat_Down INT
        nome Stringa_20 NOT NULL
        descrizione Stringa_100 NOT NULL
        livello Cat_level INT
    }

    CREATE TABLE Playlist
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT

        TAB_Categoria PosInteger NOT NULL
        FOREIGN KEY (TAB_Categoria) REFERENCES Categoria(id)
    }

        CREATE TABLE REL_Playlist
    {
        TAB_Utente PosInteger NOT NULL
        TAB_Playlist PosInteger NOT NULL
        TAB_Video PosInteger NOT NULL
        FOREIGN KEY (TAB_Utente) REFERENCES Utente(id)
        FOREIGN KEY (TAB_Playlist) REFERENCES Playlist(id)
        FOREIGN KEY (TAB_Video) REFERENCES Video(id)
    }

    CREATE TABLE Visualizzazione
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
        boolutente BOOLEAN 

        TAB_Utente PosInteger NOT NULL
        TAB_Video PosInteger NOT NULL
        FOREIGN KEY (TAB_Utente) REFERENCES Utente(id)
        FOREIGN KEY (TAB_Video) REFERENCES Video(id)
    }

    CREATE TABLE Valutazione (
        TAB_Utente PosInteger NOT NULL,
        TAB_Video PosInteger NOT NULL,
        voto Voto NOT NULL,
        PRIMARY KEY (TAB_Utente, TAB_Video),
        FOREIGN KEY (TAB_Utente) REFERENCES Utente(id),
        FOREIGN KEY (TAB_Video) REFERENCES Video(id)
    }


    CREATE TABLE Commento
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT

        TAB_Utente PosInteger NOT NULL,
        TAB_Video PosInteger NOT NULL,
        FOREIGN KEY (TAB_Utente) REFERENCES Utente(id),
        FOREIGN KEY (TAB_Video) REFERENCES Video(id)
    }

    CREATE TABLE REL_Commento
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
        commento Stringa_500 NOT NULL

        TAB_Utente PosInteger NOT NULL,
        TAB_Commento PosInteger NOT NULL,
        FOREIGN KEY (TAB_Utente) REFERENCES Utente(id),
        FOREIGN KEY (TAB_Commento) REFERENCES Commento(id)

    }

    CREATE TABLE Tipo_Segnalazione
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
        nome Stringa_50 NOT NULL
    }

    CREATE TABLE Segnalazione
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT

        TAB_Tipo_Segnalazione PosInteger NOT NULL
        FOREIGN KEY (TAB_Tipo_Segnalazione) REFERENCES Tipo_Segnalazione(id)
    }

    CREATE TABLE Moderatore
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
        nome Stringa_50 NOT NULL
        codice Stringa_50 NOT NULL
    }

    CREATE TABLE Moderazione
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
        istante DATE NOT NULL
        relazione Stringa_500 NOT NULL

        TAB_Moderatore PosInteger NOT NULL
        FOREIGN KEY (TAB_Moderatore) REFERENCES Moderatore(id)

    }

    CREATE TABLE Video
    {
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT

        TAB_Hashtag PosInteger NOT NULL
        TAB_Codec PosInteger NOT NULL
        TAB_Formato PosInteger NOT NULL
        TAB_Categoria PosInteger NOT NULL
        FOREIGN KEY (TAB_Hashtag) REFERENCES Hashtag(id)
        FOREIGN KEY (TAB_Codec) REFERENCES Codec(id)
        FOREIGN KEY (TAB_Formato) REFERENCES Formato(id)
        FOREIGN KEY (TAB_Categoria) REFERENCES Categoria(id)

    }

    