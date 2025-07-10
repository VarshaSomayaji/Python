def divide(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        print("Cant div by zero")
        return None
a = float(input("a: "))
b = float(input("b: "))
res = divide(a, b)
print("Result:", res)
