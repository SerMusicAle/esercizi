""""
    edifici
    stanze
    programmi di studio
    studenti
    esami
    slides
    esercizi
"""


    
class Room:
    def __init__(self, id:str, floor: int, seats: int):
                 self.id = id
                 self.floor = floor
                 self.seats = seats
    
    def get_floor(self) -> int:
        return self.floor

    def get_seats(self) -> int:
        return self.seats
    
    def get_id(self) -> int:
        return self.id
    
    def __str__ (self) -> self:
        return f"Rooms(id={self.id}, floor {self.floor}, seats = {self.seats})"
    

class Building:
    def __init__ (self, name:str, address:str, rooms: list = [], num_floors:int):
        self.name = name
        self.address = address
        self.num_floors = num_floors
        self.rooms = rooms

    def num_floors (self) -> int:
        return self.num_floors
    
    def get_rooms(self) ->list[Room]:
        return self.rooms

    def add_room(self,room:Room):
        if room and isinstance(room, Room) and Room not in self.rooms\
            and room.get_floor() <= self.get_num_floors():
            self.rooms.append(room)

    def __str__ (self) ->self:
        return f"(self.name.capitalize() @ {self.address})"
    
class BelloMio:

    def __init__(self,fregati):
         self.fregati = fregati

    b = Building (name = "SMI", address="via sierra nevada60", num_floors=5) 
    b.add_room(Room(id="666", floor=3., seats=32))
    armellini.add_room(Room(id="333", floor=2, seats=50))
    print(b.get_room())