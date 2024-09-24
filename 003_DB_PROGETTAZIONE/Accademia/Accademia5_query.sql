-----------------------ACCADEMIA 5 QUERY -----------------------


--1. Quali sono il nome, la data di inizio e la data di fine 
    -- dei WP del progetto di nome ‘Pegasus’?
SELECT wp.nome, wp.inizio, wp.fine
FROM WP
JOIN progetto P
    ON wp.progetto = p.id
WHERE p.nome = 'Pegasus';

--2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno 
    --almeno una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?
SELECT PA.nome, PA.cognome, PA.posizione
FROM persona PA
JOIN attivitaProgetto AP 
    ON PA.id = AP.persona
JOIN progetto PR 
    ON AP.progetto = PR.id
WHERE PR.nome = 'Pegasus'
ORDER BY PA.cognome DESC;

--3. Quali sono il nome, il cognome e la posizione degli strutturati 
    --che hanno più di una attività nel progetto ‘Pegasus’?
SELECT P.nome, P.cognome, P.posizione
FROM persona P
JOIN attivitaProgetto AP 
    ON P.id = AP.persona
JOIN progetto PR 
    ON AP.progetto = PR.id
WHERE PR.nome = 'Pegasus'
GROUP BY P.nome, P.cognome, P.posizione
HAVING COUNT(AP.id) > 1;
--VERSIONE 2
--SELECT DISTINCT s.nome, s.conome, s.posizione
--FROM progetto P
--  JOIN attivitaprogetto A1
--      ON P.id = AL.progetto
--  JOIN attivitaprogetto A2
--      ON P.id = A2.progetto
--  JOIN persona S
--      ON S.id = A1.persona
--      AND A1.persona = A2.persona
--WHERE
--  AND A1.id <>A2.id
--  AND P.nome = 'Pegasus';

--4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari 
    --che hanno fatto almeno una assenza per malattia?
SELECT DISTINCT P.nome, P.cognome, P.posizione
FROM persona P
JOIN assenza A 
    ON P.id = A.persona
WHERE P.posizione = 'Professore Ordinario' 
    AND A.tipo = 'Malattia';

--5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari 
    --che hanno fatto più di una assenza per malattia?
SELECT DISTINCT P.nome, P.cognome, P.posizione
FROM persona P
JOIN assenza A 
    ON P.id = A.persona
WHERE P.posizione = 'Professore Ordinario'
    AND A.tipo = 'Malattia'
GROUP BY P.nome, P.cognome, P.posizione
HAVING COUNT(A.id) > 1;
--VERSIONE 2
--SELECT DISTINCT nome, cognome, posizione
--FROM assenza A1, assenza A2, persona S
--WHERE A1.id <> A2.id
--  AND A1.persona = A2.persona
--  AND A1.persona = S.id
--  AND S.posizione = 'Professore Ordinario'

--6. Quali sono il nome, il cognome e la posizione dei Ricercatori 
    --che hanno almeno un impegno per didattica?
SELECT DISTINCT P.nome, P.cognome, P.posizione
FROM persona P
JOIN attivitaNonProgettuale ANP 
    ON P.id = ANP.persona
WHERE P.posizione = 'Ricercatore'
    AND ANP.tipo = 'Didattica';

--7. Quali sono il nome, il cognome e la posizione dei Ricercatori 
    --che hanno più di un impegno per didattica?
SELECT P.nome, P.cognome, P.posizione
FROM persona P
JOIN attivitaNonProgettuale ANP 
    ON P.id = ANP.persona
WHERE P.posizione = 'Ricercatore'
    AND ANP.tipo = 'Didattica'
GROUP BY P.nome, P.cognome, P.posizione
HAVING COUNT(ANP.id) > 1;
--VERSIONE 2
--FROM persona PA,
--  attivitanonprogettuale ANP
--  attivitanonprogettuale ANP1
--  persona P1
--WHERE PA.id = ANP.persona 
--  AND ANP.tipo = 'Didattica'
--  AND ANP1.tipo = 'Didattica'
--  AND PP.posizione = 'Ricercatore'
--  AND ANP.id <>ANP1.id
--  AND ANP.persona = ANP1.persona


--8. Quali sono il nome e il cognome degli strutturati 
    --che nello stesso giorno hanno sia attività progettuali che attività non progettuali?
SELECT DISTINCT P.nome, P.cognome
FROM persona P
JOIN attivitaProgetto AP 
    ON P.id = AP.persona
JOIN attivitaNonProgettuale ANP 
    ON P.id = ANP.persona
WHERE AP.giorno = ANP.giorno;

--9. Quali sono il nome e il cognome degli strutturati 
    --che nello stesso giorno hanno sia attività progettuali che attività non progettuali? 
    --Si richiede anche di proiettare il giorno, il nome del progetto, 
    --il tipo di attività non progettuali e la durata in ore di entrambe le attività.
SELECT DISTINCT P.nome, P.cognome, AP.giorno, PR.nome AS nome_progetto, 
       ANP.tipo AS tipo_attivita_non_progettuale, AP.oreDurata AS ore_attivita_progetto, 
       ANP.oreDurata AS ore_attivita_non_progetto
FROM persona P
JOIN attivitaProgetto AP 
    ON P.id = AP.persona
JOIN progetto PR 
    ON AP.progetto = PR.id
JOIN attivitaNonProgettuale ANP 
    ON P.id = ANP.persona
WHERE AP.giorno = ANP.giorno;
--VERSIONE 2
--SELECT  DISTINCT
--  S.nome, S.cognome, AP.giorno
--  P.nome AS progetto
--  ANP.tipo AS TipoAttNonProgettuale,
--  AP.durata AS durataAttProg
--  ANO.durata AS durataAttNonProg
--FROM attivitaprogetto AP  
--  JOIN attivitaNonProgettuale ANP
--      ON AP.persona = ANP.persona
--  JOIN persona S
--      ON S.id = AP.persona
--  JOIN progetto P
--      ON AP.progetto = P.id
--  WHERE AP.giorno = ANP.giorno;
      
--10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno 
    --sono assenti e hanno attività progettuali?
SELECT DISTINCT P.nome, P.cognome
FROM persona P
    JOIN attivitaProgetto AP 
        ON P.id = AP.persona
    JOIN assenza A 
        ON P.id = A.persona
WHERE AP.giorno = A.giorno;
--VERSIONE 2
--SELECT DISTINCT PE.nome, PE.cognome
--FROM attivitaProgetto AS A1
--  persona AS PE
--  assenza AS A2
--WHERE
--  PE.id = A2.persona
--  AND PE.id = A1.persona
--  AND A1.giorno = A2.giorno;

--11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno 
    --sono assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, 
    --il nome del progetto, la causa di assenza e la durata in ore della attività progettuale.
SELECT DISTINCT P.nome, P.cognome, A.giorno, PR.nome AS nome_progetto, A.tipo AS causa_assenza, 
       AP.oreDurata AS ore_attivita_progetto
FROM persona P
    JOIN attivitaProgetto AP 
        ON P.id = AP.persona
    JOIN progetto PR 
        ON AP.progetto = PR.id
    JOIN assenza A 
        ON P.id = A.persona
WHERE AP.giorno = A.giorno;

--12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?
SELECT WP.nome, COUNT(DISTINCT WP.progetto) AS progetti_diversi
FROM wp WP
GROUP BY WP.nome
HAVING COUNT(DISTINCT WP.progetto) > 1;
--VERSIONE2
--SELECT DISTINCT WP.nome
--FROM wp WP1, wp WP2
--WHERE WP1.nome = WP2.nome
--  AND WP1.progetto <> WP2.progetto;
--

