from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine is ON.")

    def turn_off(self):
        print("Washing Machine is OFF.")

class Fridge(Appliance):
    def turn_on(self):
        print("Fridge is now ON.")

    def turn_off(self):
        print("Fridge is now OFF.")

print("Choose ONE appliance:")
print("1. Washing Machine")
print("2. Fridge")

choice = input("Enter choice (1 or 2): ").strip()

if choice == "1":
    appliance = WashingMachine()
elif choice == "2":
    appliance = Fridge()
else:
    print("Invalid choice. Please select only one valid appliance.")
    exit()

action = input("Enter action (on/off): ").strip().lower()

if action == "on":
    appliance.turn_on()
elif action == "off":
    appliance.turn_off()
else:
    print("Invalid action. Please enter 'on' or 'off'.")
