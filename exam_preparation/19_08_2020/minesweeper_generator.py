def index_validator(new_position):
    if 0 <= new_position[0] < field_size and 0 <= new_position[1] < field_size:
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

    elif direction == "top-left":
        current_position[0] -= 1
        current_position[1] -= 1

    elif direction == "top-right":
        current_position[0] -= 1
        current_position[1] += 1

    elif direction == "bottom-left":
        current_position[0] += 1
        current_position[1] -= 1

    elif direction == "bottom-right":
        current_position[0] += 1
        current_position[1] += 1

    return current_position


def minesweeper(coordinates):
    mines_count = 0
    for direction in directions:
        new_position = position_change(coordinates, direction)
        if index_validator(new_position):
            if mine_field[new_position[0]][new_position[1]] == "*":
                mines_count += 1
    return mines_count


field_size = int(input())
number_of_mines = int(input())

mine_field = list()
mines_coordinates = list()
directions = ["up", "down", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right"]

for i in range(field_size):
    mine_field.append([])
    for j in range(field_size):
        mine_field[i].append(0)


for _ in range(number_of_mines):
    data = input().strip("(").strip(")").split(", ")
    mines_coordinates.append(data)

for item in mines_coordinates:
    mine_field[int(item[0])][int(item[1])] = "*"


for row in range(field_size):
    for column in range(field_size):
        position = [row, column]
        if mine_field[row][column] == "*":
            continue
        else:
            value = minesweeper(position)
            mine_field[row][column] = value

for row_number in mine_field:
    print(*row_number, sep=" ")
