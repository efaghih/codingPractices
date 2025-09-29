# Let’s pick one that is simple but deep, often used by companies like Google,
# Amazon, or Uber to see if you understand OOP structure, encapsulation, and basic design

# Design a class RideShareCar to simulate a simple Uber car system.

# Requirements
# You need to build a class that can:
# Store the driver’s name and car model.
# Keep track of whether the car is available or busy.
# Store the current passenger’s name (if any).

# Have methods to:
# accept_ride(passenger_name) → mark car busy, assign passenger.
# end_ride() → finish ride, mark car available again.
# __repr__() → show a nice description of the car’s current state.


# 💡 Expected Output Example
# car1 = RideShareCar("Alex", "Toyota Camry")
# print(car1)
# # Output: RideShareCar(driver=Alex, model=Toyota Camry, available=True)

# car1.accept_ride("John")
# print(car1)
# # Output: RideShareCar(driver=Alex, model=Toyota Camry, passenger=John, available=False)

# car1.end_ride()
# print(car1)
# # Output: RideShareCar(driver=Alex, model=Toyota Camry, available=True)


### Start of code ###
class info:
    rate_per_km = 2.5   # class variable shared by all cars
    nextID = 1
    def __init__(self, dName, cModel):
        self.carID = self.nextID
        info.nextID += 1    # increase the class's variable not the instance one! 
        self.dName = dName  # driver name
        self.cModel = cModel    # car model
        self.available = True   # car availability 
        self.pName = None   # passenger name
        self.totalRides = 0
        self.total_earnings = 0
        self.distance = 0   # km
        self.history = []
        

    def accept_ride(self, passenger_name, distance):
        if self.available == False:
            print(f"The car is not available to accept {passenger_name}!")
            return None
        self.pName = passenger_name
        self.distance = distance
        self.available = False
        self.totalRides += 1
        print(f"{self.dName} accepted ride for {passenger_name} ({distance} km).")
    
    
    def end_ride(self):
        if self.available:
            print("No trip to end!")
            return
        self.available = True
        fare = self.distance * self.rate_per_km
        self.distance = fare
        self.total_earnings += fare 
        print(f"Ride with {self.pName} ended. Fare: ${fare:.2f}")
        self.history.append ({"passenger": self.pName, "distance": self.distance, "fare": fare}) 
        self.pName = None
        
    
    def __repr__(self):
        status = "available" if self.available else f"busy with {self.pName}"
        return f"RideShareCar(carID = {self.carID}, driver={self.dName}, model={self.cModel}, status={status}, earnings=${self.total_earnings:.2f})"
              

    def print_history(self):
        if not self.history:
            print("No history!")
            return
        
        for i, ride in enumerate(self.history, 0):
            print(f"{i}. Passenger: {ride['passenger']}, Distance: {ride['distance']} km, Fare: ${ride['fare']:.2f}")



        



from typing import List
class FleetManager:
    
    def __init__(self):
        self.cars:  List[info] = []
    
    def add_car(self, car: info):
        self.cars.append(car)

    def show_carList(self):
        for carID in self.cars:
            print(f"Car ID: {carID.carID}")
        





fm = FleetManager()


car1 = info ("ali", "benz")
fm.add_car(car1)

car1.accept_ride("mosi", 10)
#car1.__repr__()
car1.end_ride()

car1.accept_ride("Nino", 2)
car1.end_ride()

car1.accept_ride("Shina", 3)
car1.end_ride()

# car1.__repr__()

car1.accept_ride("Sara",5)
# car1.__repr__()
print(car1)
car1.end_ride()
print(car1)


car1.print_history()


car2 = info ("Mohsen", "BMW")
fm.add_car(car2)


fm.show_carList()
