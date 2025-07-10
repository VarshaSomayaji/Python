from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine is now ON.")

class Fridge(Appliance):
    def turn_on(self):
        print("Fridge is now ON and cooling.")

a1 = WashingMachine()
a1.turn_on()

a2 = Fridge()
a2.turn_on()
