--1
SELECT cognome 
FROM Persona;
--2
SELECT nome, cognome 
FROM Persona 
WHERE posizione = 'Ricercatore';
--3
SELECT nome, cognome 
FROM Persona 
WHERE posizione = 'Professore Associato' 
AND cognome LIKE 'V%';
--4
SELECT nome, cognome 
FROM Persona 
WHERE posizione = 'Professore Associato' ù
OR posizione ='Professore Ordinario' 
AND cognome LIKE 'V%';
--5
SELECT * 
FROM progetto 
WHERE fine < CURRENT_DATE;
--6



