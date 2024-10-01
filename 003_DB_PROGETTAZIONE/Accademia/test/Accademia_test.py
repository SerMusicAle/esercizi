import sqlite3

def execute_sql_script(connection, script_file):
    with open(script_file, 'r') as file:
        sql_script = file.read()
    
    try:
        cursor = connection.cursor()
        cursor.executescript(sql_script)
        connection.commit()
        print("Script SQL eseguito con successo.")
    except sqlite3.Error as e:
        print(f"Errore durante l'esecuzione dello script: {e}")

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def main():
    # Connessione al database SQLite
    conn = sqlite3.connect('accademia.db')

    # Esegui il file SQL
    execute_sql_script(conn, 'Accademia4.sql')

    while True:
        query = input("Inserisci la tua query SQL (o 'exit' per uscire): ")
        if query.lower() == 'exit':
            break
        try:
            results = execute_query(conn, query)
            print("Risultati della query:")
            for row in results:
                print(row)
        except sqlite3.Error as e:
            print(f"Errore nell'esecuzione della query: {e}")

    # Chiudi la connessione
    conn.close()

if __name__ == "__main__":
    main()
