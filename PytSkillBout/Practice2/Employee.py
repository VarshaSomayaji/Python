class Employee:
    def __init__(self):
        # Private attributes to store name, salary, and age
        self._name = ""
        self._salary = 0.0
        self._age = 0

    # Setter method for name
    def set_name(self, name):
        self._name = name

    # Getter method for name
    def get_name(self):
        return self._name

    # Setter method for salary
    def set_salary(self, salary):
        if salary > 0:
            self._salary = salary
        else:
            print("Error: Salary must be greater than 0.")

    # Getter method for salary
    def get_salary(self):
        return self._salary

    # Setter method for age with validation
    def set_age(self, age):
            self._age = age

    # Getter method for age
    def get_age(self):
        return self._age


# Create an employee
employee = Employee()

# Setting employee details
employee.set_name("John Doe")
employee.set_salary(50000.0)
employee.set_age(30)

# Display employee details
print(f"Employee Name: {employee.get_name()}")
print(f"Employee Salary: {employee.get_salary()}")
print(f"Employee Age: {employee.get_age()}")

# Attempt to set invalid salary and age
employee.set_salary(-100)  # Invalid salary


