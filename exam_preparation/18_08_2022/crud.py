def position_change(start_position, direction):
    next_position = []
    if direction == 'up':
        next_position = [start_position[0] - 1, start_position[1]]
    elif direction == 'down':
        next_position = [start_position[0] + 1, start_position[1]]
    elif direction == 'left':
        next_position = [start_position[0], start_position[1] - 1]
    elif direction == 'right':
        next_position = [start_position[0], start_position[1] + 1]
    return next_position


grid = list()

for row in range(6):
    grid.append(input().split())

starting_info = input().split(", ")

starting_pos = [int(starting_info[0][1:]), int(starting_info[1][:-1])]


command = input()

while command != "Stop":
    to_do, go_to, *values = command.split(", ")
    starting_pos = position_change(starting_pos, go_to)

    if to_do == "Create":
        if grid[starting_pos[0]][starting_pos[1]] == ".":
            grid[starting_pos[0]][starting_pos[1]] = values[0]

    elif to_do == "Update":
        if grid[starting_pos[0]][starting_pos[1]] != ".":
            grid[starting_pos[0]][starting_pos[1]] = values[0]

    elif to_do == "Delete":
        if grid[starting_pos[0]][starting_pos[1]] != ".":
            grid[starting_pos[0]][starting_pos[1]] = "."

    elif to_do == "Read":
        if grid[starting_pos[0]][starting_pos[1]] != ".":
            print(grid[starting_pos[0]][starting_pos[1]])

    command = input()

for row in grid:
    print(" ".join(row))
