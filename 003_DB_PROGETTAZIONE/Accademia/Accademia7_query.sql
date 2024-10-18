-- 1. Qual è la media e deviazione standard degli stipendi per ogni categoria di strutturati?
SELECT posizione, 
       AVG(stipendio) AS Media_Stipendio, 
       STDDEV(stipendio) AS Deviazione_Standard
FROM Persona
GROUP BY posizione;


-- 2. Quali sono i ricercatori (tutti gli attributi) con uno stipendio superiore alla media
    --della loro categoria?
SELECT 
    *
FROM 
    Persona p
WHERE 
    p.stipendio > (SELECT AVG(stipendio) 
                   FROM Persona 
                   WHERE posizione = p.posizione)
    AND p.posizione = 'Ricercatore';

--VERSIONE AVANZATA

-- SELECT 
--     p.*
-- FROM 
--     Persona p
-- JOIN 
--     (SELECT 
--         posizione, 
--         AVG(stipendio) AS media_stipendio
--     FROM 
--         Persona
--     GROUP BY 
--         posizione) AS avg_table
-- ON 
--     p.posizione = avg_table.posizione
-- WHERE 
--     p.stipendio > avg_table.media_stipendio
--     AND p.posizione = 'Ricercatore';


-- 3. Per ogni categoria di strutturati quante sono le persone con uno stipendio che
    --differisce di al massimo una deviazione standard dalla media della loro categoria?
WITH Stats {
    
}

SELECT posizione,
       stipendio,
       STDDEV(stipendio) AS Deviazione_Standard
       AVG(stipendio) AS Media_Stipendio, 
       COUNT (*) As Num_Ric
       
FROM persona p

GROUP BY posizione

HAVING (AVG(stipendio) OVER (PARTITION BY posizione) - STDDEV(stipendio) OVER (PARTITION BY posizione))
       AND 
       (AVG(stipendio) OVER (PARTITION BY posizione) + STDDEV(stipendio) OVER (PARTITION BY posizione))

-- 4. Chi sono gli strutturati che hanno lavorato almeno 20 ore complessive in attività
    --progettuali? Restituire tutti i loro dati e il numero di ore lavorate.
SELECT *
       SUM(ap.oreDurata) AS TotaleOre

FROM Persona p

JOIN AttivitàProgetto ap ON p.id = ap.persona

GROUP BY p.id, p.nome, p.cognome, p.posizione, p.stipendio

HAVING SUM(ap.oreDurata) >= 20

-- 5. Quali sono i progetti la cui durata è superiore alla media delle durate di tutti i
    --progetti? Restituire nome dei progetti e loro durata in giorni.


-- 6. Quali sono i progetti terminati in data odierna che hanno avuto attività di tipo
    --“Dimostrazione”? Restituire nome di ogni progetto e il numero complessivo delle
    --ore dedicate a tali attività nel progetto.


-- 7. Quali sono i professori ordinari che hanno fatto più assenze per malattia del numero di assenze medio per malattia dei professori associati? Restituire id, nome e
    --cognome del professore e il numero di giorni di assenza per malattia.
