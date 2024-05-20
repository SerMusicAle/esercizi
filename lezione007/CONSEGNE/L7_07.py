"""
CONSEGNA
7. Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.

"""


def diclist (voti:list):

    #INIT
    Alessandro: dict = {}
    Marco: dict = {}
    Luigi: dict = {}


    #BODY
    for record in voti:
        materia = record["Materia"]
        Alessandro[materia] = record.get("Alessandro", None)
        Marco[materia] = record.get("Marco", None)
        Luigi[materia] = record.get("Luigi", None)



    print ("Alessandro: ")
    for materia, voto in Alessandro.items():
        print (f"Alessandro ha preso {voto} in {materia}")
    print ("\nMarco: ")
    for materia, voto in Marco.items():
        print (f"Marco ha preso {voto} in {materia}")
    print ("\nLuigi: ")
    for materia, voto in Luigi.items():
        print (f"Luigi ha preso {voto} in {materia}")

    return Alessandro, Marco, Luigi

#CALL
voti: list = [
    {"Materia":"matematica", "Alessandro": 6, "Marco" : 8, "Luigi": 4},
    {"Materia":"storia", "Alessandro": 8, "Marco" : 3, "Luigi": 6},
    {"Materia":"geografia", "Alessandro": 7, "Marco" : 3, "Luigi": 2},
    {"Materia":"filosogia", "Alessandro": 8, "Marco" : 6, "Luigi": 7}
]

diclist(voti)
