numbers = []
for i in range(5):
    numbers.append(int(input(f"Enter number {i+1}: ")))
print("Reversed:", numbers[::-1], "Sum:", sum(numbers), "Average:", sum(numbers)/len(numbers))
