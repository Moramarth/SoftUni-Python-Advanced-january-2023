size_of_matrix = int(input())
racing_number = input()
race_track = list()
tunnel_positions = list()

distance_covered = 0
car_position = [0, 0]
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size_of_matrix):
    current_row = input().split()
    if "T" in current_row:
        tunnel_positions.append((row, current_row.index("T")))
    race_track.append(current_row)


while True:
    command = input()
    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        race_track[car_position[0]][car_position[1]] = "C"
        break
    new_row, new_column = car_position[0] + directions[command][0], car_position[1] + directions[command][1]
    race_track[car_position[0]][car_position[1]] = "."

    if race_track[new_row][new_column] == "F":
        distance_covered += 10
        print(f"Racing car {racing_number} finished the stage!")
        race_track[new_row][new_column] = "C"
        break
    elif race_track[new_row][new_column] == "T":
        distance_covered += 30
        race_track[new_row][new_column] = "."
        if (new_row, new_column) == tunnel_positions[0]:
            new_row, new_column = tunnel_positions[1]
        else:
            new_row, new_column = tunnel_positions[0]
        car_position = [new_row, new_column]
        race_track[new_row][new_column] = "C"
    else:
        distance_covered += 10
        car_position = [new_row, new_column]
        race_track[new_row][new_column] = "C"


print(f"Distance covered {distance_covered} km.")

for row in race_track:
    print("".join(row))
