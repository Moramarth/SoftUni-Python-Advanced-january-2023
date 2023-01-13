from _collections import deque

water_amount = int(input())
people_to_drink = deque()

COMMAND_START = "Start"
COMMAND_END = "End"
COMMAND_REFILL = "refill"

command = input()
while command != COMMAND_START:
    people_to_drink.append(command)
    command = input()


while True:
    command = input()
    if command == COMMAND_END:
        print(f"{water_amount} liters left")
        break
    elif command.startswith(COMMAND_REFILL):
        water_amount += int(command.split()[1])
    else:
        person = people_to_drink.popleft()
        needed_water_amount = int(command)
        if water_amount >= needed_water_amount:
            water_amount -= needed_water_amount
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
