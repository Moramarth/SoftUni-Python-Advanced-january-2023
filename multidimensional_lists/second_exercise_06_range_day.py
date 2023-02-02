number_of_rows = 5

shooting_range = list()
my_position = list()

total_targets = 0
hit_targets_locations = list()

for row in range(number_of_rows):
    current_row = input().split()
    if "A" in current_row:
        my_position = [row, current_row.index("A")]
    if "x" in current_row:
        total_targets += current_row.count("x")
    shooting_range.append(current_row)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

number_of_commands = int(input())

for _ in range(number_of_commands):

    command, *info = input().split()
    if command == "move":
        direction = info[0]
        steps = int(info[1])
        x, y = directions[direction]
        my_pos_row, my_pos_col = my_position[0], my_position[1]
        for _ in range(steps):
            my_pos_row += x
            my_pos_col += y
            if not (0 <= my_pos_row < number_of_rows and 0 <= my_pos_col < number_of_rows):
                break
        else:
            if shooting_range[my_pos_row][my_pos_col] == ".":
                my_position = [my_pos_row, my_pos_col]

    elif command == "shoot":
        direction = info[0]
        x, y = directions[direction]
        my_pos_row, my_pos_col = my_position[0], my_position[1]
        while True:
            my_pos_row += x
            my_pos_col += y
            if not (0 <= my_pos_row < number_of_rows and 0 <= my_pos_col < number_of_rows):
                break
            if shooting_range[my_pos_row][my_pos_col] == "x":
                hit_targets_locations.append([my_pos_row, my_pos_col])
                shooting_range[my_pos_row][my_pos_col] = "."
                break

    if len(hit_targets_locations) == total_targets:
        print(f"Training completed! All {len(hit_targets_locations)} targets hit.")
        print(*hit_targets_locations, sep="\n")
        break
else:
    print(f"Training not completed! {total_targets - len(hit_targets_locations)} targets left.")
    print(*hit_targets_locations, sep="\n")
