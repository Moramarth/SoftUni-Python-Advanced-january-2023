first_sequence = set(int(number) for number in input().split())
second_sequence = set(int(number) for number in input().split())

number_of_commands = int(input())

for _ in range(number_of_commands):
    first_command, *data = input().split()
    to_do = first_command + " " + data.pop(0)

    if to_do == "Add First":
        [first_sequence.add(int(number)) for number in data]
    elif to_do == "Add Second":
        [second_sequence.add(int(number)) for number in data]
    elif to_do == "Remove First":
        [first_sequence.discard(int(number)) for number in data]
    elif to_do == "Remove Second":
        [second_sequence.discard(int(number)) for number in data]
    else:
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print(True)
        else:
            print(False)

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
