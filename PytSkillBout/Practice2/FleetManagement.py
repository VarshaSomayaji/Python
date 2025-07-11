# Base class: Vehicle
class Vehicle:
    def __init__(self, brand, fuel_capacity):
        self.brand = brand
        self.fuel_capacity = fuel_capacity
        self.fuel = 0  # Initially, no fuel
        self.km_run = 0  # Initially, no distance traveled

    def start(self):
        print(f"{self.brand} is starting...")

    def stop(self):
        print(f"{self.brand} is stopping...")

    def refuel(self, liters):
        if liters <= 0:
            print(f"{self.brand}: Invalid fuel amount.")
        elif self.fuel + liters > self.fuel_capacity:
            print(f"{self.brand}: Cannot refuel beyond fuel capacity.")
        else:
            self.fuel += liters
            print(f"{self.brand}: Refueled {liters}L. Current fuel: {self.fuel}L")

    def run_trip(self, km):
        # A trip consumes fuel, 1L for every 10 km.
        fuel_needed = km / 10
        if self.fuel >= fuel_needed:
            self.km_run += km
            self.fuel -= fuel_needed
            print(f"{self.brand}: Trip of {km} km completed.")
        else:
            print(f"{self.brand}: Not enough fuel for the trip.")

    def needs_service(self):
        return self.km_run > 10000  # Needs service if km_run > 10,000


# Derived class: Car
class Car(Vehicle):
    def __init__(self, brand, fuel_capacity):
        super().__init__(brand, fuel_capacity)

    def start(self):
        print(f"{self.brand} Car is starting...")

    def stop(self):
        print(f"{self.brand} Car is stopping...")


# Derived class: Bike
class Bike(Vehicle):
    def __init__(self, brand, fuel_capacity):
        super().__init__(brand, fuel_capacity)

    def start(self):
        print(f"{self.brand} Bike is starting...")

    def stop(self):
        print(f"{self.brand} Bike is stopping...")


# Derived class: Truck
class Truck(Vehicle):
    def __init__(self, brand, fuel_capacity):
        super().__init__(brand, fuel_capacity)

    def start(self):
        print(f"{self.brand} Truck is starting...")

    def stop(self):
        print(f"{self.brand} Truck is stopping...")


# Fleet Management Class
class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def show_fleet_summary(self):
        print("\n=== Fleet Summary ===")
        for vehicle in self.vehicles:
            print(f"{vehicle.__class__.__name__} - Brand: {vehicle.brand}, Fuel: {vehicle.fuel}L, KM Run: {vehicle.km_run}")
            print(f"{vehicle.brand} is a {vehicle.__class__.__name__}")
            if vehicle.needs_service():
                print(f"Needs Service")
            else:
                print(f"Does Not Need Service")
            print()


# Example usage
if __name__ == "__main__":
    # Create vehicles
    car = Car("Toyota", 50)
    bike = Bike("Yamaha", 20)
    truck = Truck("Volvo", 150)

    # Fleet management
    fleet = Fleet()
    fleet.add_vehicle(car)
    fleet.add_vehicle(bike)
    fleet.add_vehicle(truck)

    # Operations on the vehicles
    car.start()
    car.refuel(30)
    car.run_trip(200)
    car.stop()

    bike.start()
    bike.refuel(30)
    bike.run_trip(200)
    bike.stop()

    truck.start()
    truck.refuel(30)
    truck.run_trip(200)
    truck.stop()

    # Show fleet summary
    fleet.show_fleet_summary()
