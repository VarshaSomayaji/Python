class Employee:
    def work(self):
        print("Employee is working.")

class Manager(Employee):
    def manage(self):
        print("Manager is managing the team.")

e1 = Employee()
e1.work()

m1 = Manager()
m1.work()
m1.manage()
