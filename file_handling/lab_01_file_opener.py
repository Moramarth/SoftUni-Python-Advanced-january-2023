try:
    with open("text.txt") as file:
        print("File exists")
except FileNotFoundError:
    print("File not found")
