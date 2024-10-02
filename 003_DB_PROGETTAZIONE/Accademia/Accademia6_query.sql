-- 1. Quanti sono gli strutturati di ogni fascia?
SELECT posizione, COUNT(*) AS numero_strutturati
FROM accademia.persona
GROUP BY posizione;

-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?
SELECT COUNT(*) AS numero_strutturati
FROM accademia.persona
WHERE stipendio >= 40000;

-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?
SELECT COUNT(*) AS progetti_finiti
FROM accademia.progetto
WHERE fine IS NOT NULL AND budget > 50000;

-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto ‘Pegasus’?
SELECT 
    AVG(oreDurata) AS media_ore,
    MAX(oreDurata) AS max_ore,
    MIN(oreDurata) AS min_ore
FROM accademia.attivitaProgetto AP
JOIN accademia.progetto P ON AP.progetto = P.id
WHERE P.nome = 'Pegasus';

-- 5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto ‘Pegasus’ da ogni singolo docente?
SELECT 
    persona,
    AVG(oreDurata) AS media_ore,
    MAX(oreDurata) AS max_ore,
    MIN(oreDurata) AS min_ore
FROM accademia.attivitaProgetto AP
JOIN accademia.progetto P ON AP.progetto = P.id
WHERE P.nome = 'Pegasus'
GROUP BY persona;

-- 6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?
SELECT 
    persona, 
    SUM(oreDurata) AS totale_ore_didattica
FROM accademia.attivitaProgetto
WHERE tipo = 'Didattica'
GROUP BY persona;

-- 7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?
SELECT 
    AVG(stipendio) AS media_stipendio,
    MAX(stipendio) AS max_stipendio,
    MIN(stipendio) AS min_stipendio
FROM accademia.persona
WHERE posizione = 'Ricercatore';

-- 8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori associati e dei professori ordinari?
SELECT 
    posizione,
    AVG(stipendio) AS media_stipendio,
    MAX(stipendio) AS max_stipendio,
    MIN(stipendio) AS min_stipendio
FROM accademia.persona
GROUP BY posizione;

-- 9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?
SELECT 
    progetto,
    SUM(oreDurata) AS totale_ore
FROM accademia.attivitaProgetto
WHERE persona = (SELECT id FROM accademia.persona WHERE nome = 'Ginevra' AND cognome = 'Riva')
GROUP BY progetto;

-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?
SELECT 
    P.nome
FROM accademia.wp W
JOIN accademia.progetto P ON W.progetto = P.id
GROUP BY P.nome
HAVING COUNT(DISTINCT W.id) > 2;

-- 11. Quali sono i professori associati che hanno lavorato su più di un progetto?
SELECT 
    persona
FROM accademia.attivitaProgetto AP
JOIN accademia.persona P ON AP.persona = P.id
WHERE P.posizione = 'Professore Associato'
GROUP BY AP.persona
HAVING COUNT(DISTINCT AP.progetto) > 1;
