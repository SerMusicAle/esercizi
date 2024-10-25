-- 1. Quali sono le persone (id, nome e cognome) 
    -- assenze solo nei giorni senza attivitÃ (progettuali o non progettuali)?
    -- giorno assenza = 
SELECT p.id,
       p.nome,
       p.cognome
FROM persona p

    LEFT OUTER JOIN assenza a ON p.id = a.persona
    LEFT OUTER JOIN attivitaProgetto ap ON p.id = ap.persona AND a.giorno != ap.giorno
    LEFT OUTER JOIN attivitaNonProgettuale anp ON p.id = anp.persona AND a.giorno != anp.giorno

GROUP BY p.id, p.nome, p.cognome
HAVING COUNT(a.id) > 0 AND COUNT(ap.id) = 0 AND COUNT(anp.id) = 0;

-- 2. Quali sono le persone (id, nome e cognome) che non hanno mai partecipato ad
    --alcun progetto durante la durata del progetto “Pegasus”?


-- 3. Quali sono id, nome, cognome e stipendio dei ricercatori con stipendio maggiore
    --di tutti i professori (associati e ordinari)?

--4. Quali sono le persone che hanno lavorato su progetti con un budget superiore alla
    --media dei budget di tutti i progetti?

--5. Quali sono i progetti con un budget inferiore allala media, ma con un numero
    --complessivo di ore dedicate alle attività di ricerca sopra la media?

id dataassenza

persone che non hanno fatto assenze
persone che hanno fatto assenze quando non c'erano attività