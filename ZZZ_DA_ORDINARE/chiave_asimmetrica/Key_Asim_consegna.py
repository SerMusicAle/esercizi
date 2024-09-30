#chiave_asimmetrica/Key_Asim_consegna -------------------------------------------------------------------------------------


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Funzione per generare una coppia di chiavi RSA (pubblica e privata)
def generate_key_pair():
    key_pair = RSA.generate(2048)  # Genera una coppia di chiavi RSA di 2048 bit
    private_key = key_pair.export_key()  # Esporta la chiave privata in formato PEM
    public_key = key_pair.publickey().export_key()  # Esporta la chiave pubblica in formato PEM
    
    return private_key, public_key

# Funzione per cifrare il messaggio
def encrypt_message(message, public_key_pem):
    public_key = RSA.import_key(public_key_pem)  # Importa la chiave pubblica
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode('utf-8'))
    return base64.b64encode(encrypted_message).decode('utf-8')

# Funzione per decifrare il messaggio
def decrypt_message(encrypted_message_base64, private_key_pem):
    private_key = RSA.import_key(private_key_pem)  # Importa la chiave privata
    encrypted_message = base64.b64decode(encrypted_message_base64)
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(encrypted_message).decode('utf-8')

# Simulazione della comunicazione tra Alessandro e Francisco
def main():
    # Genera la coppia di chiavi per Alessandro
    print("Generazione della coppia di chiavi di Alessandro...")
    alessandro_private_key, alessandro_public_key = generate_key_pair()
    
    # Genera la coppia di chiavi per Francisco
    print("\nGenerazione della coppia di chiavi di Francisco...")
    francisco_private_key, francisco_public_key = generate_key_pair()

    # Alessandro invia una domanda a Francisco
    message_from_alessandro = "È meglio la Roma o la Lazio?"
    print("\nMessaggio di Alessandro in chiaro:")
    print(message_from_alessandro)
    
    # Alessandro cifra il messaggio con la chiave pubblica di Francisco
    encrypted_message = encrypt_message(message_from_alessandro, francisco_public_key)
    print("\nMessaggio cifrato da Alessandro con la chiave pubblica di Francisco:")
    print(encrypted_message)
    
    # Francisco riceve il messaggio e lo decifra con la sua chiave privata
    decrypted_message = decrypt_message(encrypted_message, francisco_private_key)
    print("\nMessaggio decifrato da Francisco con la sua chiave privata:")
    print(decrypted_message)

    # Francisco risponde ad Alessandro
    response_from_francisco = "La Grande Roma"
    print("\nRisposta di Francisco in chiaro:")
    print(response_from_francisco)
    
    # Francisco cifra la risposta con la chiave pubblica di Alessandro
    encrypted_response = encrypt_message(response_from_francisco, alessandro_public_key)
    print("\nRisposta cifrata di Francisco con la chiave pubblica di Alessandro:")
    print(encrypted_response)
    
    # Alessandro riceve la risposta e la decifra con la sua chiave privata
    decrypted_response = decrypt_message(encrypted_response, alessandro_private_key)
    print("\nRisposta decifrata da Alessandro con la sua chiave privata:")
    print(decrypted_response)

# Avvio del programma
if __name__ == "__main__":
    main()
