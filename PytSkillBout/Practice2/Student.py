class Student:
    # a func for private atribu8te
    def __init__(self):
        self.__name = ""  # Name private attribute
        self.__marks = 0  # Marks private attribute

    #Func to set name
    def set_name(self, n):
        self.__name = n  # set name

    # Func to get name
    def get_name(self):
        return self.__name  # get name

    # Func to set marks
    def set_marks(self, m):
        if 0 <= m <= 100:  # check marks range
            self.__marks = m
        else:
            print("Error: Marks should be between 0 and 100.")

    # Func to get marks
    def get_marks(self):
        return self.__marks #get marks

#Create objects
s = Student()
s.set_name("Alice")
s.set_marks(99)
print("Student Name:", s.get_name())
print("Student Marks:", s.get_marks())

# try invalid marks
s.set_marks(-5)  # invalid
print("Student Marks (after invalid input):", s.get_marks())



