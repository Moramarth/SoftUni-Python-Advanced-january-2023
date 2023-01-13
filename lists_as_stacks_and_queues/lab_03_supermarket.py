from _collections import deque

people_on_the_cash_register = deque()

COMMAND_END = "End"
COMMAND_PAID = "Paid"

while True:
    command = input()

    if command == COMMAND_END:
        print(f"{len(people_on_the_cash_register)} people remaining.")
        break
    elif command == COMMAND_PAID:
        while people_on_the_cash_register:
            print(people_on_the_cash_register.popleft())
    else:
        people_on_the_cash_register.append(command)
