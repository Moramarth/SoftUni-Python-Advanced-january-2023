from collections import deque


def rest_condition(player):
    global jerry_is_resting
    global tom_is_resting
    if player == "Tom" and tom_is_resting:
        tom_is_resting = False
        return True
    elif player == "Jerry" and jerry_is_resting:
        jerry_is_resting = False
        return True
    else:
        return False


player_one, player_two = input().split(", ")

game_board = []
for row in range(6):
    current_row = input().split()
    game_board.append(current_row)

tom_is_resting = False
jerry_is_resting = False
players = deque([player_one, player_two])


while True:
    data = input().split(", ")
    coordinates = [int(data[0][1:]), int(data[1][:-1])]
    current_player = players.popleft()

    if rest_condition(current_player):
        players.append(current_player)
        continue

    if game_board[coordinates[0]][coordinates[1]] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break

    elif game_board[coordinates[0]][coordinates[1]] == "T":
        print(f"{current_player} is out of the game! The winner is {players.popleft()}.")
        break

    elif game_board[coordinates[0]][coordinates[1]] == "W":
        if current_player == "Tom":
            tom_is_resting = True
        elif current_player == "Jerry":
            jerry_is_resting = True
        print(f"{current_player} hits a wall and needs to rest.")

    players.append(current_player)
