from abc import ABC, abstractmethod 

class vechicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(vechicle):
    def start_engine(self):
        print("Car engine started.Vroom!!!")

    def stop_engine(self):
        print("car engine has stopped") 

class Bike(vechicle):
    def start_engine(self):
        print("Bike engine has started ,zOOOOOm!!!")

carObj = Car()
carObj.start_engine()
carObj.stop_engine()
Bikeobj = Bike()
Bikeobj.start_engine()        