from collections import deque


def out_of_bounds(position):
    if position[0] < 0:
        position[0] = field_size - 1
    elif position[0] == field_size:
        position[0] = 0
    if position[1] < 0:
        position[1] = field_size - 1
    elif position[1] == field_size:
        position[1] = 0

    return position


def position_change(start_position, direction):

    if direction == 'up':
        start_position[0] -= 1
    elif direction == 'down':
        start_position[0] += 1
    elif direction == 'left':
        start_position[1] -= 1
    elif direction == 'right':
        start_position[1] += 1

    start_position = out_of_bounds(start_position)

    return start_position


field_size = 6

exploration_area = list()
rover_coordinates = list()

water_collected = 0
metal_collected = 0
concrete_collected = 0

for row in range(field_size):
    current_row = input().split()
    if "E" in current_row:
        rover_coordinates = [row, current_row.index("E")]
    exploration_area.append(current_row)

commands = deque(input().split(", "))

while commands:
    to_go = commands.popleft()
    next_step = position_change(rover_coordinates, to_go)
    row, column = next_step[0], next_step[1]

    if exploration_area[row][column] == "R":
        print(f"Rover got broken at ({row}, {column})")
        break

    elif exploration_area[row][column] == "W":
        print(f"Water deposit found at ({row}, {column})")
        water_collected += 1

    elif exploration_area[row][column] == "M":
        print(f"Metal deposit found at ({row}, {column})")
        metal_collected += 1

    elif exploration_area[row][column] == "C":
        print(f"Concrete deposit found at ({row}, {column})")
        concrete_collected += 1

    rover_coordinates = [row, column]


if water_collected and metal_collected and concrete_collected:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
