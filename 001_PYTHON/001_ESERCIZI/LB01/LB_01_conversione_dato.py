#conversione liste
import ast

class Liste:

    def __init__(self, mydict_1:dict[str:str|bool|], mydict_2:str):
        self.mydict_1 = mydict_1
        self.mydict_2 = mydict_2
        self.mydict_3: str = "" 
        self.mydict_4: list[str] = []
        
    def DeserializeJson(self, file_path): --> dict
        self.mydict_3 = str(self.mydict_1)

    def SerializeJson(self, dData, file_path): --> True/False
        self.mydict_4 = ast.literal_eval(self.mydict_2)


mydict_1 = { "brand": "Ford", "electric": False, "year": 1964, "colors": ["red", "white", "blue"]}

mydict_2 = "{ 'brand':   'Ford'," + \
"'electric': False," + \
"'year': 1964," + \
"'colors': ['red', 'white', 'blue']}"

 
mydict_1.DeserializeJson()
mydict_2.SerializeJson()

json.dump()

print("Ser:", lista1.lista3)
print("conversione2:", lista2.lista4)


str1 = json.dumps(mydict_1)

json.load
dict_1 = json.loads(mydict_2)

