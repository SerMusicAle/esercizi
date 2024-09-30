--1. voli(codice, nome) sopra le 3 ore
SELECT codice
FROM Volo
WHERE durataMinuti > 180;

--2. compagnie che hanno voli che superano le 3 ore?
SELECT DISTINCT comp
FROM Volo
WHERE durataMinuti > 180;

--3.  voli (codice e nome della compagnia) che partono da ‘CIA’
SELECT codice, comp
FROM ArrPart
WHERE partenza = 'CIA';

--4.  compagnie con voli che arrivano da ‘FCO’
SELECT DISTINCT comp
FROM ArrPart
WHERE arrivo = 'FCO';

--5.  voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’ e arrivano all’aeroporto ‘JFK’ ?
SELECT codice, comp
FROM ArrPart
WHERE partenza = 'FCO'
    AND arrivo = 'JFK';

--6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atterrano all’aeroporto ‘JFK’ ?
SELECT DISTINCT comp
FROM ArrPart
WHERE partenza = 'FCO'
    AND arrivo = 'JFK';

--7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla città di ‘New York’ ?
SELECT DISTINCT ap.codice, ap.comp, ap, partenza, part.nome, lpart.citta
FROM ArrPart ap, aereoporto part, LuogoAeroporto lpart
WHERE ap.partenza = part.codice
AND ap.arrivo = larr.aereoporto
AND part.codice = lpart.aereoporto;


--8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli
    -- della compagnia di nome ‘MagicFly’ ?

SELECT DISTINCT nome, a.codice, citta, nazione
FROM ArrPart, LuogoAeroporto, aereoporto A
WHERE partenza = aereoporto
AND comp = 'MagicFly' and a.codice = arrpart.partenza;

--8. Prof. Mancini
SELECT 
    a.codice as codice IATA,
    , a.nome as nome
    la.citta as cittala.naziopne as nazione
FROM ArrPart ap, Aeroporto a, LuogoAeroporto larr
WHERE ap.partenza = a.codice
    AND ap.partenza = la.aeroporto
    AND ap.comp = 'MagicFly'


--9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ 
    -- e atterrano ad un qualunque aeroporto della città di ‘New York’ ? 
    -- Restituire: codice del volo, nome della compagnia, e aeroporti di partenza e arrivo.
SELECT DISTINCT ap.codice, ap.comp, ap.partenza, ap.arrivo
FROM ArrPart ap, Luogoaereoporto rpart, LuogoAeroporto lpart
WHERE ap.partenza = larr.aereoporto
AND ap.arrivo = larr.aereoporto
AND lpart, citta = 'Roma'
AND larr, citta = 'New York';

--9. Prof. Mancini
SELECT a.codice as codice
    ap.comp as compagnia
    aeroop_p.codice as partenza_codice
    aerop_p.nome as partenza_nome
    aerop_arr.codice as arrivo_codice
    aerop_arr.nome as arrivo_nome
FROM ArrPart ap
    LuogoAeroporto lap,
    LuoboAeroporto laa,
    Aeroporto aerop_p,
    Aeroporto aerop:arr
WHERE ap.partenza = lap.aeroporto
    AND lap.citta = citta
    --da finire guardando il video

--10. Quali sono i possibili piani di volo con esattamente un cambio 
    -- (utilizzando solo voli della stessa compagnia) da un qualunque aeroporto
    -- della città di ‘Roma’ ad un qualunque aeroporto della città di ‘New York’ ? 
    -- Restituire: nome della compagnia, codici dei voli, e aeroporti di partenza, 
    -- scalo e arrivo.
SELECT  v1.comp as compagnia
        v1.codice as volo1
        v2.codice as volo2
        v1.partenza as partenza
        v1.arrivo as scalo
        v1.arrivo as arrivo

FROM arrpart v1, arrpart v2, Luogoaereoporto lpart, Luogoaereoporto larr
WHERE v1.arrivo = v2.partenza
    AND v1.comp = v2.comp
    AND v1.partenza = lpart.aereoporto 
    AND v1.partenza = larr.aereoporto 
    AND lpart.citta = 'Roma' 
    AND larr.citta = 'New York' 


--11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, 
    -- atterrano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?
SELECT DISTINCT comp 
FROM arrpart up, compagnia c 
WHERE comp = c.nome
AND ap.partenza = 'FCO' 
AND ap.arrivo ='JFK' 
AND annodondaz is NOT NULL;

























SELECT Volo.codice, ArrPart.arrivo, ArrPart.partenza, AeroportoArrivo.nome AS nome_arrivo, AeroportoPartenza.nome AS nome_partenza
FROM ArrPart
JOIN Volo ON ArrPart.codice = Volo.codice AND ArrPart.comp = Volo.comp
JOIN Aeroporto AS AeroportoArrivo ON ArrPart.arrivo = AeroportoArrivo.codice
JOIN Aeroporto AS AeroportoPartenza ON ArrPart.partenza = AeroportoPartenza.codice
WHERE Volo.codice = 123;  -- Sostituisci 123 con il codice del volo specifico


SELECT Aeroporto.codice, Aeroporto.nome
FROM Aeroporto
JOIN LuogoAeroporto ON Aeroporto.codice = LuogoAeroporto.aeroporto
WHERE LuogoAeroporto.citta = 'Roma' AND LuogoAeroporto.nazione = 'Italia';

SELECT Volo.codice, Volo.durataMinuti
FROM Volo
WHERE Volo.comp = 'Alitalia' AND Volo.durataMinuti > 120;

SELECT Volo.codice, Volo.comp, ArrPart.arrivo
FROM ArrPart
JOIN Volo ON ArrPart.codice = Volo.codice AND ArrPart.comp = Volo.comp
WHERE ArrPart.partenza = 'FCO';  -- Sostituisci 'FCO' con il CodIATA dell'aeroporto di partenza


--, Compagnia.annoFondaz