--voli sopra le 3 ore
SELECT codice
FROM Volo
WHERE durataMinuti > 180

--compagnie che hanno voli che superano le 3 ore?
SELECT DISTINCT comp
FROM Volo
WHERE durataMinuti > 180


3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con
codice ‘CIA’ ?
4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice
‘FCO’ ?
5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’
e arrivano all’aeroporto ‘JFK’ ?
6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atter-
rano all’aeroporto ‘JFK’ ?
7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla
città di ‘New York’ ?
8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli
della compagnia di nome ‘MagicFly’ ?
9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e
atterrano ad un qualunque aeroporto della città di ‘New York’ ? Restituire: codice
del volo, nome della compagnia, e aeroporti di partenza e arrivo.
10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo
voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un
qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia,
codici dei voli, e aeroporti di partenza, scalo e arrivo.
11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atter-
rano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?


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