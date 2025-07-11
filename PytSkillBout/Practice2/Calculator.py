class Calculator:
    #This func add 2 num
    def add(self, a, b):
        return a + b

    # This func minus 2 num
    def sub(self, a, b):
        return a - b

    # This func multiplies 2 num
    def mul(self, a, b):
        return a * b

    # This func Divides 2 num
    def div(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        else:
            return a / b

'''a = int(input())
b = int(input())'''
x = 10
y = 5
calc = Calculator()

print("Addition (10 + 5):", calc.add(x, y))
print("Subtraction (10 - 5):", calc.sub(x, y))
print("Multiplication (10 * 5):", calc.mul(x, y))
print("Division (10 / 5):", calc.div(x, y))
print("Division (10 / 0):", calc.div(x, 0))




