from fibonacci import *

sequence = list()

command = input()

while command != "Stop":
    to_do, *info = command.split()
    if to_do == "Create":
        number = int(info[1])
        sequence = create(number)
        print(*sequence, sep=" ")
    elif to_do == "Locate":
        number = int(info[0])
        print(locate(sequence, number))
    else:
        print("Please enter a valid command!")

    command = input()