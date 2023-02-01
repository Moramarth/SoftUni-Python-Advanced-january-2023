number_of_rows = int(input())
move_commands = input().split()

square_field = list()

total_coal = 0
coal_collected = 0

miner_position = list()

for row in range(number_of_rows):
    current_row = input().split()
    square_field.append(current_row)
    if "c" in current_row:
        total_coal += current_row.count("c")
    if "s" in current_row:
        miner_position = [row, current_row.index("s")]
        square_field[miner_position[0]][miner_position[1]] = "*"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for command in move_commands:
    new_row, new_column = directions[command]
    move_to_row, move_to_column = new_row + miner_position[0], new_column + miner_position[1]
    if 0 <= move_to_row < number_of_rows and 0 <= move_to_column < number_of_rows:
        miner_position = [move_to_row, move_to_column]
        if square_field[move_to_row][move_to_column] == "c":
            coal_collected += 1
            square_field[move_to_row][move_to_column] = "*"
            if coal_collected == total_coal:
                print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")
                break
        elif square_field[move_to_row][move_to_column] == "e":
            print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
            break
else:
    print(f"{total_coal - coal_collected} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
