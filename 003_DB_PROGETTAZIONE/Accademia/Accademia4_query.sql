--1 cognomi distinti di tutti gli strutturati
SELECT DISTINCT cognome 
FROM Persona;
--where true è opzionale 
WHERE TRUE

--2 nome e cognome dei ricercatori
SELECT id, nome, cognome 
FROM Persona 
WHERE posizione = 'Ricercatore';

--3 professori associati il cui cognome comincia con la V
SELECT nome, cognome 
FROM Persona 
WHERE posizione = 'Professore Associato' 
    AND cognome LIKE 'V%';

--4 tutti i prof con la V
SELECT nome, cognome 
FROM Persona 
WHERE 
(
    posizione = 'Professore Associato'
    OR 
    posizione ='Professore Ordinario' 
    --oppure
    --  posizione IN ('Professore Associato', 'Professore Ordinario')
)
    AND cognome LIKE 'V%';

--5 progetti terminati prima di data odierna
SELECT * 
FROM progetto 
WHERE fine < CURRENT_DATE;
    --oppure
    -- WHERE fine < NOW

--6 progetti ordinati in ordine temporale
SELECT nome
FROM Progetto
--where true è opzionale 
WHERE TRUE
ORDER BY inizio ASC;

--7 WP in ordine di nome crescente
SELECT nome
FROM WP
WHERE TRUE
ORDER BY nome ASC;

--8 cause distinte degli strutturati
SELECT DISTINCT tipo
FROM Assenza A
JOIN Persona P ON A.persona = P.id
WHERE P.posizione IN ('Ricercatore', 'Professore Associato', 'Professore Ordinario');
--SELECT DISTINCT tipo
--FROM Assenza
--WHERE TRUE;

--9 tipologie distinte di attività progetto di tutti 
SELECT DISTINCT tipo
FROM AttivitaProgetto AP
JOIN Persona P ON AP.persona = P.id
WHERE P.posizione IN ('Ricercatore', 'Professore Associato', 'Professore Ordinario');
--SELECT DISTINCT tipo
--FROM AttivitaProgetto
--WHERE TRUE;

--10 giorni di attività non didattica in ordine crescente
SELECT DISTINCT giorno
FROM AttivitaNonProgettuale
WHERE tipo = 'Didattica'
ORDER BY giorno ASC;
--SELECT DISTINCT giorno
--FROM AttivitaNonProgettuale
--WHERE tipo = 'Didattica'
--ORDER BY giorno ASC


