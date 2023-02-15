field_size = int(input())


def position_change(start_position, direction):
    current_pos = [start_position[0], start_position[-1]]
    if direction == 'up':
        current_pos[0] -= 1
        if current_pos[0] < 0:
            current_pos[0] = field_size - 1

    elif direction == 'down':
        current_pos[0] += 1
        if current_pos[0] == field_size:
            current_pos[0] = 0

    elif direction == 'left':
        current_pos[1] -= 1
        if current_pos[1] < 0:
            current_pos[1] = field_size - 1

    elif direction == 'right':
        current_pos[1] += 1
        if current_pos[1] == field_size:
            current_pos[1] = 0

    return current_pos


player_position = list()
play_field = list()
collected_coins = 0
player_path = list()

for row_number in range(field_size):
    current_row = [int(item) if item.isnumeric() else item for item in input().split()]
    if "P" in current_row:
        player_position = [row_number, current_row.index("P")]
    play_field.append(current_row)

player_path.append([player_position[0], player_position[1]])

while collected_coins < 100:
    command = input()
    new_position = position_change(player_position, command)
    play_field[player_position[0]][player_position[1]] = 0
    player_position = [new_position[0], new_position[1]]
    player_path.append([player_position[0], player_position[1]])

    if play_field[new_position[0]][new_position[1]] == "X":
        collected_coins //= 2
        print(f"Game over! You've collected {collected_coins} coins.")
        break

    collected_coins += play_field[new_position[0]][new_position[1]]
    play_field[new_position[0]][new_position[1]] = "P"

else:
    print(f"You won! You've collected {collected_coins} coins.")

print("Your path:")
print(*player_path, sep="\n")
