def index_validator(position):

    if 0 <= position[0] < play_field_size and 0 <= position[1] < play_field_size:
        return True

    return False


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

    return current_position


play_field_size = int(input())

field = list()
snake_position = list()
burrow_coordinates = list()
food_eaten = 0

for row_number in range(play_field_size):
    current_row = list(input())
    if "S" in current_row:
        snake_position = [row_number, current_row.index("S")]
    if "B" in current_row:
        if current_row.count("B") == 2:
            for i in range(len(current_row)):
                if current_row[i] == "B":
                    burrow_coordinates.append([row_number, i])
        burrow_coordinates.append([row_number, current_row.index("B")])

    field.append(current_row)

while food_eaten < 10:
    command = input()
    field[snake_position[0]][snake_position[1]] = "."
    new_position = position_change(snake_position, command)

    if not index_validator(new_position):
        print("Game over!")
        break

    if field[new_position[0]][new_position[1]] == "*":
        food_eaten += 1

    elif field[new_position[0]][new_position[1]] == "B":
        field[new_position[0]][new_position[1]] = "."
        index = burrow_coordinates.index([new_position[0], new_position[1]])
        new_position[0], new_position[1] = burrow_coordinates[index - 1][0], burrow_coordinates[index - 1][1]

    snake_position = [new_position[0], new_position[1]]
    field[snake_position[0]][snake_position[1]] = "S"

else:
    print("You won! You fed the snake.")


print(f"Food eaten: {food_eaten}")

for row in field:
    print("".join(row))
