with open("example.txt", "w") as f:
    f.write(input("Enter text : ") + "\n")

with open("example.txt", "r") as f:
    print("\nFile content:\n" + f.read())

with open("example.txt", "a") as f:
    f.write(input("append: ") + "\n")

with open("example.txt", "r") as f:
    print("\nFile content:\n" + f.read())
