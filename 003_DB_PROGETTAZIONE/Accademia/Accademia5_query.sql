-----------------------ACCADEMIA 5 QUERY -----------------------


--1. Quali sono il nome, la data di inizio e la data di fine 
    -- dei WP del progetto di nome ‘Pegasus’?
SELECT nome, inizio, fine
FROM WP
WHERE nome = Pegasus;

--2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno 
    --almeno una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?
SELECT PA.nome, PA.cognome, PA.posizione
FROM persona PA
JOIN attivitaProgetto AP ON PA.id = AP.persona
JOIN progetto PR ON AP.progetto = PR.id
WHERE PR.nome = 'Pegasus'
ORDER BY PA.cognome DESC;

--3. Quali sono il nome, il cognome e la posizione degli strutturati 
    --che hanno più di una attività nel progetto ‘Pegasus’?
SELECT P.nome, P.cognome, P.posizione
FROM persona P
JOIN attivitaProgetto AP ON P.id = AP.persona
JOIN progetto PR ON AP.progetto = PR.id
WHERE PR.nome = 'Pegasus'
GROUP BY P.nome, P.cognome, P.posizione
HAVING COUNT(AP.id) > 1;

--4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari 
    --che hanno fatto almeno una assenza per malattia?
SELECT P.nome, P.cognome, P.posizione
FROM persona P
JOIN assenza A ON P.id = A.persona
WHERE P.posizione = 'Professore Ordinario' 
    AND A.tipo = 'Malattia';

--5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari 
    --che hanno fatto più di una assenza per malattia?
SELECT P.nome, P.cognome, P.posizione
FROM persona P
JOIN assenza A ON P.id = A.persona
WHERE P.posizione = 'Professore Ordinario'
    AND A.tipo = 'Malattia'
GROUP BY P.nome, P.cognome, P.posizione
HAVING COUNT(A.id) > 1;

--6. Quali sono il nome, il cognome e la posizione dei Ricercatori 
    --che hanno almeno un impegno per didattica?
SELECT P.nome, P.cognome, P.posizione
FROM persona P
JOIN attivitaNonProgettuale ANP ON P.id = ANP.persona
WHERE P.posizione = 'Ricercatore'
    AND ANP.tipo = 'Didattica';

--7. Quali sono il nome, il cognome e la posizione dei Ricercatori 
    --che hanno più di un impegno per didattica?
SELECT P.nome, P.cognome, P.posizione
FROM persona P
JOIN attivitaNonProgettuale ANP ON P.id = ANP.persona
WHERE P.posizione = 'Ricercatore'
    AND ANP.tipo = 'Didattica'
GROUP BY P.nome, P.cognome, P.posizione
HAVING COUNT(ANP.id) > 1;

--8. Quali sono il nome e il cognome degli strutturati 
    --che nello stesso giorno hanno sia attività progettuali che attività non progettuali?
SELECT P.nome, P.cognome
FROM persona P
JOIN attivitaProgetto AP ON P.id = AP.persona
JOIN attivitaNonProgettuale ANP ON P.id = ANP.persona
WHERE AP.giorno = ANP.giorno;

--9. Quali sono il nome e il cognome degli strutturati 
    --che nello stesso giorno hanno sia attività progettuali che attività non progettuali? 
    --Si richiede anche di proiettare il giorno, il nome del progetto, 
    --il tipo di attività non progettuali e la durata in ore di entrambe le attività.
SELECT P.nome, P.cognome, AP.giorno, PR.nome AS nome_progetto, 
       ANP.tipo AS tipo_attivita_non_progettuale, AP.oreDurata AS ore_attivita_progetto, 
       ANP.oreDurata AS ore_attivita_non_progetto
FROM persona P
JOIN attivitaProgetto AP ON P.id = AP.persona
JOIN progetto PR ON AP.progetto = PR.id
JOIN attivitaNonProgettuale ANP ON P.id = ANP.persona
WHERE AP.giorno = ANP.giorno;
 
--10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno 
    --sono assenti e hanno attività progettuali?
SELECT P.nome, P.cognome
FROM persona P
JOIN attivitaProgetto AP ON P.id = AP.persona
JOIN assenza A ON P.id = A.persona
WHERE AP.giorno = A.giorno;

--11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno 
    --sono assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, 
    --il nome del progetto, la causa di assenza e la durata in ore della attività progettuale.
SELECT P.nome, P.cognome, A.giorno, PR.nome AS nome_progetto, A.tipo AS causa_assenza, 
       AP.oreDurata AS ore_attivita_progetto
FROM persona P
JOIN attivitaProgetto AP ON P.id = AP.persona
JOIN progetto PR ON AP.progetto = PR.id
JOIN assenza A ON P.id = A.persona
WHERE AP.giorno = A.giorno;

--12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?
SELECT WP.nome, COUNT(DISTINCT WP.progetto) AS progetti_diversi
FROM wp WP
GROUP BY WP.nome
HAVING COUNT(DISTINCT WP.progetto) > 1;

