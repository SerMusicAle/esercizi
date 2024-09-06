import os
import shutil

def SalvaFile(sFilePath, sFileName, sOutDir):
    # Creiamo un percorso univoco per evitare sovrascritture
    sFilePathNew = sFilePath.replace("_", "__").replace("\\", "_").replace("/", "_")
    sOutFile = os.path.join(sOutDir, sFilePathNew)
    print(f"Devo copiare {sFilePath} in {sOutFile}")
    shutil.copyfile(sFilePath, sOutFile)

def verifica_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def in_directory(dir1, dir2):
    dir1_abs = os.path.abspath(dir1).lower()
    dir2_abs = os.path.abspath(dir2).lower()
    return dir2_abs in dir1_abs
