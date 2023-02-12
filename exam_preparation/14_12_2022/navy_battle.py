battlefield_size = int(input())

battle_field = list()
submarine_position = list()

for row in range(battlefield_size):
    current_row = list(input())
    if "S" in current_row:
        submarine_position = [row, current_row.index("S")]
    battle_field.append(current_row)

destroyed_ships = 0
hits_taken = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    if destroyed_ships == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break
    elif hits_taken == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates"
              f" [{submarine_position[0]}, {submarine_position[1]}]!")
        break
    command = input()
    battle_field[submarine_position[0]][submarine_position[1]] = "-"
    new_row, new_column = directions[command][0] + submarine_position[0], \
                          directions[command][1] + submarine_position[1]

    if battle_field[new_row][new_column] == "C":
        destroyed_ships += 1

    elif battle_field[new_row][new_column] == "*":
        hits_taken += 1

    battle_field[new_row][new_column] = "S"
    submarine_position = [new_row, new_column]

for row in battle_field:
    print(*row, sep="")
