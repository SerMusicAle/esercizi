--1 cognomi di tutti gli strutturati
SELECT cognome 
FROM Persona;

--2 nome e cognome dei ricercatori
SELECT nome, cognome 
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
WHERE posizione = 'Professore Associato' ù
OR posizione ='Professore Ordinario' 
AND cognome LIKE 'V%';

--5 progetti terminati prima di data odierna
SELECT * 
FROM progetto 
WHERE fine < CURRENT_DATE;

--6 progetti ordinati in ordine temporale
SELECT nome
FROM Progetto
ORDER BY inizio ASC;

--7 WP in ordine di nome crescente
SELECT nome
FROM WP
ORDER BY nome ASC;

--8 cause distinte degli strutturati
SELECT DISTINCT tipo
FROM Assenza A
JOIN Persona P ON A.persona = P.id
WHERE P.posizione IN ('Ricercatore', 'Professore Associato', 'Professore Ordinario');

--9 tipologie distinte di attività progetto di tutti 
SELECT DISTINCT tipo
FROM AttivitaProgetto AP
JOIN Persona P ON AP.persona = P.id
WHERE P.posizione IN ('Ricercatore', 'Professore Associato', 'Professore Ordinario');

--10 giorni di attività non didattica in ordine crescente
SELECT DISTINCT giorno
FROM AttivitaNonProgettuale
WHERE tipo = 'Didattica'
ORDER BY giorno ASC;



