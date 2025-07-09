from logic import *

name = input("Enter your name: ")
marks = list(map(int, input("Enter marks : ").split()))

avg = calcavg(marks)
grade = get_grade(avg)

print("Name:", name)
print("Marks:", marks)
print("Average:", round(avg, 2))
print("Grade:", grade)
