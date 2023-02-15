initial_string = input()


def position_change(start_position, direction):
    current_position = [start_position[0], start_position[1]]

    if direction == 'up':
        current_position[0] -= 1
    elif direction == 'down':
        current_position[0] += 1
    elif direction == 'left':
        current_position[1] -= 1
    elif direction == 'right':
        current_position[1] += 1

    if not 0 <= current_position[0] < matrix_size or not 0 <= current_position[1] < matrix_size:
        current_position = [start_position[0], start_position[1]]

    return current_position


matrix_size = int(input())
field = list()
player_position = list()

for row_number in range(matrix_size):
    current_row = list(input())
    if "P" in current_row:
        player_position = [row_number, current_row.index("P")]
    field.append(current_row)

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input()
    new_position = position_change(player_position, command)

    if player_position == new_position:
        if initial_string:
            initial_string = initial_string[:-1]
        continue

    if field[new_position[0]][new_position[1]] != "-":
        initial_string += field[new_position[0]][new_position[1]]

    field[player_position[0]][player_position[1]] = "-"
    field[new_position[0]][new_position[1]] = "P"
    player_position = [new_position[0], new_position[1]]

print(initial_string)

for row in field:
    print("".join(row))
