from sys import maxsize


def moving_bunny_func(square, bunny_position):
    max_eggs = -maxsize
    where_to_go = ""
    best_path = list()
    for key, value in directions.items():
        current_path = list()
        x, y = value[0], value[1]
        collected_eggs = 0
        next_step_row = x + bunny_position[0]
        next_step_column = y + bunny_position[1]
        if not (0 <= next_step_row < field_size and 0 <= next_step_column < field_size):
            continue
        else:
            next_step = square[next_step_row][next_step_column]
        while next_step != "X":
            current_path.append([next_step_row, next_step_column])
            collected_eggs += int(square[next_step_row][next_step_column])
            next_step_row += x
            next_step_column += y
            if not (0 <= next_step_row < field_size and 0 <= next_step_column < field_size):
                break
            next_step = square[next_step_row][next_step_column]
        if collected_eggs > max_eggs:
            max_eggs = collected_eggs
            where_to_go = key
            best_path = current_path

    return max_eggs, where_to_go, best_path


field_size = int(input())

field = []
bunny = []

for row in range(field_size):
    current_row = input().split()
    field.append(current_row)
    if "B" in current_row:
        bunny = [row, current_row.index("B")]
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

eggs, direction, route = moving_bunny_func(field, bunny)

print(direction)
print(*route, sep="\n")
print(eggs)
