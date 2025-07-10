class Marks:
    def __init__(self):
        self.__math = 0

    def set_marks(self, m):
        if 0 <= m <= 100:
            self.__math = m

    def show_marks(self):
        print("Math Marks:", self.__math)

m1 = Marks()
m = int(input("Enter math marks (0-100): "))
m1.set_marks(m)
m1.show_marks()
