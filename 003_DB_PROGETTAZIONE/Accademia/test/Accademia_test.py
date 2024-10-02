import psycopg2

def execute_queries():
    # Configura la connessione al database
    conn = psycopg2.connect(
        dbname='tuo_db',  # Sostituisci con il nome del tuo database
        user='tuo_user',  # Sostituisci con il tuo username
        password='tuo_password',  # Sostituisci con la tua password
        host='localhost',  # Modifica se necessario
        port='5432'  # Modifica se necessario
    )
    
    try:
        with conn.cursor() as cursor:
            # 1. Cognomi distinti di tutti gli strutturati
            query1 = """
            SELECT DISTINCT cognome 
            FROM accademia.persona;
            WHERE TRUE
            """
            cursor.execute(query1)
            results1 = cursor.fetchall()
            print("Cognomi distinti di tutti gli strutturati:")
            for row in results1:
                print(row)

            # 2. Nome e cognome dei ricercatori
            query2 = """
            SELECT id, nome, cognome 
            FROM accademia.persona 
            WHERE posizione = 'Ricercatore';
            """
            cursor.execute(query2)
            results2 = cursor.fetchall()
            print("\nNome e cognome dei ricercatori:")
            for row in results2:
                print(row)

    except Exception as e:
        print(f"Errore: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    execute_queries()
