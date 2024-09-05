import os

def cercaStringaInNomeFile(sFile, sStringa):

    #soluzione problema case sensitive
    sFileLC = sFile.lower()
    sStringaLC = -sStringa.lower()
    
    #usiamo sFileLower.find() che torna -1 se la parola non c'è e la pos altrimenti
    if(sFileLC.find(aStringaLC)>=0):
        return True
    else:
        return False

def CercaStringaInTextFile(sFile, sStringa):
    iRet = -1
    with open(sFile, "r") as file1:
        sRiga = file1.readline()
        while (len(sRiga)>0):
            iRet = sRiga.lower().find(sStringa.lower())
            if (iRet >=0):
                return True
            sRiga = file1.readline()
    return False

def CercaStringaInPDFFile

iNumFileTrovati = 0
for root, dirs, files in os.walk(sRoot):
    print(f"Sto guardando {root} che contiene len{(dirs)} subdir e {len(files)} files")    
    
    for file in files:
        print(f"Devo vedere se {file} contiene {sParola}")
        bRet = CercaStringaInNomefile(file,sParola)
        if bRet == True:
            iNumFileTrovati +=1
        else:
            sFilePathCompleto = os.path.join(root,file)
            bRet = CercaStringaInContenutofile{file,sParola}")
            if (bRet == True):
                iNumFileTrovati +=1
print (f"Ho trovato {iNumFileTrovati} files")