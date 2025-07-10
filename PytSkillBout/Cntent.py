with open('data.txt', 'r') as file:
    text = file.read()
    words = text.split()
    print("No of words:", len(words))
