number_of_integers = int(input())

my_stack = list()

COMMAND_PUSH = "1"
COMMAND_POP = "2"
PRINT_MAX = "3"
PRINT_MIN = "4"

for _ in range(number_of_integers):
    command = input()

    if command.startswith(COMMAND_PUSH):
        integer = int(command.split()[1])
        my_stack.append(integer)
    elif not my_stack:
        continue
    elif command == COMMAND_POP:
        my_stack.pop()
    elif command == PRINT_MAX:
        print(max(my_stack))
    elif command == PRINT_MIN:
        print(min(my_stack))

my_stack.reverse()
my_stack = list(map(str, my_stack))
print(", ".join(my_stack))
