--cielo/cielo.sql

create domain PosInteger as integer check 
(
    VALUE >= 0
);

create domain StringaM as varchar
(
    100
);

create domain codIATA as char
(
    100
);

CREATE SCHEMA cielo
    CREATE TABLE Volo 
    (
        codice Posinteger primary key,
        comp StringaM not null 
        durataMinuti PosInteger not null 
        foreign key (codice,comp) references ArrPart (codice,comp)
    );









    create table progetto 
    (
        id PosInteger primary key,               
        nome StringaM not null,                 
        inizio date not null,                   
        fine date,                        
        budget Denaro not null, 
        constraint Progetto_inizio_fine check (inizio < fine)
    );
    create table wp 
    (
        progetto PosInteger,
        id Posinteger,
        nome StringaM not null
        inizio date not null,
        fine date,
        primary_key (progetto, id), 
        constraint WP_inizio_fine check (inizio < fine),
        unique (progetto, nome),
        constraint fk_progetto foreign key (progetto)references Progetto(id)
    );

    create table attivitaProgetto 
    (
        id Posinteger primary key,
        persona PosInteger
        progetto PosInteger
        wp PosInteger
        giorno date not null
        tipo LavoroProgetto not null
        oreDurata NumeroOre not null
        constraint fk_persona_ap foreign key (persona) references Persona(id), 
        constraint fk_progetto_wp foreign key (progetto, wp) references WP(progetto, id)
    );

    create table attivitàNonProgettuale
    (
        id Posinteger primary key,
        nome StringaM not null
        cognome StringaM not null
        posizione Strutturato not null
        stipendio Denaro not null
        constraint fk_persona_anp foreign key (persona) references Persona(id)
    );

    create table assenza 
    (
        Assenza (id: PosInteger, persona: PosInteger, tipo: CausaAssenza, giorno: date)

        id Posinteger PRIMARY KEY,
        persona PosInteger NOT NULL
        tipo CausaAssenza NOT NULL
        giorno date NOT NULL
        unique (persona, giorno),
        constraint fk_persona_assenza foreign key (persona) references Persona(id)
    );

"""

Schema relazionale con vincoli della base dati

Persona (id: PosInteger, nome: StringaM, cognome: StringaM, posizione: Strutturato, stipendio: Denaro)
Progetto (id: PosInteger, nome: StringaM, inizio: date, fine: date, budget:
Denaro)
[VincoloDB.1] altra chiave: (nome)
[VincoloDB.2] ennupla: inizio < fine
WP (progetto: PosInteger, id: PosInteger, nome: StringaM, inizio: date, fine:
date)
[VincoloDB.3] ennupla: inizio < fine
[VincoloDB.4] altra chiave: (progetto, nome)
[VincoloDB.5] foreign key: progetto references Progetto(id)
AttivitaProgetto (id: PosInteger, persona: PosInteger, progetto: PosInteger,
wp: PosInteger, giorno: date, tipo: LavoroProgetto, oreDurata: NumeroOre)
[VincoloDB.6] foreign key: persona references Persona(id)
[VincoloDB.7] foreign key: (progetto, wp) references WP(progetto, id)
AttivitaNonProgettuale (id: PosInteger, persona: PosInteger, tipo: LavoroNonProgettuale, giorno: date, oreDurata: NumeroOre)
[VincoloDB.8] foreign key: persona references Persona(id)
Assenza (id: PosInteger, persona: PosInteger, tipo: CausaAssenza, giorno: date)
[VincoloDB.9] altra chiave: persona, giorno
[VincoloDB.10] foreign key: persona references Persona(id)


Il database Accademia è definito sul seguente insieme di domini e sul seguente schema
relazionale con vincoli.
Definizione dei domini
• Strutturato
enum (’Ricercatore’, ’Professore Associato’, ’Professore Ordinario’)
• LavoroProgetto
enum (’Ricerca e Sviluppo’, ’Dimostrazione’, ’Management’, ’Altro’)
• LavoroNonProgettuale
enum (’Didattica’, ’Ricerca’, ’Missione’, ’Incontro Dipartimentale’, ’Incontro
Accademico’, ’Altro’)
• CausaAssenza
enum (’Chiusura Universitaria’, ’Maternita’, ’Malattia’)
• PosInteger
integer ≥ 0
• StringaM
varchar(100)
• NumeroOre
integer tra 0 e 8
• Denaro
real ≥ 0
"""