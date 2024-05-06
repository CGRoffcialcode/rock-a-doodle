class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = ["Gimmy","dajdhw","Ayan","Saif"]

    def add_passeger(self, name):
        if not self.open_seats():
            return False 
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
    
    



flight = Flight(3)

people = [""]
for person in people:
    
    if flight.add_passeger(person):
        print(f"Added {person} to flight successfuly")
    else:
        print(f"No avalible seats for {person}")
    