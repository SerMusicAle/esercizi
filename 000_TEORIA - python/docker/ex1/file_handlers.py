import mmap
import PyPDF2
import textract

def CercaStringaInFilename(sFilename, sStringToSearch):
    sFilename1 = sFilename.lower()
    sStringToSearch1 = sStringToSearch.lower()
    return sStringToSearch1 in sFilename1

def CercaStringaInFileContent(sFile, sString):
    sString = sString.lower()
    try:
        with open(sFile, "r+b") as f:
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            while True:
                line = s.readline().lower()
                if not line:
                    break
                if sString.encode() in line:
                    return True
    except:
        return False
    return False

def CercaInFilePdf(sFile, sString):
    try:
        reader = PyPDF2.PdfFileReader(sFile)
        num_pages = reader.getNumPages()
        for page in range(num_pages):
            text = reader.getPage(page).extractText().lower()
            if sString in text:
                return True
    except:
        return False
    return False

def CercaInFileDoc(sFile, sString):
    try:
        text = textract.process(sFile).decode("utf-8").lower()
        return sString in text
    except:
        return False
