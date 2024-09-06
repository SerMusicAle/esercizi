import os
from file_handlers import CercaStringaInFilename, CercaStringaInFileContent, CercaInFilePdf, CercaInFileDoc
from utilities import SalvaFile, in_directory
import datetime

def cerca_stringa_in_file_system(sRoot, sStringaDaCercare, sOutDir):
    iNumFileTrovati = 0
    iNumFileTotali = 0
    
    now = datetime.datetime.now()
    dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")
    sOutSubDir = os.path.join(sOutDir, dt_string)
    os.makedirs(sOutSubDir, exist_ok=True)

    for root, dirs, files in os.walk(sRoot):
        # Evitare la directory di output per prevenire cicli infiniti
        if in_directory(root, sOutDir):
            continue

        for filename in files:
            iNumFileTotali += 1
            pathCompleto = os.path.join(root, filename)

            # Cerca la stringa nel nome del file
            iRet = CercaStringaInFilename(filename, sStringaDaCercare)
            if iRet:
                print(f"Trovato file: {filename}")
                SalvaFile(pathCompleto, filename, sOutSubDir)
                iNumFileTrovati += 1
                continue

            # Cerca la stringa nel contenuto del file (binario, PDF, DOC, ecc.)
            iRet = CercaStringaInFileContent(pathCompleto, sStringaDaCercare)
            if iRet:
                print(f"Trovato file: {filename}")
                SalvaFile(pathCompleto, filename, sOutSubDir)
                iNumFileTrovati += 1
            else:
                _, ext = os.path.splitext(filename)
                if ext.lower() == ".pdf":
                    iRet = CercaInFilePdf(pathCompleto, sStringaDaCercare)
                elif ext.lower() in [".doc", ".docx"]:
                    iRet = CercaInFileDoc(pathCompleto, sStringaDaCercare)

                if iRet:
                    print(f"Trovato file: {filename}")
                    SalvaFile(pathCompleto, filename, sOutSubDir)
                    iNumFileTrovati += 1

    print(f"Trovati {iNumFileTrovati} file su {iNumFileTotali} totali.")
