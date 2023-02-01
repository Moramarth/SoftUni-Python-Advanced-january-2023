from copy import deepcopy


def bunny_multiplication_func(play_field_copy, bunny, player_is_alive):
    for x, y in directions.values():
        new_bunny_row, new_bunny_column = bunny[0] + x, bunny[1] + y
        if (0 <= new_bunny_row < number_of_rows) and (0 <= new_bunny_column < number_of_columns):
            if play_field_copy[new_bunny_row][new_bunny_column] == "P":
                player_is_alive = False
            play_field_copy[new_bunny_row][new_bunny_column] = "B"

    return play_field_copy, player_is_alive


def bunnies_turn_func(play_field, player_status):
    player_is_alive = player_status
    play_field_copy = deepcopy(play_field)

    for r in range(number_of_rows):
        for c in range(number_of_columns):
            if play_field[r][c] == "B":
                bunny = [r, c]
                play_field_copy, player_is_alive = bunny_multiplication_func(play_field_copy, bunny, player_is_alive)
    play_field = play_field_copy
    return play_field, player_is_alive


def player_turn_func(play_field, player, movement):
    player_is_alive = True
    player_escapes = False
    new_row, new_column = player[0] + movement[0], player[1] + movement[1]
    if not (0 <= new_row < number_of_rows) or not (0 <= new_column < number_of_columns):
        play_field[player[0]][player[1]] = "."
        player_escapes = True
    elif play_field[new_row][new_column] == "B":
        player_is_alive = False
        play_field[player[0]][player[1]] = "."
        player = [new_row, new_column]
    else:
        play_field[player[0]][player[1]] = "."
        player = [new_row, new_column]
        play_field[player[0]][player[1]] = "P"

    return play_field, player, player_is_alive, player_escapes


number_of_rows, number_of_columns = map(int, input().split())

bunny_lair = list()
player_position = list()
player_alive = True
player_wins = False

for row in range(number_of_rows):
    current_row = list(input())
    if "P" in current_row:
        player_position = [row, current_row.index("P")]
    bunny_lair.append(current_row)

move_commands = list(input())

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

for move in move_commands:
    if player_wins:
        break
    if not player_alive:
        break
    bunny_lair, player_position, player_alive, player_wins = \
        player_turn_func(bunny_lair, player_position, directions[move])
    bunny_lair, player_alive = bunnies_turn_func(bunny_lair, player_alive)


for row in range(number_of_rows):
    print(*bunny_lair[row], sep="")

if player_wins:
    print(f"won: {player_position[0]} {player_position[1]}")
else:
    print(f"dead: {player_position[0]} {player_position[1]}")
