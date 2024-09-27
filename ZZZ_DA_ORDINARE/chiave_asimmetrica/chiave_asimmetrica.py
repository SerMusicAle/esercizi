
# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# pypcryptodome oppure python3 -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# # Per iniziare generiamo una coppia di chiavi e le stampiamo
# # Generating RSA Key Pair
# # Una volta stampate, non serve più
#-------------------------------------------------------------------- #TROVA CHIAVI PUBBLICHE E PRIVATE A 2048 bit sia privata che pubblica.

# #chiave privata
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())

# #chiave pubblica
# public_key = key_pair.publickey()
# print(public_key.export_key())

# exit(0)
# FINE-------------------------------------------------------------------- #TROVA CHIAVI PUBBLICHE E PRIVATE A 2048 bit sia privata che pubblica.

#CHIAVI PRIVATE E PUBBLICHE
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEA1OOZigoOuxZh5eNLhfmgSXftsct3wy9z7Uxk2t7tU4XCIVQ8\nqxOYddOk5Blv/OvAIxKJjJTP9vB7KKDpefLwrfP1I2vfTJIjSltX13T0LiwFviCZ\nXmoOvmkSz9Fv89v0o8pSfavXyNpI3BShOy25l4Q+kOcuE8vL7LKuP8GnWlPFtfap\ncbFJfEe+Rda8htuA1b7c4Bpd+Pw42tZw/FWKw3lv6BSEuf82bzk7MK0J43nyJW4P\nXsruur0diP+/iPiMFwQJGkzGFD6dbYOFoRcYzjIBuhDc/YVxL/JRvkwubRZEqePb\nsoL/03ovFTknT1ymu0LwsAwbp7P2H2Lfp9Jf/wIDAQABAoIBAAMk+XeYfm80/W0v\n1kW8UinDo7ckkjhH0yaGIlc5Q7ggGaX0YJEGURIsdhsIZScPNF9QPsfcytWS577J\n4ajzdaqcF9rWFQ5EelD22G1ORO0JqWwNfzZtypn1Y1m+djDb5tkke+NvTlihIMJf\na6I8IqmiQmpRf9S7BeARI5G9goNLApK3ELzNRjYZToM8MiTdYn/9Tp+1MrZEdCZr\nYdiXiUHRX5LJhPcAH+tdQbMK2B81ERVkB+tEQ4FR9NRIelBOaXa0ot5hJ8mO7fwn\navD/7xlCGDyWZzyyhPW+ADLJB3X9gQJzYscTIxqZmQRhlIGY3nAd4+TBFlzGJZcW\nfjxsuQECgYEA5JWUWqcRlxRLRYACfKfoxk6mFkOmij7felWO6/JNG18jRizs9isQ\n3W9nRtVLbd24MQ7UNm4V37Quj+NXkzS+yUD0TQgJDQ6S67GBoqe9NhWZv3h6PKxO\npD7hHzF/AOMq0ruCa+ZdESvDROEqGmWocKBKqp0vrVHZyyj7KipjrHECgYEA7mwd\nsTTvS/XdoeK7jd8SodVtxUjt5doRhsCkilXVK1TUvLrdkqb5Njmw4TyPUW4rdmOH\nhH94BzOobmCNCkU5SwDgxdoxKo1qOnCHakTBh246xcc8wVk2XL2B39RpJVXUb9PU\naupRySvCpwkO0NU9uQSrDEAW2K+iiMjlPj0ty28CgYAshcoAojv13lkO73EMkLPx\nNE57Va/xi2+B53pQEMDeDPjU6Vk6VYcSammGTXNEsgP3YjkJZQXTrcfH9PMQ1Bw5\nHPK4slD4/xa0270xTlS3XRu2RKQifzlOGoVEyyI+rQChTS6JD7Se7JQ7LVRDEfvt\n+/qvIrCvpJq0TIYnX1xMsQKBgCTGvonADY1c/nPjImUO3LPj1QvSZQfIbF2px3ej\nJ7+IVUxLUrQ1V0ma+oKzsbOw17lqPtQcSWpq+HcWI4tLBDxihUlfj6ftqk4bX3fv\n5R47zYsGYYO9fBowDSF2hUWCCMO7HA/l1vm960eSqRtjWSL56lx4Yk3IQbzxqBLC\noxa3AoGAUe/OL4BZLTvtq+xtnKgX7NBgGwGgHQ/xAzNiMV5l50mCXFCa79g6XNK/\nNFl3Iv/vrMzENaY53DR/CXbkfgLprDFXc7KYEMUTJmp19iqVOPkXpOu6iD7gTtJW\nB7LsnpnDAUvQNFFcxMD8QhklyCsHq08KbUqruQEOAeZt6KPDNwc=\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1OOZigoOuxZh5eNLhfmg\nSXftsct3wy9z7Uxk2t7tU4XCIVQ8qxOYddOk5Blv/OvAIxKJjJTP9vB7KKDpefLw\nrfP1I2vfTJIjSltX13T0LiwFviCZXmoOvmkSz9Fv89v0o8pSfavXyNpI3BShOy25\nl4Q+kOcuE8vL7LKuP8GnWlPFtfapcbFJfEe+Rda8htuA1b7c4Bpd+Pw42tZw/FWK\nw3lv6BSEuf82bzk7MK0J43nyJW4PXsruur0diP+/iPiMFwQJGkzGFD6dbYOFoRcY\nzjIBuhDc/YVxL/JRvkwubRZEqePbsoL/03ovFTknT1ymu0LwsAwbp7P2H2Lfp9Jf\n/wIDAQAB\n-----END PUBLIC KEY-----"
sFrancisco_domanda = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1860g4EdDj175BImYOe1\nZPLhBr5KfNbvW6xyJQGfGaOHB6hkmEpIWXquibfZ9PGyr9gDe/9xAeqD1A93RceK\nUL7poHBOLjtRypgysokeJkRnYAsbWa2pTQ9GaxGxHQClZ3RDnvA32J8J5e9224Vk\nL/bZKn7ohd0qnXBxVg67lUMUvP9wOVOyp4pq8vHMUaKO118ANrPDW4V+x6AKKY/J\nBCw0L+BRb6T52hUmCGzA6OVYUiCrbqi7h6z7i+Drc0Peg1csU2s2LChNeb/3qFyd\nDsaH36fzWT2lMHdyIbdKLUuAZQvYcj5Q8FnMLsz+8D8UUxA42DDqlBpWWiUmls/L\ndQIDAQAB\n-----END PUBLIC KEY-----"
sFrancisco_risposta ="LmR0cuMbAmXZ5jLU8Uv1WFXAs1Aj929JfNFC9FHLzGLgrh3HgVf8aUCsCukNByr2gcTxPCoWX8+aXINhbOtk07yF9CoI+5aEOfALx12COmEpt5N1Mel6GpOvNIkysKRllAfolu/GrtTX1jam8ZHZOrmLyvfncNt1qr5y0fYZJkxUITsXm3NYfD7+29BloPZMOJ+4iz+m1vA1EWecSrdXV/a+iHRYIYr5qesqXRikse0nssNpyWAFKJfrM5JuG3ufIo62rc8iFYs83Cc0/J0BCtmrr21PPVGubcHzL7ypLVWFA2BbPPkrlotDOaknebu/eLaS+y7Gc70SrCdMwSKGJA=="

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)

# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# # Example usage
# message = "è meglio goku o vegeta?"
# encrypted_message = encrypt_message(message, public_key)
# decrypted_message = decrypt_message(encrypted_message, key_pair)

# print("Original Message:", message)
# print("Encrypted Message:", encrypted_message)
# print("Decrypted Message:", decrypted_message)

# Example invio domanda
#message = "è meglio goku o vegeta?"
#encrypted_message = encrypt_message(message, publicKeyF)

#print("Encrypted Message:", encrypted_message)

# Example ricezione risposta
decrypted_message = decrypt_message(sFrancisco_risposta, key_pair)

print("Decrypted Message:", decrypted_message)
