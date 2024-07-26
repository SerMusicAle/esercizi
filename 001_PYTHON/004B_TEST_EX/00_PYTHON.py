"""PYTHON - ALGORITMI
Boln,ln MQon2 F(r)o2n F(i)On BSon2 MSnln MS<tBS

  Quale metodo di lettura legge una singola linea alla volta fino a incontrare il token EOF?
Risposta corretta: readline()
Spiegazione/Esempio: Il metodo readline() legge una sola linea di testo da un file fino a trovare il carattere di fine file (EOF). Ad esempio, se hai un file file.txt con più righe e usi file.readline(), verrà letta e restituita solo la prima riga del file.
Risposte errate:
readlines(): Legge tutte le righe del file e le restituisce come una lista.
read(): Legge tutto il contenuto del file come una stringa unica.
readall(): Non è un metodo standard in Python per la lettura dei file.
  Quale metodo della classe Process consente di attendere la terminazione di un processo figlio?
Risposta corretta: wait()
Spiegazione/Esempio: Il metodo wait() della classe Process del modulo multiprocessing blocca l'esecuzione fino a quando il processo figlio non termina. Ad esempio, se hai un processo in esecuzione e chiami p.wait(), il tuo programma aspetterà che il processo p termini prima di continuare.
Risposte errate:
join(): Utilizzato per thread e non per processi.
pause(): Non esiste un metodo pause() nella classe Process.
terminate(): Termina immediatamente il processo senza attendere.
  Che cosa si intende per overhead in un contesto di multiprocessing?
Risposta corretta: Il costo aggiuntivo in termini di risorse computazionali per gestire i processi
Spiegazione/Esempio: L'overhead nel contesto del multiprocessing rappresenta il costo aggiuntivo associato alla gestione di più processi, come il consumo di memoria e il tempo necessario per la sincronizzazione e la comunicazione tra i processi.
Risposte errate:
La quantità di memoria utilizzata da un processo: Non è specifico dell'overhead, ma piuttosto una caratteristica di un processo.
Il numero di processi che possono essere eseguiti contemporaneamente: Non è un costo ma una capacità.
Il tempo di esecuzione di un processo: Non è specificamente il costo di gestione dei processi.
  Cosa rappresenta un file in un sistema operativo moderno?
Risposta corretta: Un insieme contiguo di byte utilizzati per memorizzare dati
Spiegazione/Esempio: In un sistema operativo, un file è considerato come una sequenza di byte memorizzati su un disco o un altro supporto di memorizzazione. I file possono contenere dati di vario tipo, come testo, immagini, o eseguibili.
Risposte errate:
Un programma eseguibile: Solo alcuni file sono eseguibili, non tutti i file.
Una sequenza di comandi per il sistema operativo: Questo è più adatto ai comandi di shell o script.
Una parte della memoria RAM: I file sono memorizzati su supporti di memorizzazione persistenti, non nella RAM.
  Quale problema risolvono i container rispetto alle VM in termini di portabilità?
Risposta corretta: I container sono progettati per essere indipendenti dalla piattaforma
Spiegazione/Esempio: I container, come quelli creati con Docker, sono progettati per essere portabili e indipendenti dalla piattaforma sottostante. Questo significa che un'applicazione containerizzata può essere eseguita su qualsiasi sistema che supporta il runtime del container senza problemi di compatibilità.
Risposte errate:
Le VM sono più leggere dei container: I container sono generalmente più leggeri delle VM.
I container sono più difficili da spostare: I container sono progettati per essere facili da spostare e distribuire.
Le VM hanno un overhead inferiore: I container hanno un overhead inferiore rispetto alle VM.
  Quale metodo viene utilizzato per proteggere le variabili condivise in un ambiente multi-thread?
Risposta corretta: Aggiungere lock
Spiegazione/Esempio: I lock sono utilizzati per garantire che solo un thread alla volta possa accedere a una sezione critica del codice, proteggendo così le variabili condivise da accessi simultanei che potrebbero causare inconsistenze. Ad esempio, il modulo threading in Python fornisce il costrutto Lock per questo scopo.
Risposte errate:
Incrementare i thread: Non protegge le variabili condivise.
Utilizzare variabili globali: Le variabili globali non proteggono di per sé i dati condivisi.
Ridurre l'uso della memoria: Non è correlato alla protezione delle variabili condivise.
  Quale eccezione viene sollevata quando un'operazione aritmetica non valida viene eseguita?
Risposta corretta: ArithmeticError
Spiegazione/Esempio: ArithmeticError è una classe base per eccezioni che si verificano in operazioni aritmetiche, come ZeroDivisionError e OverflowError. Ad esempio, la divisione per zero in Python solleva un ZeroDivisionError, che è un sotto-tipo di ArithmeticError.
Risposte errate:
CalculationError: Non esiste in Python.
ValueError: Viene sollevata quando una funzione riceve un argomento con un valore inappropriato, non necessariamente aritmetico.
MathError: Non esiste in Python.
  Qual è il vantaggio principale dell'uso del multiprocessing rispetto al threading per compiti CPU-bound?
Risposta corretta: Il multiprocessing può sfruttare più core del processore
Spiegazione/Esempio: Il multiprocessing utilizza processi separati che possono essere eseguiti su core diversi della CPU, il che è particolarmente utile per compiti che richiedono molta potenza di calcolo. A differenza del threading, che è limitato dal Global Interpreter Lock (GIL) in Python, il multiprocessing può effettivamente utilizzare più core.
Risposte errate:
Il threading è più efficiente in termini di memoria: Non è corretto per compiti CPU-bound.
Il threading è più facile da implementare: Non è specificamente un vantaggio per compiti CPU-bound.
Il multiprocessing è sempre più veloce: Non è sempre vero, dipende dal contesto.
  Come si avvia un nuovo thread in Python?
Risposta corretta: Creando un'istanza di Thread e chiamando .start()
Spiegazione/Esempio: Per avviare un nuovo thread in Python, si crea un'istanza della classe Thread e si chiama il metodo .start(). Ad esempio, utilizzando threading.Thread(target=worker).start(), si avvia il thread che eseguirà la funzione worker.
Risposte errate:
Chiamando .run() su una funzione: .run() viene chiamato automaticamente da .start().
Importando il modulo sys: Non è relativo alla creazione o gestione di thread.
Utilizzando il modulo os: Non è il modulo giusto per la gestione dei thread.
  Qual è la funzione principale del GIL (Global Interpreter Lock) in Python?
Risposta corretta: Limitare l'esecuzione a un solo thread alla volta
Spiegazione/Esempio: Il GIL è un meccanismo di sincronizzazione in Python che impedisce l'esecuzione simultanea di più thread all'interno dello stesso processo, limitando l'esecuzione a un solo thread alla volta. Questo è stato progettato per semplificare la gestione della memoria condivisa, ma può limitare le prestazioni nei compiti CPU-bound.
Risposte errate:
Gestire la memoria: Non è la funzione principale del GIL.
Ottimizzare le prestazioni: Il GIL può effettivamente ridurre le prestazioni in alcuni casi.
Permettere l'esecuzione simultanea di più thread: Il GIL impedisce l'esecuzione simultanea.
Come si solleva un'eccezione con un messaggio personalizzato?
Risposta corretta: raise Exception('messaggio')
Spiegazione/Esempio: In Python, si utilizza raise seguito dal tipo di eccezione e, facoltativamente, un messaggio personalizzato. Ad esempio, raise Exception('Errore personalizzato') solleva un'eccezione di tipo Exception con il messaggio 'Errore personalizzato'.
Risposte errate:
throw Exception('messaggio'): throw non è usato in Python; è un termine di altri linguaggi come Java.
throw Error('messaggio'): Error non è una classe di eccezione predefinita in Python e throw non è un termine valido in Python.
raise Error('messaggio'): Error non è una classe di eccezione predefinita in Python.
Quale comando esegue i test unittest in modalità verbosa?
Risposta corretta: python -m unittest -v
Spiegazione/Esempio: Il flag -v (verbose) rende l'output di unittest più dettagliato, mostrando informazioni aggiuntive sui test eseguiti. Ad esempio, python -m unittest -v test_module.py mostra dettagli su ogni test.
Risposte errate:
python -m unittest --verbose: Anche se il flag --verbose è corretto, -v è una sintassi più comune.
python -m unittest -verbose: -verbose non è una sintassi valida per unittest.
python -m unittest --v: --v non è una sintassi valida.
Quale funzione deve essere passata a un'istanza di Thread?
Risposta corretta: Una funzione da eseguire nel nuovo thread
Spiegazione/Esempio: Quando si crea un'istanza della classe Thread, è necessario passare la funzione che si desidera eseguire nel nuovo thread tramite il parametro target. Ad esempio:
python
Copia codice
import threading

def worker():
    print("Worker")

t = threading.Thread(target=worker)
t.start()
Risposte errate:
Un oggetto: Non è corretto; deve essere una funzione.
Un modulo: Non è corretto; deve essere una funzione.
Una variabile: Non è corretto; deve essere una funzione.
Cosa specifica l'istruzione "CMD" in un Dockerfile?
Risposta corretta: Il comando da eseguire quando il container viene avviato
Spiegazione/Esempio: L'istruzione CMD in un Dockerfile definisce il comando che verrà eseguito quando il container sarà avviato. Ad esempio, CMD ["python", "app.py"] avvierà il file app.py usando Python quando il container parte.
Risposte errate:
Le dipendenze del container: Non è corretto; le dipendenze vengono gestite con RUN o COPY.
Il sistema operativo del container: Specificato nell'istruzione FROM.
Le variabili d'ambiente del container: Specificate con l'istruzione ENV.
Cos'è Docker?
Risposta corretta: Uno strumento per creare e gestire container
Spiegazione/Esempio: Docker è una piattaforma che consente di sviluppare, spedire e eseguire applicazioni in container, fornendo un ambiente isolato e riproducibile per il software.
Risposte errate:
Un tipo di macchina virtuale: I container sono diversi dalle macchine virtuali; sono più leggeri e condividono il kernel del sistema operativo.
Un sistema operativo: Docker non è un sistema operativo ma un tool di containerizzazione.
Un linguaggio di programmazione: Docker non è un linguaggio di programmazione.
Quale problema comune si verifica quando si dimentica di chiudere un file in Python?
Risposta corretta: Memory leak
Spiegazione/Esempio: Non chiudere un file può causare un leak di memoria poiché le risorse del file rimangono aperte, consumando memoria e potenzialmente esaurendo le risorse del sistema. È una buona pratica chiudere sempre i file, preferibilmente usando il costrutto with.
Risposte errate:
Runtime error: Non specificamente un errore di runtime dovuto alla mancata chiusura di un file.
Type error: Non è correlato alla chiusura di file.
Syntax error: Non è correlato alla chiusura di file.
Cosa verifica il metodo assertIsNone in unittest?
Risposta corretta: Verifica se una variabile è None
Spiegazione/Esempio: Il metodo assertIsNone di unittest verifica se il valore di una variabile è None. Ad esempio:
python
Copia codice
import unittest

class TestExample(unittest.TestCase):
    def test_is_none(self):
        self.assertIsNone(None)
Risposte errate:
Verifica se una variabile è False: assertIsNone non verifica se una variabile è False.
Verifica se una variabile è vuota: assertIsNone non verifica se una variabile è vuota.
Verifica se una variabile è True: assertIsNone non verifica se una variabile è True.
Quale metodo viene utilizzato per assicurarsi che un file venga chiuso correttamente, anche in caso di errore?
Risposta corretta: with statement
Spiegazione/Esempio: L'istruzione with in Python garantisce che il file venga chiuso automaticamente quando il blocco di codice viene completato, anche se si verifica un errore. Ad esempio:
python
Copia codice
with open('file.txt', 'r') as file:
    data = file.read()
Risposte errate:
open statement: Non esiste un'istruzione open che chiuda automaticamente i file.
close statement: Non è un metodo per aprire file.
try-catch statement: Utilizzato per gestire le eccezioni, ma non per chiudere automaticamente i file.
Cosa succede se si passa una funzione con le parentesi come argomento a un'altra funzione?
Risposta corretta: La funzione viene eseguita immediatamente e viene passato il valore ritornato
Spiegazione/Esempio: Se passi una funzione con le parentesi (es. func()), la funzione viene eseguita subito e l'argomento passato sarà il valore restituito dalla funzione. Ad esempio, se func() ritorna 5, allora passerai 5 come argomento.
Risposte errate:
La funzione viene ignorata: La funzione non viene ignorata, viene eseguita.
La funzione viene convertita in una stringa: Non è corretto.
La funzione viene passata come referenza: Le parentesi eseguono la funzione e passano il risultato, non la funzione stessa.
Come si può creare un'eccezione personalizzata in Python?
Risposta corretta: Ereditando da Exception
Spiegazione/Esempio: Per creare un'eccezione personalizzata in Python, si deve creare una nuova classe che eredita dalla classe Exception. Ad esempio:
python
Copia codice
class MyCustomError(Exception):
    pass
Risposte errate:
Ereditando da CustomError: CustomError non è una classe predefinita in Python.
Ereditando da BaseException: Exception è una sottoclasse di BaseException e più specifica.
Ereditando da RaiseException: RaiseException non esiste in Python.
Cosa succede se non si utilizza il metodo join in un programma con multiprocessing?
Risposta corretta: Il programma principale può terminare prima che i processi figli abbiano finito
Spiegazione/Esempio: Il metodo join() viene utilizzato per far sì che il programma principale aspetti la terminazione dei processi figli. Senza join(), il programma principale potrebbe terminare mentre i processi figli sono ancora in esecuzione, potenzialmente interrompendo il lavoro in corso.
Risposte errate:
I processi figli non iniziano mai: Non è corretto; i processi figli iniziano comunque.
I processi figli terminano immediatamente: Non è corretto; i processi figli continuano fino alla loro conclusione.
Il programma principale e i processi figli terminano contemporaneamente: Non è garantito senza join().
Cosa succede se si lancia un'asserzione con una condizione falsa senza fornire un messaggio?
Risposta corretta: Viene sollevata un'AssertionError senza messaggio
Spiegazione/Esempio: Quando si usa assert con una condizione falsa e senza fornire un messaggio, viene sollevata un'eccezione AssertionError senza messaggio specifico. Ad esempio, assert 1 < 0 solleverà un'eccezione senza messaggio.
Risposte errate:
Non succede nulla: Un'asserzione falsa solleverà sempre un'eccezione.
Viene sollevata un'AssertionError con messaggio predefinito: Non viene fornito un messaggio specifico se non è stato indicato.
Il programma si chiude senza errore: L'asserzione solleverà un errore.
Quale metodo Python utilizza per la gestione della memoria?
Risposta corretta: Garbage collection
Spiegazione/Esempio: Python utilizza la garbage collection per gestire la memoria. Questo meccanismo libera automaticamente la memoria che non è più in uso, aiutando a prevenire i memory leak.
Risposte errate:
Reference counting: Anche se il conteggio dei riferimenti è usato, la garbage collection è il metodo principale.
Manual memory management: Python gestisce automaticamente la memoria, senza richiedere la gestione manuale da parte degli utenti.
Memory pooling: Non è un metodo standard per la gestione della memoria in Python.
Qual è il risultato dell'istruzione assert 1 < 0?
Risposta corretta: AssertionError
Spiegazione/Esempio: L'asserzione assert 1 < 0 fallisce perché la condizione è falsa. Di conseguenza, viene sollevata un'eccezione AssertionError.
Risposte errate:
ValueError: Non è il tipo di errore generato dalle asserzioni.
SyntaxError: Non è un errore di sintassi.
TypeError: Non è un errore di tipo.
Qual è lo scopo di un decoratore in Python?
Risposta corretta: Modificare il comportamento di una funzione
Spiegazione/Esempio: I decoratori in Python sono usati per modificare o estendere il comportamento di una funzione o metodo. Ad esempio, un decoratore può aggiungere funzionalità aggiuntive prima o dopo l'esecuzione della funzione decorata.
Risposte errate:
Rendere una funzione più veloce: Non è lo scopo primario di un decoratore.
Rendere una funzione più leggibile: I decoratori non sono principalmente usati per migliorare la leggibilità.
Creare una nuova funzione: I decoratori non creano nuove funzioni, ma modificano il comportamento delle esistenti.
Quale libreria standard Python fornisce il supporto per i thread?
Risposta corretta: threading
Spiegazione/Esempio: Il modulo threading della libreria standard di Python fornisce il supporto per lavorare con i thread. Permette di creare, gestire e sincronizzare thread all'interno di un programma Python.
Risposte errate:
sys: Non è usato per il supporto dei thread.
os: Non è specifico per i thread, ma per operazioni di sistema.
multiprocessing: È usato per il supporto dei processi, non dei thread.
Perché è consigliato utilizzare ThreadPoolExecutor come context manager?
Risposta corretta: Per assicurarsi che i thread vengano uniti e chiusi correttamente
Spiegazione/Esempio: Utilizzare ThreadPoolExecutor come context manager assicura che tutti i thread completino il loro lavoro e che le risorse vengano liberate correttamente al termine del blocco di codice, evitando risorse non rilasciate.
Risposte errate:
Per creare più thread: Non è il motivo principale; è per la gestione corretta dei thread.
Per ridurre l'uso della memoria: Non è lo scopo del context manager.
Per aumentare la velocità di esecuzione: Non è il beneficio principale dell'uso del context manager.
Qual è uno dei vantaggi principali dei container?
Risposta corretta: Portabilità
Spiegazione/Esempio: I container offrono portabilità perché possono essere eseguiti su qualsiasi sistema che supporta il runtime del container, indipendentemente dalle differenze di ambiente. Questo consente di sviluppare e distribuire software in modo coerente su diverse piattaforme.
Risposte errate:
Latenza elevata: I container tendono a ridurre la latenza rispetto alle macchine virtuali.
Bassa efficienza: I container sono generalmente più efficienti delle macchine virtuali.
Consumo maggiore di risorse: I container hanno un consumo di risorse inferiore rispetto alle macchine virtuali.
Quale funzione viene chiamata per chiudere un file aperto in Python?
Risposta corretta: close()
Spiegazione/Esempio: Il metodo close() viene utilizzato per chiudere un file che è stato aperto. Ad esempio:
python
Copia codice
file = open('file.txt', 'r')
file.close()
Risposte errate:
end(): Non è una funzione per chiudere file.
finish(): Non è una funzione per chiudere file.
terminate(): Non è una funzione per chiudere file.
Qual è il vantaggio dell'utilizzo del GIL rispetto all'aggiunta di lock a tutte le strutture dati?
Risposta corretta: Previene i deadlock
Spiegazione/Esempio: Il GIL (Global Interpreter Lock) in Python previene i deadlock gestendo la sincronizzazione dell'accesso alle strutture dati in modo centralizzato. Senza GIL, ogni thread avrebbe bisogno di gestire i lock su tutte le strutture dati, il che potrebbe portare a situazioni di deadlock.
Risposte errate:
Aumenta la velocità: Non aumenta la velocità; il GIL limita l'esecuzione parallela.
Permette l'esecuzione parallela: Il GIL limita l'esecuzione parallela dei thread.
Riduce la memoria utilizzata: Non è il beneficio principale del GIL.
Che cos'è un deadlock in un contesto di multiprocessing?
Risposta corretta: Una situazione in cui due o più processi si bloccano a vicenda aspettando risorse
Spiegazione/Esempio: Un deadlock si verifica quando due o più processi si bloccano a vicenda, ciascuno aspettando che l'altro rilasci una risorsa. Ad esempio, se il processo A ha bloccato la risorsa 1 e aspetta la risorsa 2, mentre il processo B ha bloccato la risorsa 2 e aspetta la risorsa 1, entrambi i processi rimangono bloccati in un deadlock.
Risposte errate:
Un processo che termina inaspettatamente: Non è un deadlock, ma un crash o errore di processo.
Una tecnica di ottimizzazione delle risorse: Il deadlock è un problema, non una tecnica di ottimizzazione.
Un metodo per sincronizzare processi: La sincronizzazione può causare deadlock se non è gestita correttamente.
Quale eccezione viene sollevata quando si accede a una variabile non definita?
Risposta corretta: NameError
Spiegazione/Esempio: NameError viene sollevata quando si cerca di accedere a una variabile che non è stata definita. Ad esempio:
python
Copia codice
print(non_definita)
Questo solleverà un NameError.
Risposte errate:
AttributeError: Viene sollevata quando si accede a un attributo non esistente di un oggetto.
ValueError: Viene sollevata quando una funzione riceve un argomento con un valore corretto ma non appropriato.
TypeError: Viene sollevata quando un'operazione o funzione viene applicata a un oggetto di tipo errato.
Cosa rappresenta il metodo __exit__ di un context manager in Python?
Risposta corretta: Il metodo chiamato quando il flusso di esecuzione esce dal blocco with, indipendentemente dal fatto che si sia verificata un'eccezione o meno
Spiegazione/Esempio: Il metodo __exit__ viene chiamato quando il blocco with termina, sia che il blocco termini normalmente o a causa di un'eccezione. Ad esempio:
python
Copia codice
class MyContextManager:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with MyContextManager() as cm:
    print("Inside the context")
Questo stampa "Exiting the context" quando il blocco with termina.
Risposte errate:
Il metodo utilizzato per aprire un file: Non è corretto; il metodo __enter__ gestisce l'apertura.
Il metodo utilizzato per chiudere un file: Non è corretto; il metodo __exit__ gestisce la chiusura.
Il metodo chiamato quando il flusso di esecuzione entra nel blocco with: Non è corretto; quello è il metodo __enter__.
Quali sono le tre parti principali che compongono un file su sistemi moderni?
Risposta corretta: Header, Data, End of file (EOF)
Spiegazione/Esempio: In molti sistemi di file, i file sono composti da tre parti principali: un'intestazione (header) che contiene metadati e informazioni, i dati principali (data) e una marcatura di fine file (EOF) che indica la fine dei dati.
Risposte errate:
Name, Size, Type: Non rappresentano le parti interne di un file, ma piuttosto le informazioni sui file.
Metadata, Content, Footer: Questi non sono termini standard per la struttura interna di un file.
Start, Body, End: Non è una terminologia standard per la struttura dei file.
Come si può far sì che il processo principale attenda la fine dei processi figli?
Risposta corretta: Usando il metodo join
Spiegazione/Esempio: Il metodo join() viene utilizzato per bloccare il processo principale fino a quando i processi figli non sono terminati. Ad esempio:
python
Copia codice
from multiprocessing import Process

def worker():
    print("Worker")

p = Process(target=worker)
p.start()
p.join()  # Aspetta che il processo p finisca
Risposte errate:
Usando il metodo stop: Non è corretto; stop() è usato per terminare un processo.
Usando il metodo wait: wait() è usato in alcuni contesti, ma join() è il metodo standard per i processi.
Usando il metodo pause: Non esiste un metodo pause per questo scopo.
Quale modulo deve contenere una directory per essere considerata importabile per i test?
Risposta corretta: __init__.py
Spiegazione/Esempio: Un file __init__.py deve essere presente in una directory affinché Python la riconosca come un modulo e possa importarla. Questo è importante anche per l'importazione dei test.
Risposte errate:
__module__.py: Non è un modulo standard di Python.
__test__.py: Non è usato per rendere una directory importabile.
__main__.py: Non è utilizzato per rendere la directory importabile per i test.
Qual è la funzione in Python utilizzata per aprire un file?
Risposta corretta: open()
Spiegazione/Esempio: La funzione open() è utilizzata per aprire un file in Python. Ad esempio:
python
Copia codice
file = open('file.txt', 'r')
Risposte errate:
write(): Non apre file, ma scrive nei file.
close(): Non apre file, ma chiude i file aperti.
read(): Non apre file, ma legge i file già aperti.
Qual è il metodo utilizzato per scrivere una lista di stringhe in un file?
Risposta corretta: writelines()
Spiegazione/Esempio: Il metodo writelines() è usato per scrivere una lista di stringhe in un file. Ad esempio:
python
Copia codice
with open('file.txt', 'w') as file:
    file.writelines(['line1\n', 'line2\n'])
Risposte errate:
writeall(): Non esiste come metodo standard.
write(): Scrive una singola stringa, non una lista.
writefile(): Non esiste come metodo standard.
Qual è lo scopo del metodo start() nella libreria multiprocessing?
Risposta corretta: Avviare un nuovo processo
Spiegazione/Esempio: Il metodo start() viene utilizzato per avviare un nuovo processo creato con la classe Process della libreria multiprocessing. Ad esempio:
python
Copia codice
from multiprocessing import Process

def worker():
    print("Worker")

p = Process(target=worker)
p.start()  # Avvia il processo
Risposte errate:
Creare una nuova thread: Non è corretto; start() avvia un processo, non un thread.
Terminare un processo: start() non termina processi.
Sincronizzare due processi: start() non è usato per sincronizzare processi.
Cosa fa il comando docker run mytesting?
Risposta corretta: Esegue il contenitore basato sull'immagine mytesting
Spiegazione/Esempio: Il comando docker run avvia un nuovo contenitore basato sull'immagine specificata, in questo caso, mytesting. Ad esempio, docker run mytesting eseguirà il contenitore basato sull'immagine mytesting.
Risposte errate:
Rimuove un'immagine Docker chiamata mytesting: docker run non rimuove immagini.
Aggiorna un contenitore Docker chiamato mytesting: docker run non aggiorna contenitori.
Costruisce un'immagine Docker con il tag mytesting: docker run non costruisce immagini, ma le esegue.
Cosa include un container?
Risposta corretta: Codice, runtime, strumenti di sistema e librerie
Spiegazione/Esempio: Un container include tutto il necessario per eseguire l'applicazione: il codice applicativo, le librerie necessarie, il runtime e gli strumenti di sistema. Questo garantisce che l'applicazione si comporti in modo coerente in ambienti diversi.
Risposte errate:
Solo gli strumenti di sistema: Non include il codice applicativo o le librerie necessarie.
Solo il runtime: Non include le librerie o il codice applicativo.
Solo il codice applicativo: Non include il runtime, le librerie o gli strumenti di sistema.
Come si specifica una clausola except che cattura solo l'eccezione TypeError?
Risposta corretta: except TypeError as e
Spiegazione/Esempio: La clausola except TypeError as e cattura specificamente l'eccezione TypeError e la associa alla variabile e. Ad esempio:
python
Copia codice
try:
    x = int("stringa")
except TypeError as e:
    print("Errore:", e)
Risposte errate:
except Exception as e: Cattura tutte le eccezioni di tipo Exception, non solo TypeError.
except e: TypeError: Non è una sintassi valida.
except e: Exception: Non è una sintassi valida e non specifica TypeError.
Quale libreria Python è utilizzata per il multiprocessing?
Risposta corretta: multiprocessing
Spiegazione/Esempio: La libreria multiprocessing in Python consente di creare e gestire processi separati. Ad esempio:
python
Copia codice
from multiprocessing import Process

def worker():
    print("Worker")

p = Process(target=worker)
p.start()
p.join()
Risposte errate:
asyncio: Utilizzata per la programmazione asincrona, non per il multiprocessing.
threading: Utilizzata per i thread, non per il multiprocessing.
multiprocess: Non è una libreria standard, mentre multiprocessing è quella corretta.
Qual è un potenziale problema dell'aggiunta di lock a tutte le strutture dati condivise?
Risposta corretta: Deadlock
Spiegazione/Esempio: Aggiungere lock a tutte le strutture dati condivise può portare a situazioni di deadlock, dove due o più processi o thread si bloccano a vicenda aspettando risorse. È importante gestire i lock con attenzione per evitare questo problema.
Risposte errate:
Aumento della velocità: I lock non aumentano la velocità; possono rallentare l'esecuzione.
Miglioramento delle prestazioni: L'uso eccessivo di lock può ridurre le prestazioni.
Riduzione della memoria: L'uso di lock non influisce direttamente sulla memoria.
Come si definisce una funzione all'interno di un'altra funzione in Python?
Risposta corretta: Nested function
Spiegazione/Esempio: Una funzione definita all'interno di un'altra funzione è chiamata funzione annidata o nested function. Ad esempio:
python
Copia codice
def outer_function():
    def inner_function():
        print("Inside inner function")
    inner_function()
outer_function()
Risposte errate:
Inner function: Non è il termine standard, anche se spesso usato.
Internal function: Non è un termine standard per una funzione annidata.
Sub function: Non è un termine usato per descrivere una funzione annidata.
Come si esegue un singolo file di test con unittest?
Risposta corretta: python -m unittest nome_test
Spiegazione/Esempio: Il comando python -m unittest nome_test esegue i test presenti nel file specificato. Ad esempio, se il file si chiama test_mio.py, il comando sarà:
sh
Copia codice
python -m unittest test_mio
Risposte errate:
python -m unittest -v nome_file: -v è per la modalità verbosa, ma non è necessario per eseguire un file specifico.
python -m unittest -v directory: Esegue tutti i test nella directory, non un singolo file.
python -m unittest -v nome_metodo: Esegue un metodo di test specifico, non un file intero.
Quale dei seguenti non è un esempio di utilizzo dei decoratori?
Risposta corretta: Aumentare la velocità di esecuzione delle funzioni
Spiegazione/Esempio: I decoratori in Python sono utilizzati per aggiungere funzionalità come logging, memorizzazione o modifica del comportamento di una funzione, ma non per aumentare direttamente la velocità di esecuzione. Ad esempio:
python
Copia codice
def my_decorator(func):
    def wrapper():
        print("Something before the function")
        func()
        print("Something after the function")
    return wrapper
@my_decorator
def say_hello():
    print("Hello")
say_hello()
Risposte errate:
Aggiungere funzionalità di logging: I decoratori possono essere usati per questo.
Stampare informazioni: I decoratori possono essere usati per questo.
Aggiungere funzionalità di memorizzazione: I decoratori possono essere usati per questo.
Quale clausola si utilizza per eseguire il codice solo se non ci sono eccezioni?
Risposta corretta: else
Spiegazione/Esempio: La clausola else viene eseguita solo se non ci sono state eccezioni nel blocco try. Ad esempio:
python
Copia codice
try:
    print("No exception")
except ValueError:
    print("Caught ValueError")
else:
    print("No exception occurred")
Risposte errate:
finally: Viene eseguita sempre, sia che ci siano eccezioni sia che non ce ne siano.
then: Non è una parola chiave in Python.
except: Cattura eccezioni, non esegue codice senza eccezioni.
Qual è il comando utilizzato per eseguire tutti i test in una directory in Python?
Risposta corretta: python -m unittest
Spiegazione/Esempio: Il comando python -m unittest esegue tutti i test all'interno della directory corrente, cercando i file di test e i metodi di test. Ad esempio:
sh
Copia codice
python -m unittest discover
Risposte errate:
python run tests: Non è un comando standard per l'esecuzione dei test.
python test all: Non è un comando standard per l'esecuzione dei test.
python unittest all: Non è un comando standard per l'esecuzione dei test.
Qual è la soluzione per proteggere il conteggio dei riferimenti in un ambiente multi-thread?
Risposta corretta: Aggiungere lock a tutte le strutture dati condivise
Spiegazione/Esempio: In un ambiente multi-thread, l'uso di lock può proteggere le strutture dati condivise e prevenire condizioni di gara (race conditions). Ad esempio:
python
Copia codice
from threading import Lock

lock = Lock()
shared_data = 0

def thread_function():
    global shared_data
    with lock:
        shared_data += 1
Risposte errate:
Aumentare il numero di thread: Non risolve i problemi di sincronizzazione.
Ridurre l'uso della memoria: Non è una soluzione per la sincronizzazione dei dati.
Utilizzare variabili globali: Non gestisce i problemi di concorrenza.
Quale parola chiave viene utilizzata in Python per sollevare un'eccezione?
Risposta corretta: raise
Spiegazione/Esempio: La parola chiave raise è utilizzata per sollevare eccezioni in Python. Ad esempio:
python
Copia codice
raise ValueError("Messaggio di errore")
Risposte errate:
error: Non è una parola chiave per sollevare eccezioni.
throw: È usata in altri linguaggi di programmazione, ma non in Python.
catch: È usata per gestire eccezioni, non per sollevarle.
Quale funzione utilizza Python per il conteggio dei riferimenti?
Risposta corretta: sys.getrefcount()
Spiegazione/Esempio: La funzione sys.getrefcount() restituisce il conteggio dei riferimenti di un oggetto in Python. Ad esempio:
python
Copia codice
import sys
x = []
print(sys.getrefcount(x))
Risposte errate:
os.countrefs(): Non esiste una funzione del genere.
sys.countrefs(): Non esiste una funzione del genere.
os.getrefcount(): Non esiste una funzione del genere.
Quale parola chiave viene utilizzata per definire una funzione in Python?
Risposta corretta: def
Spiegazione/Esempio: La parola chiave def viene utilizzata per definire una funzione in Python. Ad esempio:
python
Copia codice
def my_function():
    print("Hello")
Risposte errate:
function: Non è una parola chiave in Python.
define: Non è una parola chiave in Python.
func: Non è una parola chiave in Python.
Qual è il comando per eseguire un contenitore Docker?
Risposta corretta: docker run
Spiegazione/Esempio: Il comando docker run esegue un contenitore basato su un'immagine Docker. Ad esempio:
sh
Copia codice
docker run my_image
Risposte errate:
docker create: Crea un contenitore, ma non lo avvia.
docker start: Avvia un contenitore esistente.
docker build: Costruisce un'immagine Docker, non esegue un contenitore.
Qual è il comando per costruire un'immagine Docker da un Dockerfile?
Risposta corretta: docker build
Spiegazione/Esempio: Il comando docker build costruisce un'immagine Docker a partire da un Dockerfile. Ad esempio:
sh
Copia codice
docker build -t my_image .
Risposte errate:
docker create: Non è usato per costruire immagini.
docker image: Non è un comando per costruire immagini.
docker run: Esegue un contenitore, non costruisce un'immagine.
In quale scenario i thread sono particolarmente utili?
Risposta corretta: Quando i compiti attendono eventi esterni
Spiegazione/Esempio: I thread sono particolarmente utili per compiti che attendono eventi esterni o operazioni di I/O, come le richieste di rete o le operazioni di lettura/scrittura su file. Questo consente al programma di continuare a funzionare mentre attende l'evento esterno.
Risposte errate:
Quando i compiti sono brevi: Non è un uso specifico dei thread.
Quando i compiti sono sequenziali: I thread non sono particolarmente utili per compiti sequenziali.
Quando i compiti richiedono calcoli pesanti: I thread non sono sempre efficaci per compiti CPU-bound a causa del GIL.
Cosa può causare un race condition nella gestione della memoria?
Risposta corretta: Due thread che modificano il conteggio dei riferimenti simultaneamente
Spiegazione/Esempio: Una race condition si verifica quando due o più thread modificano simultaneamente una variabile condivisa, come il conteggio dei riferimenti, senza una sincronizzazione adeguata. Questo può portare a comportamenti imprevedibili.
Risposte errate:
Due thread che eseguono la stessa funzione: Non necessariamente causano una race condition senza accesso a dati condivisi.
Un thread che attende un evento esterno: Non causa una race condition.
Un thread che accede a un file: Non causa direttamente una race condition a meno che non ci sia una modifica simultanea.
Qual è l'effetto del GIL sui programmi multithreaded in Python?
Risposta corretta: Limita l'utilizzo effettivo dei threads ai programmi I/O Bounded
Spiegazione/Esempio: Il Global Interpreter Lock (GIL) limita la possibilità di eseguire codice Python in parallelo su più thread, rendendolo meno efficace per programmi CPU-bound ma adatto per programmi I/O-bound.
Risposte errate:
Permette il parallelismo reale su tutti i tipi di programmi: Il GIL limita il parallelismo reale.
Rimuove la necessità di sincronizzazione dei thread: Non lo fa.
Aumenta l'efficienza dei programmi CPU-bound: Il GIL può ridurre l'efficienza dei programmi CPU-bound.
Quale comando della libreria multiprocessing permette di creare un nuovo processo?
Risposta corretta: Process()
Spiegazione/Esempio: Il comando Process() della libreria multiprocessing viene utilizzato per creare e gestire nuovi processi. Ad esempio:
python
Copia codice
from multiprocessing import Process

def worker():
    print("Worker")

p = Process(target=worker)
p.start()
p.join()
Risposte errate:
run(): Non è un metodo per creare processi.
Thread(): È usato per creare thread, non processi.
start(): Avvia un processo o un thread, ma non lo crea.
Qual è il vantaggio dell'utilizzo di Docker in sviluppo?
Risposta corretta: Assicura che l'applicazione funzioni allo stesso modo in diversi ambienti
Spiegazione/Esempio: Docker crea ambienti isolati chiamati container, che garantiscono che l'applicazione e tutte le sue dipendenze funzionino allo stesso modo in qualsiasi ambiente, sia di sviluppo che di produzione. Questo riduce il problema del "funziona sul mio computer".
Risposte errate:
Riduce la portabilità: Docker migliora la portabilità, non la riduce.
Aumenta la complessità del codice: Docker gestisce l'ambiente, non il codice applicativo.
Aumenta il consumo di risorse: I container sono generalmente più leggeri delle VM.
Quale tecnologia permette di creare ambienti simulati su una singola macchina fisica?
Risposta corretta: Containerizzazione
Spiegazione/Esempio: La containerizzazione permette di creare ambienti isolati all'interno di una sola macchina fisica, come i container Docker, che condividono il kernel del sistema operativo ma sono altrimenti indipendenti.
Risposte errate:
Virtualizzazione: Crea ambienti separati attraverso VM, che richiedono più risorse rispetto ai container.
Automazione: Non è specifica per la creazione di ambienti simulati.
Scripting: Non crea ambienti simulati, ma può essere usato per automatizzare compiti.
Quale comando esegue una singola funzione di test all'interno di un file di test con unittest?
Risposta corretta: python -m unittest -v nome_file.nome_classe.nome_funzione
Spiegazione/Esempio: Questo comando esegue una specifica funzione di test all'interno di una classe di test in un file di test. Ad esempio:
sh
Copia codice
python -m unittest -v test_module.MyTestCase.test_method
Risposte errate:
python -m unittest -v nome_classe.nome_funzione: Non specifica il file di test.
python -m unittest -v nome_test.nome_funzione: Non è un formato valido per unittest.
python -m unittest -v nome_file.nome_funzione: Non specifica la classe di test.
Qual è un altro vantaggio dei container rispetto alle VM?
Risposta corretta: Efficienza
Spiegazione/Esempio: I container sono più efficienti rispetto alle VM in termini di utilizzo delle risorse, poiché condividono il kernel del sistema operativo e non richiedono un intero sistema operativo per ogni istanza.
Risposte errate:
Consumo maggiore di risorse: I container consumano meno risorse rispetto alle VM.
Latenza elevata: I container tendono ad avere una latenza inferiore rispetto alle VM.
Dipendenza dall'hardware: I container sono progettati per essere indipendenti dall'hardware sottostante.
Quale modulo in Python fornisce funzioni per lavorare con il sistema operativo, inclusa la gestione dei file?
Risposta corretta: os
Spiegazione/Esempio: Il modulo os fornisce funzioni per interagire con il sistema operativo, comprese le operazioni sui file e la gestione dei percorsi. Ad esempio:
python
Copia codice
import os
os.listdir()
Risposte errate:
file: Non esiste un modulo chiamato file per la gestione del sistema operativo.
numpy: È una libreria per il calcolo numerico, non per la gestione del sistema operativo.
path: Non è un modulo standard; pathlib è usato per operazioni sui percorsi.
Cosa rappresenta il metodo enter di un context manager in Python?
Risposta corretta: Il metodo chiamato quando il flusso di esecuzione entra nel blocco with
Spiegazione/Esempio: Il metodo __enter__ viene chiamato quando l'esecuzione entra nel blocco with di un context manager. Ad esempio:
python
Copia codice
class MyContextManager:
    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit")

with MyContextManager():
    print("Inside")
Risposte errate:
Il metodo utilizzato per chiudere un file: Questo è __exit__.
Il metodo utilizzato per aprire un file: Questo è gestito dal __enter__, ma non è l'unica operazione.
Il metodo chiamato quando il flusso di esecuzione esce dal blocco with: Questo è __exit__.
Qual è l'output di assert 1 > 0 se la condizione è vera?
Risposta corretta: Nessun output
Spiegazione/Esempio: Quando l'asserzione è vera, non viene sollevata alcuna eccezione e quindi non c'è output. Ad esempio:
python
Copia codice
assert 1 > 0  # Nessun output se la condizione è vera
Risposte errate:
True: assert non produce output se la condizione è vera.
False: Non è applicabile perché la condizione è vera.
AssertionError: Viene sollevato solo se la condizione è falsa.
Qual è il vantaggio principale dell'utilizzo dei decoratori?
Risposta corretta: Modificare facilmente il comportamento delle funzioni senza modificarne il codice
Spiegazione/Esempio: I decoratori permettono di aggiungere o modificare funzionalità delle funzioni in modo modulare e riutilizzabile senza alterare il loro codice. Ad esempio:
python
Copia codice
def my_decorator(func):
    def wrapper():
        print("Something before")
        func()
        print("Something after")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
Risposte errate:
Aumentare il numero di funzioni in un programma: Non è lo scopo principale dei decoratori.
Rendere il codice più leggibile: Non è sempre vero; i decoratori possono a volte complicare la lettura.
Rendere le funzioni più veloci: Non è l'obiettivo principale dei decoratori.
Cos'è un'asserzione (assert) in Python?
Risposta corretta: Una parola chiave di python che verifica se una condizione/valore è vera o falsa
Spiegazione/Esempio: assert è usato per verificare se una condizione è vera e sollevare un'eccezione se non lo è. Ad esempio:
python
Copia codice
assert 1 + 1 == 2  # Non solleva eccezioni
Risposte errate:
Una funzione per gestire gli errori: Non è una funzione di gestione degli errori.
Una libreria di debug: Non è una libreria, ma una dichiarazione.
Un modulo di test in Python: Non è un modulo, ma una funzionalità del linguaggio.
Quale clausola viene utilizzata per eseguire azioni di pulizia dopo l'esecuzione del codice?
Risposta corretta: finally
Spiegazione/Esempio: La clausola finally viene utilizzata per eseguire codice di pulizia, che viene eseguito indipendentemente dal fatto che sia stata sollevata un'eccezione o meno. Ad esempio:
python
Copia codice
try:
    # codice che potrebbe sollevare un'eccezione
    pass
finally:
    # codice di pulizia
    pass
Risposte errate:
cleanup: Non è una clausola valida in Python.
finish: Non è una clausola valida in Python.
end: Non è una clausola valida in Python.
Qual è lo scopo del metodo assertRaises in unittest?
Risposta corretta: Verificare se viene sollevata un'eccezione specifica
Spiegazione/Esempio: Il metodo assertRaises è usato per verificare che un blocco di codice sollevi una specifica eccezione. Ad esempio:
python
Copia codice
import unittest

class TestExample(unittest.TestCase):
    def test_raise(self):
        with self.assertRaises(ValueError):
            raise ValueError("An error occurred")
Risposte errate:
Verificare se una variabile è None: Usa assertIsNone.
Verificare se due valori sono uguali: Usa assertEqual.
Verificare se una condizione è vera: Usa assertTrue.
Cosa significa che i container sono isolati?
Risposta corretta: Ogni container esegue un'applicazione e le sue dipendenze senza interferire con altri container
Spiegazione/Esempio: L'isolamento dei container significa che ogni container ha il proprio ambiente di esecuzione e dipendenze, separati da quelli degli altri container. Questo impedisce che le applicazioni nei container interferiscano tra loro.
Risposte errate:
I container condividono tutte le risorse tra loro: I container sono progettati per essere indipendenti e non condividono le risorse in modo che possano operare isolatamente.
I container dipendono dalle macchine virtuali: I container non dipendono dalle VM; sono più leggeri e usano il sistema operativo sottostante.
I container non possono essere eseguiti contemporaneamente: I container possono essere eseguiti simultaneamente e sono progettati per questo scopo.
Qual è uno dei benefici della rapida distribuzione dei container?
Risposta corretta: Scalabilità
Spiegazione/Esempio: La rapidità di distribuzione dei container consente di scalare facilmente le applicazioni, distribuendo rapidamente nuove istanze dei container per gestire carichi di lavoro più elevati.
Risposte errate:
Consumo maggiore di risorse: I container sono progettati per essere leggeri e consumano meno risorse rispetto alle VM.
Dipendenza dall'hardware: I container sono progettati per essere indipendenti dall'hardware sottostante.
Latenza elevata: I container tendono ad avere una bassa latenza rispetto alle VM.
Qual è il metodo consigliato per aprire e chiudere file in Python per garantire un codice più pulito?
Risposta corretta: with statement
Spiegazione/Esempio: Utilizzare il with statement per gestire file garantisce che i file vengano automaticamente chiusi anche se si verifica un'eccezione. Ad esempio:
python
Copia codice
with open('file.txt', 'r') as file:
    content = file.read()
Risposte errate:
try-finally block: Sebbene sia un metodo valido, with è più conciso e gestisce automaticamente la chiusura dei file.
try-except block: Non è progettato specificamente per la gestione dei file.
open-close block: Non è una sintassi valida in Python.
Quando è preferibile utilizzare il multiprocessing rispetto al threading?
Risposta corretta: Quando si eseguono operazioni CPU-bound
Spiegazione/Esempio: Il multiprocessing è più adatto per operazioni che richiedono molta elaborazione della CPU, poiché ogni processo ha il proprio spazio di memoria e può sfruttare più CPU fisiche, evitando le limitazioni del GIL (Global Interpreter Lock).
Risposte errate:
Quando si eseguono operazioni I/O-bound: Il threading può essere più efficace per operazioni che attendono input/output.
Quando si eseguono operazioni leggere: Multiprocessing è più utile per operazioni CPU-intensive.
Quando si utilizza solo un processore: Multiprocessing è progettato per sfruttare più processori.
Qual è uno svantaggio delle macchine virtuali (VM)?
Risposta corretta: Consumo maggiore di risorse
Spiegazione/Esempio: Le VM richiedono un intero sistema operativo per ogni istanza, il che può comportare un maggiore consumo di risorse rispetto ai container, che condividono il kernel del sistema operativo.
Risposte errate:
Alta portabilità: Le VM sono generalmente meno portabili rispetto ai container.
Isolamento debole: Le VM offrono un buon isolamento rispetto ai container.
Bassa efficienza: Le VM tendono ad avere una bassa efficienza rispetto ai container a causa della sovrapposizione del sistema operativo.
Cos'è un Dockerfile?
Risposta corretta: Un file con le istruzioni per costruire un'immagine Docker
Spiegazione/Esempio: Un Dockerfile è un file di testo che contiene una serie di istruzioni per creare un'immagine Docker. Ad esempio:
dockerfile
Copia codice
FROM python:3.8
COPY . /app
RUN pip install -r /app/requirements.txt
CMD ["python", "/app/app.py"]
Risposte errate:
Una libreria Docker: Non è una libreria, ma un file di configurazione.
Un comando Docker: Non è un comando, ma un file di istruzioni.
Un contenitore Docker: Un Dockerfile crea un'immagine, non un contenitore.
Qual è la differenza tra multiprocessing e threading in Python?
Risposta corretta: Multiprocessing crea processi separati con la propria memoria, mentre threading crea thread all'interno dello stesso processo con memoria condivisa
Spiegazione/Esempio: Multiprocessing usa processi separati che hanno il proprio spazio di memoria, mentre threading usa thread all'interno dello stesso processo, condividendo la memoria e risorse del processo.
Risposte errate:
Threading crea processi separati con la propria memoria, mentre multiprocessing crea thread all'interno dello stesso processo con memoria condivisa: L'opposto di quanto descritto.
Non c'è differenza tra multiprocessing e threading: Esiste una differenza significativa.
Multiprocessing è più veloce di threading in tutti i casi: Non è vero in tutti i casi, specialmente per operazioni I/O-bound.
Come si può catturare qualsiasi eccezione generica?
Risposta corretta: except Exception as e
Spiegazione/Esempio: Utilizzare except Exception as e permette di catturare tutte le eccezioni che derivano dalla classe Exception, che è la maggior parte delle eccezioni standard in Python. Ad esempio:
python
Copia codice
try:
    # codice che potrebbe sollevare un'eccezione
    pass
except Exception as e:
    print(e)
Risposte errate:
except BaseException as e: Cattura tutte le eccezioni, incluse quelle che non sono derivate da Exception.
except AllExceptions as e: Non esiste una classe AllExceptions.
except Error as e: Non esiste una classe Error per catturare tutte le eccezioni.
Come si specifica un messaggio personalizzato in un'asserzione?
Risposta corretta: assert condizione, 'messaggio'
Spiegazione/Esempio: Utilizzare assert condizione, 'messaggio' permette di aggiungere un messaggio personalizzato che viene visualizzato se l'asserzione fallisce. Ad esempio:
python
Copia codice
assert 1 == 2, "1 non è uguale a 2"
Risposte errate:
assert 'messaggio', condizione: L'ordine è sbagliato.
assert condizione as 'messaggio': Non è una sintassi valida per gli assert.
assert 'messaggio' if condizione: Non è una sintassi valida per gli assert.
Quale tipo di eccezione viene sollevata se si tenta di aprire un file che non esiste in modalità read?
Risposta corretta: FileNotFoundError
Spiegazione/Esempio: FileNotFoundError viene sollevata quando si tenta di aprire un file che non esiste e si usa la modalità di lettura. Ad esempio:
python
Copia codice
with open('non_esiste.txt', 'r') as file:
    content = file.read()
Risposte errate:
EOFError: Viene sollevata quando si cerca di leggere oltre la fine di un file.
OSError: È una classe base per errori di I/O, ma non specifica il file non trovato.
IOError: Era usata in versioni precedenti di Python, ora FileNotFoundError è preferita.
Qual è la differenza principale tra un thread e un processo?
Risposta corretta: Un thread è un flusso di esecuzione separato all'interno di un processo; un processo è un'istanza di un programma in esecuzione
Spiegazione/Esempio: Un thread è un'unità di esecuzione all'interno di un processo e condivide lo spazio di memoria del processo, mentre un processo è un'entità separata con il proprio spazio di memoria.
Risposte errate:
Un thread è un tipo di dato; un processo è un'operazione aritmetica: Questa affermazione è errata.
Non c'è differenza: C'è una differenza significativa.
Un processo è un flusso di esecuzione separato all'interno di un thread; un thread è un'istanza di un programma in esecuzione: È l'opposto di quanto descritto.
Quale simbolo viene utilizzato per applicare un decoratore a una funzione?
Risposta corretta: @
Spiegazione/Esempio: Il simbolo @ viene usato per applicare un decoratore a una funzione. Ad esempio:
python
Copia codice
@decoratore
def funzione():
    pass
Risposte errate:
$: Non è utilizzato per i decoratori.
&: Non è utilizzato per i decoratori.
Quali sono i due principali framework per unit test in Python?
Risposta corretta: unittest e PyTest
Spiegazione/Esempio: unittest è il framework di testing standard di Python, mentre pytest è una libreria di testing molto popolare con caratteristiche avanzate.
Risposte errate:
assert e unittest: assert è una dichiarazione di asserzione, non un framework di testing.
unittest e debug: debug non è un framework di testing.
pytest e assert: assert non è un framework di testing.
Cosa permette di fare la funzione wrapper() all'interno di un decoratore?
Risposta corretta: Avvolge la funzione originale e ne modifica il comportamento
Spiegazione/Esempio: La funzione wrapper in un decoratore permette di eseguire codice aggiuntivo prima o dopo la chiamata alla funzione originale, modificandone il comportamento. Ad esempio:
python
Copia codice
def decoratore(func):
    def wrapper(*args, **kwargs):
        print("Prima della funzione")
        result = func(*args, **kwargs)
        print("Dopo la funzione")
        return result
    return wrapper
Risposte errate:
Esegue la funzione originale senza modifiche: Non è l'obiettivo di wrapper.
Elimina la funzione originale: Non è ciò che fa un decoratore.
Sostituisce la funzione originale: Non è corretto; la funzione originale viene avvolta e non sostituita.
Cosa significa che Python tratta le funzioni come first-class objects?
Risposta corretta: Le funzioni possono essere passate come argomenti e restituite da altre funzioni
Spiegazione/Esempio: In Python, le funzioni possono essere assegnate a variabili, passate come argomenti e restituite da altre funzioni. Ad esempio:
python
Copia codice
def funzione():
    return "Ciao"

def chiamante(func):
    return func()

print(chiamante(funzione))  # Output: Ciao
Risposte errate:
Le funzioni devono essere globali: Le funzioni non devono essere globali.
Le funzioni non possono essere modificate: Le funzioni possono essere modificate.
Le funzioni possono essere utilizzate solo all'interno di altre funzioni: Le funzioni possono essere utilizzate anche al di fuori di altre funzioni.
Quale carattere speciale indica la fine di un file?
Risposta corretta: EOF
Spiegazione/Esempio: EOF (End Of File) è un carattere speciale che indica la fine di un file in molti contesti di programmazione.
Risposte errate:
EOL: Indica la fine di una riga.
EOT: End Of Transmission, usato in contesti di comunicazione.
END: Non è uno standard per indicare la fine di un file.
Cosa rappresenta un programma CPU-bound?
Risposta corretta: Un programma che spinge la CPU al limite
Spiegazione/Esempio: Un programma CPU-bound è quello che consuma molte risorse della CPU e quindi il tempo di esecuzione è limitato dalla velocità della CPU.
Risposte errate:
Un programma che esegue operazioni di I/O: Questi sono tipicamente I/O-bound.
Un programma che accede alla rete: Potrebbe essere I/O-bound.
Un programma che attende input/output: Tipicamente I/O-bound.
Come si passa un messaggio personalizzato a un'asserzione in Python?
Risposta corretta: assert condizione, 'messaggio'
Spiegazione/Esempio: Per aggiungere un messaggio personalizzato a un'asserzione, si usa la sintassi assert condizione, 'messaggio'. Ad esempio:
python
Copia codice
assert 1 == 2, "1 non è uguale a 2"
Risposte errate:
assert condizione as 'messaggio': Non è una sintassi valida.
assert 'messaggio', condizione: L'ordine è sbagliato.
assert 'messaggio' if condizione: Non è una sintassi valida.
Qual è il problema principale del GIL?
Risposta corretta: Può essere un collo di bottiglia per le prestazioni in programmi multi-thread
Spiegazione/Esempio: Il GIL (Global Interpreter Lock) in Python impedisce l'esecuzione simultanea di più thread in un processo, limitando le prestazioni dei programmi multi-thread che eseguono operazioni CPU-bound.
Risposte errate:
Riduce la velocità di esecuzione: Non è l'unico problema.
Impedisce l'accesso ai file: Non è collegato all'accesso ai file.
Rende impossibile l'esecuzione di più thread: Non rende impossibile, ma limita le prestazioni.
4o mini

Qual è un esempio di programma che potrebbe beneficiare dell'uso dei thread?
Risposta corretta: Un programma che attende input dall'utente
Spiegazione/Esempio: I thread possono essere particolarmente utili per gestire attività in attesa di input o eventi esterni senza bloccare l'esecuzione principale del programma. Ad esempio, un'applicazione GUI che deve rispondere a input dell'utente mentre esegue altre operazioni in background.
Risposte errate:
Un programma che accede alla memoria condivisa: Questo non è specifico per i thread.
Un programma che esegue calcoli matematici intensivi: Per calcoli pesanti, il multiprocessing è generalmente più adatto.
Un programma che non richiede attesa: I thread sono utili quando ci sono attese, non quando non ci sono.
Quale metodo viene utilizzato per verificare se una condizione è vera in unittest?
Risposta corretta: assertTrue
Spiegazione/Esempio: assertTrue verifica che una condizione sia vera. Ad esempio:
python
Copia codice
self.assertTrue(1 < 2)
Risposte errate:
assertValid: Non esiste.
assertCondition: Non esiste.
assertTruth: Non esiste.
Cosa fa il comando "docker build -t mytesting ." ?
Risposta corretta: Costruisce un'immagine Docker con il tag mytesting
Spiegazione/Esempio: Il comando docker build -t mytesting . costruisce un'immagine Docker usando il Dockerfile nella directory corrente e la tagga come mytesting.
Risposte errate:
Rimuove un'immagine Docker chiamata mytesting: Non è corretto.
Esegue un contenitore Docker chiamato mytesting: Non è corretto.
Aggiorna un contenitore Docker chiamato mytesting: Non è corretto.
Qual è il formato di default per aprire un file in Python?
Risposta corretta: 'r'
Spiegazione/Esempio: Il formato di default per aprire un file in Python è 'r' (lettura). Ad esempio:
python
Copia codice
with open('file.txt', 'r') as file:
    content = file.read()
Risposte errate:
'x': Per apertura in esclusiva, solo se non esiste.
'a': Per apertura in append.
'w': Per apertura in scrittura (crea un file vuoto o sovrascrive).
Qual è la classe base per la maggior parte delle eccezioni incorporate in Python?
Risposta corretta: Exception
Spiegazione/Esempio: Exception è la classe base per la maggior parte delle eccezioni incorporate in Python. Ad esempio:
python
Copia codice
try:
    raise ValueError("Errore")
except Exception as e:
    print(e)
Risposte errate:
BaseException: È la classe base per tutte le eccezioni, ma Exception è più comune per la maggior parte delle eccezioni.
CustomException: Non è una classe predefinita.
StandardError: Era usata in Python 2, ma non in Python 3.
Quale metodo viene utilizzato per verificare se un valore è True in unittest?
Risposta corretta: assertTrue
Spiegazione/Esempio: assertTrue verifica che il valore sia True. Ad esempio:
python
Copia codice
self.assertTrue(1 == 1)
Risposte errate:
assertTruth: Non esiste.
assertValid: Non esiste.
assertCondition: Non esiste.
Qual è il metodo utilizzato per scrivere una stringa in un file?
Risposta corretta: write()
Spiegazione/Esempio: write() è utilizzato per scrivere una stringa in un file. Ad esempio:
python
Copia codice
with open('file.txt', 'w') as file:
    file.write("Ciao mondo")
Risposte errate:
writeall(): Non esiste.
writefile(): Non esiste.
writelines(): Utilizzato per scrivere una lista di stringhe, non una singola stringa.
Quale delle seguenti non è una caratteristica delle funzioni in Python? (Leggere attentamente la domanda)
Risposta corretta: Possono essere utilizzate solo come decoratori
Spiegazione/Esempio: Le funzioni in Python possono essere assegnate a variabili, restituite da altre funzioni e passate come argomenti. Tuttavia, non sono utilizzate esclusivamente come decoratori.
Risposte errate:
Possono essere assegnate a variabili: Corretta.
Possono essere restituite da altre funzioni: Corretta.
Possono essere passate come argomenti: Corretta.
Qual è il metodo utilizzato per confrontare se due valori non sono uguali in unittest?
Risposta corretta: assertNotEqual
Spiegazione/Esempio: assertNotEqual verifica che due valori non siano uguali. Ad esempio:
python
Copia codice
self.assertNotEqual(1, 2)
Risposte errate:
assertDifferent: Non esiste.
assertNotSame: Non esiste.
assertNonEqual: Non esiste.
Cosa virtualizzano le macchine virtuali (VM)?
Risposta corretta: L'hardware
Spiegazione/Esempio: Le macchine virtuali virtualizzano l'hardware, creando un ambiente simulato per eseguire sistemi operativi e applicazioni.
Risposte errate:
Il sistema operativo: Le VM virtualizzano l'hardware, non il sistema operativo.
La rete: Non è l'obiettivo principale delle VM.
Le applicazioni: Non virtualizzano le applicazioni, ma l'hardware.
Quale modulo include ThreadPoolExecutor?
Risposta corretta: concurrent.futures
Spiegazione/Esempio: ThreadPoolExecutor è una classe fornita dal modulo concurrent.futures, che offre un'interfaccia ad alto livello per gestire pool di thread. Ad esempio:
python
Copia codice
from concurrent.futures import ThreadPoolExecutor
Risposte errate:
multiprocessing: Non include ThreadPoolExecutor.
threading: Non include ThreadPoolExecutor.
os: Non include ThreadPoolExecutor.
Qual è il comportamento della funzione passata come argomento senza parentesi?
Risposta corretta: Viene passata solo una referenza alla funzione senza eseguirla
Spiegazione/Esempio: Quando si passa una funzione come argomento senza parentesi, si passa solo una referenza alla funzione, non il risultato dell'esecuzione della funzione. Ad esempio:
python
Copia codice
def greet():
    return "Hello"

def call_function(func):
    return func()

print(call_function(greet))  # Passando greet senza parentesi
Risposte errate:
La funzione viene ignorata: Non corretto.
La funzione viene convertita in una stringa: Non corretto.
La funzione viene eseguita immediatamente: Non corretto.
In Python, cosa significa che le funzioni sono oggetti di prima classe?
Risposta corretta: Possono essere passate e utilizzate come argomenti, proprio come qualsiasi altro oggetto
Spiegazione/Esempio: Le funzioni possono essere trattate come oggetti, passate come argomenti, restituite da altre funzioni e assegnate a variabili. Ad esempio:
python
Copia codice
def add(a, b):
    return a + b

def operate(func, x, y):
    return func(x, y)

print(operate(add, 2, 3))  # Passa la funzione add come argomento
Risposte errate:
Possono essere utilizzate solo come decoratori: Non corretto.
Possono essere definite all'interno di altre funzioni: Non esprime completamente il concetto.
Possono essere solo funzioni globali: Non corretto.
Quale blocco di codice viene utilizzato in Python per gestire le eccezioni?
Risposta corretta: try-except
Spiegazione/Esempio: Il blocco try-except è utilizzato per gestire le eccezioni in Python. Ad esempio:
python
Copia codice
try:
    1 / 0
except ZeroDivisionError:
    print("Divisione per zero!")
Risposte errate:
try-rescue: Non esiste in Python.
try-handle: Non esiste in Python.
try-catch: È usato in altri linguaggi come Java, non in Python.
Qual è la modalità di apertura di default per la funzione open() in Python?
Risposta corretta: read-only
Spiegazione/Esempio: La modalità di apertura di default per open() è 'r' che indica la lettura (read-only). Ad esempio:
python
Copia codice
with open('file.txt') as file:
    content = file.read()
Risposte errate:
write-only: Non è la modalità di default.
append: Non è la modalità di default.
exclusive creation: Non è una modalità di default.
Qual è lo scopo della clausola finally in un blocco try-except?
Risposta corretta: Eseguire il codice di pulizia indipendentemente dal risultato del blocco try
Spiegazione/Esempio: Il blocco finally esegue il codice di pulizia, che viene eseguito sempre, indipendentemente dal fatto che si verifichi un'eccezione o meno. Ad esempio:
python
Copia codice
try:
    file = open('file.txt', 'r')
except IOError:
    print("Errore di I/O")
finally:
    file.close()
Risposte errate:
Terminare il programma: Non è lo scopo del finally.
Eseguire il codice solo in caso di eccezione: Non corretto.
Eseguire il codice solo se non ci sono eccezioni: Non corretto.
Quale eccezione viene sollevata quando un'operazione di I/O fallisce?
Risposta corretta: IOError
Spiegazione/Esempio: IOError viene sollevata in caso di errori di I/O, come file non trovati o errori di lettura/scrittura. Ad esempio:
python
Copia codice
try:
    with open('file.txt', 'r') as file:
        content = file.read()
except IOError:
    print("Errore di I/O!")
Risposte errate:
FileNotFoundError: È una sottoclasse di OSError usata in Python 3 per file non trovati.
ValueError: Non è relativa agli errori di I/O.
OSError: È una classe base per errori di sistema, ma IOError è più specifico per le operazioni di I/O.
Quale metodo viene eseguito prima di ogni test in una classe di test unittest?
Risposta corretta: setUp
Spiegazione/Esempio: Il metodo setUp viene eseguito prima di ogni test per preparare l'ambiente di test. Ad esempio:
python
Copia codice
import unittest

class TestExample(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3]
    
    def test_length(self):
        self.assertEqual(len(self.data), 3)
Risposte errate:
prepare: Non esiste.
initialize: Non esiste.
start: Non esiste.
Cosa succede se un'asserzione fallisce?
Risposta corretta: Viene sollevata un'AssertionError
Spiegazione/Esempio: Se un'asserzione fallisce, viene sollevata un'AssertionError, che segnala che il test non è passato. Ad esempio:
python
Copia codice
def test_addition(self):
    self.assertEqual(1 + 1, 3)  # Fallisce e solleva AssertionError
Risposte errate:
Viene sollevata un'SyntaxError: Non è corretto.
Non succede nulla: Non è corretto.
Il programma si chiude: Non è corretto.
Cosa rappresenta un programma I/O-bound?
Risposta corretta: Un programma che attende input/output
Spiegazione/Esempio: Un programma I/O-bound è limitato dalla velocità delle operazioni di input/output, come la lettura o la scrittura su disco o la comunicazione di rete.
Risposte errate:
Un programma che esegue calcoli pesanti: Non è corretto.
Un programma che non richiede attesa: Non è corretto.
Un programma che spinge la CPU al limite: Non è corretto.
Cosa rappresenta un thread in Python?
Risposta corretta: Un flusso separato di esecuzione
Spiegazione/Esempio: Un thread è un'unità di esecuzione separata all'interno di un processo, che può eseguire il codice in parallelo con altri thread dello stesso processo.
Risposte errate:
Un modulo: Non è corretto.
Un oggetto: Non è specifico.
Una funzione: Non è corretto.
Perché il GIL è considerato un problema?
Risposta corretta: Perché limita le prestazioni dei programmi multi-thread
Spiegazione/Esempio: Il Global Interpreter Lock (GIL) in Python impedisce l'esecuzione simultanea di più thread in un processo Python, limitando l'efficacia del multithreading per operazioni CPU-bound.
Risposte errate:
Perché impedisce l'uso dei thread: Non è corretto; i thread possono essere usati ma con limitazioni.
Perché aumenta la velocità dei programmi single-thread: Non è corretto; non influisce sulla velocità dei programmi single-thread.
Perché migliora le prestazioni dei programmi CPU-bound: Non è corretto; può peggiorare le prestazioni per programmi CPU-bound.
Cosa significa che un container è "standalone"?
Risposta corretta: Può essere eseguito indipendentemente su qualsiasi sistema che supporti il runtime dei container
Spiegazione/Esempio: Un container "standalone" significa che può essere eseguito su qualsiasi macchina che abbia un ambiente di runtime per container, senza dipendere da altri container o da un sistema operativo specifico.
Risposte errate:
Richiede un sistema operativo specifico: Non è corretto.
Dipende da un altro container: Non è corretto.
Richiede una VM per essere eseguito: Non è corretto.
Cos'è una macchina virtuale (VM)?
Risposta corretta: Un ambiente simulato creato tramite virtualizzazione
Spiegazione/Esempio: Una macchina virtuale è un ambiente virtuale che simula un computer fisico attraverso la virtualizzazione, permettendo di eseguire un sistema operativo separato su hardware condiviso.
Risposte errate:
Un sistema operativo: Non è corretto.
Un contenitore leggero: Non è corretto; questo è un container.
Un server fisico: Non è corretto.
Come si chiama il processo di avvolgere una funzione con un decoratore?
Risposta corretta: Decorazione
Spiegazione/Esempio: La decorazione è il processo di avvolgere una funzione con un decoratore, che modifica o estende il comportamento della funzione. Ad esempio:
python
Copia codice
def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
Risposte errate:
Incapsulamento: Non è il termine corretto.
Modifica: Non è il termine specifico.
Composizione: Non è il termine corretto.
Qual è la differenza tra una funzione con parentesi e una funzione senza parentesi passata come argomento?
Risposta corretta: La funzione con parentesi viene eseguita, mentre quella senza parentesi viene passata come referenza
Spiegazione/Esempio: Quando si passa una funzione con parentesi, si sta eseguendo la funzione e passando il suo risultato. Senza parentesi, si sta passando solo la referenza alla funzione. Ad esempio:
python
Copia codice
def greet():
    return "Hello"

def call_function(func):
    return func()  # Esegue func()

print(call_function(greet))  # Passa solo la referenza della funzione greet senza parentesi
Risposte errate:
La funzione con parentesi viene ignorata: Non corretto.
Non c'è differenza: Non corretto.
La funzione senza parentesi viene eseguita, mentre quella con parentesi viene passata come referenza: Non corretto.
Cosa fa l'istruzione else in un blocco try-except?
Risposta corretta: Esegue un blocco di codice solo in assenza di eccezioni
Spiegazione/Esempio: L'istruzione else viene eseguita solo se il blocco try non solleva eccezioni. Ad esempio:
python
Copia codice
try:
    print("Hello")
except ValueError:
    print("ValueError occurred")
else:
    print("No exception occurred")
Risposte errate:
Esegue un blocco di codice prima del blocco try: Non corretto.
Esegue un blocco di codice in caso di eccezione: Non corretto.
Esegue un blocco di codice dopo il blocco finally: Non corretto.
Quale convenzione devono seguire gli header dei metodi di test in unittest?
Risposta corretta: I nomi dei metodi devono iniziare con la parola test
Spiegazione/Esempio: In unittest, i nomi dei metodi di test devono iniziare con test_ per essere automaticamente riconosciuti come test case. Ad esempio:
python
Copia codice
import unittest

class MyTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
Risposte errate:
I nomi dei metodi devono iniziare con la parola validate: Non corretto.
I nomi dei metodi devono iniziare con la parola check: Non corretto.
I nomi dei metodi devono iniziare con la parola assert: Non corretto.
Quale metodo viene utilizzato per avviare un gruppo di thread con ThreadPoolExecutor?
Risposta corretta: map
Spiegazione/Esempio: Il metodo map di ThreadPoolExecutor può essere utilizzato per applicare una funzione a un insieme di argomenti in parallelo, gestendo i thread per l'utente. Ad esempio:
python
Copia codice
from concurrent.futures import ThreadPoolExecutor

def square(x):
    return x * x

with ThreadPoolExecutor() as executor:
    results = list(executor.map(square, [1, 2, 3, 4]))
Risposte errate:
.run(): Non esiste in questo contesto.
.execute(): Non è usato per avviare gruppi di thread.
.start(): Non è un metodo di ThreadPoolExecutor.
Quale comando esegue un singolo test case in unittest?
Risposta corretta: python -m unittest nome_file.TestNome
Spiegazione/Esempio: Per eseguire un singolo test case in un file di test, puoi usare questo comando. Ad esempio:
bash
Copia codice
python -m unittest test_module.MyTestCase
Risposte errate:
python -m unittest --v nome_file.TestNome: Non corretto; --v non è un'opzione valida.
python -m unittest -v nome_file.TestNome: Non corretto; -v è per la verbosità.
python -m unittest nome_file:TestNome: Non corretto; sintassi non valida.
Quale argomento posizionale aggiuntivo viene comunemente utilizzato con la funzione open() per specificare come si desidera aprire il file?
Risposta corretta: mode
Spiegazione/Esempio: L'argomento mode è utilizzato per specificare la modalità di apertura del file (lettura, scrittura, append, ecc.). Ad esempio:
python
Copia codice
with open('file.txt', mode='r') as file:
    content = file.read()
Risposte errate:
errors: Usato per la gestione degli errori di codifica.
buffering: Usato per specificare la dimensione del buffer.
encoding: Usato per specificare la codifica del file.
Quale carattere viene utilizzato per ottenere una nuova linea durante la scrittura su un file?
Risposta corretta: \n
Spiegazione/Esempio: Il carattere di nuova linea \n viene utilizzato per indicare una nuova linea in un file. Ad esempio:
python
Copia codice
with open('file.txt', 'w') as f:
    f.write("Prima linea\nSeconda linea")
Risposte errate:
\l: Non è un carattere di nuova linea.
\r: Carattere di ritorno a capo (carriage return), usato spesso in combinazione con \n su Windows.
\t: Carattere di tabulazione.
Qual è il principale vantaggio di utilizzare le funzioni come oggetti di prima classe?
Risposta corretta: Permette di passare, restituire e assegnare funzioni come variabili
Spiegazione/Esempio: In Python, le funzioni come oggetti di prima classe possono essere passate come argomenti a altre funzioni, restituite da funzioni, e assegnate a variabili. Ad esempio:
python
Copia codice
def outer():
    def inner():
        return "Hello"
    return inner

func = outer()  # func è ora una referenza alla funzione inner
print(func())  # Stampa: Hello
Risposte errate:
Rende il codice più leggibile: Non è il vantaggio principale.
Aumenta la velocità di esecuzione delle funzioni: Non è corretto.
Permette di creare più funzioni: Non è il vantaggio specifico.
Quale comando permette di visualizzare informazioni dettagliate sui test eseguiti con unittest?
Risposta corretta: python -m unittest -v
Spiegazione/Esempio: L'opzione -v (verbose) fornisce un output dettagliato sui test eseguiti. Ad esempio:
bash
Copia codice
python -m unittest -v test_module
Risposte errate:
python -m unittest -d: Non esiste.
python -m unittest --details: Non esiste.
python -m unittest --info: Non esiste.
Qual è la funzione di un decoratore in Python?
Risposta corretta: È una funzione che avvolge un'altra funzione, modificandone il comportamento
Spiegazione/Esempio: Un decoratore è una funzione che prende un'altra funzione e ne modifica o estende il comportamento senza cambiarne il codice. Ad esempio:
python
Copia codice
def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
Risposte errate:
È una funzione che ritorna un'altra funzione: Non descrive completamente il comportamento del decoratore.
È una funzione che viene eseguita prima di un'altra funzione: Non è sempre il caso; può essere eseguita prima e dopo.
È una funzione che accetta un'altra funzione come argomento: Non completa la definizione.
Cosa succede alla fine del blocco with quando si utilizza ThreadPoolExecutor?
Risposta corretta: Esegue un .join() su ciascuno dei thread nel pool
Spiegazione/Esempio: Quando il blocco with per ThreadPoolExecutor termina, il metodo __exit__ chiude il pool di thread e aspetta che tutti i thread terminino l'esecuzione. In pratica, __exit__ chiama shutdown() con wait=True per bloccare fino alla conclusione di tutti i thread.
Risposte errate:
Rilascia la memoria: Non è specifico per ThreadPoolExecutor.
Esegue un .start() su ciascuno dei thread nel pool: Non è corretto; i thread sono già avviati.
Incrementa il conteggio dei riferimenti: Non è corretto.
Qual è il metodo alternativo per ottenere l'esecuzione parallela in Python senza i limiti del GIL?
Risposta corretta: Utilizzare multiprocessing
Spiegazione/Esempio: Il modulo multiprocessing permette di eseguire operazioni in parallelo su più processori, evitando i limiti del GIL perché utilizza processi separati invece di thread. Ad esempio:
python
Copia codice
from multiprocessing import Process

def worker():
    print("Worker")

p = Process(target=worker)
p.start()
p.join()
Risposte errate:
Utilizzare solo un thread: Non è parallelo.
Evitare l'uso di thread: Non risolve il problema per operazioni CPU-bound.
Utilizzare il modulo os: Non è una soluzione diretta per il parallelismo.
Come si chiamano gli strumenti e i servizi necessari per costruire, eseguire e distribuire applicazioni containerizzate?
Risposta corretta: Container engine
Spiegazione/Esempio: Un container engine, come Docker, è responsabile della creazione, esecuzione e gestione dei container. Ad esempio:
bash
Copia codice
docker run hello-world
Risposte errate:
Hypervisor: Usato per la virtualizzazione, non per i container.
Dockerfile: È un file per definire l'immagine del container.
Virtual machine manager: Gestisce macchine virtuali, non container.
Qual è la funzione di ThreadPoolExecutor?
Risposta corretta: Gestire un pool di thread
Spiegazione/Esempio: ThreadPoolExecutor gestisce un gruppo di thread, permettendo l'esecuzione concorrente di operazioni. Ad esempio:
python
Copia codice
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n * n

with ThreadPoolExecutor() as executor:
    results = list(executor.map(task, range(10)))
Risposte errate:
Creare nuovi thread: Non crea thread direttamente; gestisce un pool.
Rilasciare la memoria: Non è il suo scopo principale.
Eseguire operazioni di I/O: Non è specifico per le operazioni di I/O.
Cosa fa il comando "WORKDIR /app" in un Dockerfile?
Risposta corretta: Cambia la directory di lavoro nel container a /app
Spiegazione/Esempio: WORKDIR imposta la directory di lavoro all'interno del container per le istruzioni successive nel Dockerfile. Ad esempio:
Dockerfile
Copia codice
WORKDIR /app
Risposte errate:
Installa le dipendenze nella directory /app: Non installa dipendenze.
Esegue il file /app: Non esegue file.
Copia i file nella directory /app: Non copia file.
Qual è l'effetto del GIL su un programma CPU-bound?
Risposta corretta: Limita le prestazioni a un singolo core della CPU
Spiegazione/Esempio: Il Global Interpreter Lock (GIL) in Python impedisce l'esecuzione simultanea di più thread Python nell'ambito di un singolo processo, limitando l'uso efficace di più core della CPU per programmi che richiedono intensivo utilizzo della CPU. Ad esempio, in un programma CPU-bound che utilizza più thread, il GIL potrebbe impedire ai thread di eseguire in parallelo su più core.
Risposte errate:
Permette l'esecuzione parallela su più core: Non è corretto, poiché il GIL limita questa possibilità.
Migliora le prestazioni: Non è corretto, il GIL può effettivamente ridurre le prestazioni.
Non ha effetto: Non è corretto, il GIL ha un effetto significativo.
Qual è la differenza tra un'asserzione e un'eccezione?
Risposta corretta: Un'asserzione verifica una condizione, un'eccezione gestisce errori
Spiegazione/Esempio: Le asserzioni sono usate per verificare che le condizioni siano vere e sollevano un'eccezione se la condizione non è vera. Le eccezioni sono usate per gestire errori che possono verificarsi durante l'esecuzione del programma. Ad esempio:
python
Copia codice
assert x > 0, "x deve essere positivo"
Risposte errate:
Un'eccezione verifica una condizione, un'asserzione gestisce errori: Inverso rispetto alla definizione corretta.
Non c'è differenza: Non è corretto.
Un'asserzione viene utilizzata solo per il debug: Non è del tutto corretto; può anche essere utilizzata per verifiche di condizione in generale.
Quale metodo di lettura legge tutte le linee di un file e le mette in una lista?
Risposta corretta: readlines()
Spiegazione/Esempio: readlines() legge tutte le linee di un file e le restituisce come una lista di stringhe. Ad esempio:
python
Copia codice
with open('file.txt', 'r') as f:
    lines = f.readlines()
Risposte errate:
readall(): Non esiste come metodo.
readline(): Legge solo una singola linea alla volta.
read(): Legge tutto il contenuto del file come una singola stringa.
Quale eccezione viene sollevata quando si tenta di dividere un numero per zero?
Risposta corretta: ZeroDivisionError
Spiegazione/Esempio: ZeroDivisionError viene sollevata quando si tenta di dividere per zero. Ad esempio:
python
Copia codice
result = 1 / 0  # Solleva ZeroDivisionError
Risposte errate:
DivisionByZero: Non è un'eccezione incorporata in Python.
ValueError: Usata per errori di tipo di valore, non divisione per zero.
ArithmeticError: Classe base per errori aritmetici, ma la specifica è ZeroDivisionError.
Qual è la classe base utilizzata per creare test case in unittest?
Risposta corretta: TestCase
Spiegazione/Esempio: TestCase è la classe base da cui devono derivare le classi di test in unittest. Ad esempio:
python
Copia codice
import unittest

class MyTestCase(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)
Risposte errate:
TestClass: Non esiste in unittest.
UnitTest: Non è una classe base, ma il modulo.
TestSuite: È un contenitore per test case, non una classe base.
Qual è lo scopo del blocco try in Python?
Risposta corretta: Tentare di eseguire il codice che potrebbe generare un'eccezione
Spiegazione/Esempio: Il blocco try è usato per eseguire codice che potrebbe sollevare un'eccezione, permettendo di gestire l'eccezione nel blocco except. Ad esempio:
python
Copia codice
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Divisione per zero!")
Risposte errate:
Pulire dopo l'esecuzione del codice: Non è lo scopo principale del try.
Gestire le eccezioni: È gestito dal blocco except, non solo dal try.
Verificare una condizione: Non è lo scopo del try.
Quale metodo viene utilizzato per verificare l'uguaglianza in unittest?
Risposta corretta: assertEqual
Spiegazione/Esempio: assertEqual verifica che due valori siano uguali in un test. Ad esempio:
python
Copia codice
self.assertEqual(2 + 2, 4)
Risposte errate:
assertSimilar: Non esiste come metodo.
assertEquals: Metodo non esistente, il corretto è assertEqual.
assertSame: Non esiste, e non è il nome corretto per l'uguaglianza.
Cosa fa l'istruzione "COPY . /app" in un Dockerfile?
Risposta corretta: Copia i contenuti della directory corrente nella directory /app all'interno del container
Spiegazione/Esempio: Il comando COPY copia i file e le directory dal contesto di build alla directory del container specificata. Ad esempio:
Dockerfile
Copia codice
COPY . /app
Risposte errate:
Crea un nuovo container: Non è corretto.
Installa le dipendenze: Non è specifico per COPY.
Esegue l'applicazione: Non esegue file.
Che cosa significa GIL in Python?
Risposta corretta: Global Interpreter Lock
Spiegazione/Esempio: Il Global Interpreter Lock (GIL) è un meccanismo in CPython che garantisce che solo un thread alla volta possa eseguire il bytecode Python. Questo può limitare la concorrenza in programmi multi-threaded. Ad esempio:
python
Copia codice
import threading

def worker():
    pass

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)
t1.start()
t2.start()
t1.join()
t2.join()
Risposte errate:
General Interpreter Lock: Non è il termine corretto.
Global Interpreted Language: Non è corretto.
General Instruction List: Non è un termine relativo al GIL.
  Qual è la complessità temporale della ricerca binaria?
Risposta corretta: O(log n)
Spiegazione/Esempio: La ricerca binaria divide l'array in due metà ad ogni passo, riducendo quindi il problema a una dimensione metà ogni volta, con una complessità logaritmica. Ad esempio, per trovare un elemento in un array ordinato di 1.000.000 elementi, al massimo saranno necessari circa 20 confronti.
Risposte errate:
O(1): La ricerca binaria non è costante.
O(n^2): Troppo elevata per la ricerca binaria.
O(n): Troppo alta per la ricerca binaria.
  Qual è la complessità temporale di un algoritmo che esplora una matrice quadrata?
Risposta corretta: O(n^2)
Spiegazione/Esempio: Esplorare una matrice quadrata significa visitare ogni cella della matrice, e poiché una matrice quadrata di dimensione n×nn \times nn×n ha n2n^2n2 celle, la complessità è O(n^2). Ad esempio, visitare ogni cella di una matrice 100x100 richiede 10.000 operazioni.
Risposte errate:
O(n log n): Non rappresenta il tempo di esplorazione di una matrice.
O(1): Non rappresenta la complessità per l'esplorazione di una matrice.
O(log n): Non è corretta per esplorare una matrice quadrata.
  Qual è la complessità temporale dell'algoritmo ricorsivo per calcolare il numero di Fibonacci?
Risposta corretta: O(2^n)
Spiegazione/Esempio: L'algoritmo ricorsivo per calcolare Fibonacci ha una crescita esponenziale poiché calcola i valori di Fibonacci in modo ridondante. Ad esempio, per calcolare fib(5), l'algoritmo esegue molteplici chiamate ricorsive ridondanti, portando a una complessità O(2^n).
Risposte errate:
O(log n): Non è corretto per la versione ricorsiva non ottimizzata.
O(n^2): Non rappresenta la complessità della versione ricorsiva.
O(n): Non è corretto per la versione ricorsiva non ottimizzata.
  Qual è la complessità temporale di Bubble Sort nel caso peggiore?
Risposta corretta: O(n^2)
Spiegazione/Esempio: Bubble Sort ha una complessità temporale quadratica nel caso peggiore perché richiede confronti e scambi ripetuti. Ad esempio, ordinare un array di 1.000 elementi potrebbe richiedere fino a 1.000.000 di confronti e scambi.
Risposte errate:
O(n log n): Non rappresenta il Bubble Sort.
O(log n): Non è corretto per Bubble Sort.
O(n): Non è corretto per il caso peggiore di Bubble Sort.
  Qual è la complessità temporale di un algoritmo che ha una crescita quadratica con la dimensione dell'input?
Risposta corretta: O(n^2)
Spiegazione/Esempio: Un algoritmo con crescita quadratica ha un tempo di esecuzione che aumenta con il quadrato della dimensione dell'input. Ad esempio, se l'input raddoppia, il tempo di esecuzione aumenta di circa quattro volte.
Risposte errate:
O(log n): Non rappresenta la crescita quadratica.
O(n): Non rappresenta la crescita quadratica.
O(n log n): Non rappresenta la crescita quadratica.
  Qual è il primo passo dell'algoritmo Merge Sort?
Risposta corretta: Dividere il problema in sotto-problemi più piccoli
Spiegazione/Esempio: Merge Sort utilizza il paradigma Divide et Impera per dividere l'array in due metà, ordinare ciascuna metà ricorsivamente e poi unirle. Ad esempio, un array di 10 elementi viene diviso in due array di 5 elementi.
Risposte errate:
Confrontare elementi adiacenti: Non è il primo passo di Merge Sort.
Ordinare un array di dimensioni uno: Non è il primo passo, ma il risultato finale.
Unire le soluzioni dei sotto-problemi: È l'ultimo passo di Merge Sort.
  Qual è la complessità temporale di Bubble Sort?
Risposta corretta: O(n^2)
Spiegazione/Esempio: Bubble Sort ha una complessità temporale quadratica sia nel caso migliore che nel caso peggiore, poiché richiede due cicli annidati per confrontare e scambiare gli elementi.
Risposte errate:
O(log n): Non rappresenta Bubble Sort.
O(n log n): Non rappresenta Bubble Sort.
O(n): Non è corretto per Bubble Sort.
  Che cos'è la sequenza di Fibonacci?
Risposta corretta: Una sequenza di numeri interi in cui ciascun numero è la somma dei due precedenti
Spiegazione/Esempio: La sequenza di Fibonacci inizia con 0 e 1 e ogni numero successivo è la somma dei due numeri precedenti. Ad esempio, 0, 1, 1, 2, 3, 5, 8, ...
Risposte errate:
Una sequenza di numeri primi: Non è corretto.
Una sequenza di numeri pari: Non è corretto.
Una sequenza di numeri dispari: Non è corretto.
  Qual è il paradigma su cui si basa l'algoritmo Merge Sort?
Risposta corretta: Divide et impera
Spiegazione/Esempio: Merge Sort utilizza il paradigma Divide et Impera per dividere un problema in sotto-problemi più piccoli, risolverli e combinare le soluzioni. Ad esempio, un array viene diviso in due metà, ordinate e poi unite.
Risposte errate:
Programmazione dinamica: Non è il paradigma usato da Merge Sort.
Backtracking: Non è il paradigma usato da Merge Sort.
  Qual è la caratteristica principale degli algoritmi con complessità O(1)?
Risposta corretta: Il tempo di esecuzione è costante e non dipende dalla dimensione dell'input
Spiegazione/Esempio: Gli algoritmi con complessità O(1) eseguono un'operazione in tempo costante, indipendentemente dalla dimensione dell'input. Ad esempio, accedere a un elemento in un array usando l'indice.
Risposte errate:
Il tempo di esecuzione cresce linearmente con la dimensione dell'input: Non è corretto.
Il tempo di esecuzione cresce esponenzialmente con la dimensione dell'input: Non è corretto.
Il tempo di esecuzione dipende dal quadrato della dimensione dell'input: Non è corretto.
  Qual è la complessità temporale di un algoritmo che ha una crescita fattoriale con la dimensione dell'input?
Risposta corretta: O(n!)
Spiegazione/Esempio: La crescita fattoriale significa che il tempo di esecuzione aumenta esponenzialmente con la dimensione dell'input. Ad esempio, il numero di permutazioni di una sequenza di n elementi è n!.
Risposte errate:
O(n): Non rappresenta la crescita fattoriale.
O(n^2): Non rappresenta la crescita fattoriale.
O(log n): Non rappresenta la crescita fattoriale.
  Qual è la complessità temporale di Merge Sort?
Risposta corretta: O(n log n)
Spiegazione/Esempio: Merge Sort ha una complessità temporale di O(n log n) sia nel caso migliore che nel caso peggiore, poiché divide l'array in metà e unisce i risultati ordinati. Ad esempio, ordinare un array di 1.000 elementi richiede circa 10.000 operazioni.
Risposte errate:
O(n): Non rappresenta la complessità di Merge Sort.
O(n^2): Non rappresenta la complessità di Merge Sort.
O(log n): Non rappresenta la complessità di Merge Sort.
  Qual è un vantaggio dell'algoritmo Merge Sort rispetto a Bubble Sort?
Risposta corretta: Ha una complessità temporale migliore
Spiegazione/Esempio: Merge Sort ha una complessità temporale di O(n log n), mentre Bubble Sort ha una complessità di O(n^2), rendendo Merge Sort più efficiente per array di grandi dimensioni.
Risposte errate:
Utilizza meno memoria: Non è necessariamente vero; Merge Sort può utilizzare più memoria.
Richiede meno confronti: Non è sempre vero.
È più facile da implementare: Bubble Sort è generalmente più semplice da implementare.
  Qual è un esempio di algoritmo con complessità O(n log n)?
Risposta corretta: Merge Sort
Spiegazione/Esempio: Merge Sort è un algoritmo di ordinamento con complessità O(n log n). Ad esempio, ordinare un array di 1.000 elementi richiede circa 10.000 operazioni.
Risposte errate:
Bubble Sort: Ha una complessità O(n^2).
Ricerca lineare: Ha una complessità O(n).
Ricerca binaria: Ha una complessità O(log n).
  Qual è un esempio di algoritmo con complessità O(log n)?
Risposta corretta: Ricerca binaria
Spiegazione/Esempio: La ricerca binaria ha una complessità O(log n) perché riduce il problema a metà ad ogni passo. Ad esempio, per cercare un elemento in un array ordinato di 1.000.000 elementi, la ricerca binaria richiede al massimo 20 confronti.
Risposte errate:
Bubble sort: Ha una complessità O(n^2).
Ricerca lineare: Ha una complessità O(n).
Fibonacci: La versione ricorsiva ha una complessità O(2^n).
  Qual è la complessità temporale di un algoritmo che esegue un'operazione indipendentemente dalla dimensione dell'input?
Risposta corretta: O(1)
Spiegazione/Esempio: Gli algoritmi con complessità O(1) eseguono un'operazione in tempo costante, indipendentemente dalla dimensione dell'input. Ad esempio, l'accesso a un elemento in un array tramite un indice è un'operazione O(1).
Risposte errate:
O(n): Non rappresenta una complessità costante.
O(n^2): Non rappresenta una complessità costante.
O(log n): Non rappresenta una complessità costante.
  Qual è la complessità temporale della soluzione iterativa per calcolare i numeri di Fibonacci?
Risposta corretta: O(n)
Spiegazione/Esempio: La soluzione iterativa per calcolare i numeri di Fibonacci ha una complessità O(n) poiché itera attraverso i numeri fino a n per calcolare il valore richiesto. Ad esempio, calcolare fib(10) richiede 10 iterazioni.
Risposte errate:
O(1): Non rappresenta la soluzione iterativa.
O(n^2): Non rappresenta la soluzione iterativa.
O(n log n): Non rappresenta la soluzione iterativa.

"""