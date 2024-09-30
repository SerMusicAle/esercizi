import sys
import json

def SerializaJson1(dData,file_path):
    sData = json.dumps(dData)
    try:        
        with open(file_path, "w") as myfile:
            myfile.write(sData)    
        return True
    except:
        return False

def SerializaJson2(dData, file_path):
    try:
        with open (file_path, "w") as myfile:
            json.dump(Data,myfile)
        return True
    except:
        return False
    
mydict_1 = { "brand": "Ford", "electric": False, "year": 1964, "colors": ["red", "white", "blue"]}

mydict_2 = "{ 'brand':   'Ford'," + \
"'electric': False," + \
"'year': 1964," + \
"'colors': ['red', 'white', 'blue']}"    

bRet = SerializaJson1(mydict_1,"./prodotto.json")
bRet = SerializaJson2(mydict_1,"./prodotto.json")
print (bRet)
sys.exit()    
    
#da stringa a lista    
def DeserializeJson1(sFile_Path):
    sData:str = ""
    sAppo:str = ""
    dData:dict = []
    try:
        with open(sFile_Path, "r") as myfile:
            sAppo = myfile.read(500)
            while len(sAppo) == 500:
                sData += sAppo
                sAppo = myfile.read(500)
            if len(sAppo) > 0:
                sData += sAppo
        if len(sData)>0:
            dData = json.loads(sData)
            return sData
        else: 
            return None
    except:
        return None
