import operator as op


def directional_check(board, current_position, player, direction, operator=op.add):
    digits = 0
    while board[current_position[0]][current_position[1]] == player:
        digits += 1

        if not index_validator_rows(operator(current_position[0], directions[direction][0])) \
                or not index_validator_cols(operator(current_position[1], directions[direction][1])):
            break
        current_position = [operator(current_position[0], directions[direction][0]),
                            operator(current_position[1],  directions[direction][1])]

    return digits


def win_condition_check(board, player, column, row):
    player_wins = False
    current_pos = (row, column)
    direction_digits = 0
    opposite_digits = 0
    for direction, value in directions.items():
        next_step = (current_pos[0] + value[0], current_pos[1] + value[1])

        if not index_validator_rows(next_step[0]) or not index_validator_cols(next_step[1]):
            continue

        if board[current_pos[0] + value[0]][current_pos[1] + value[1]] == player:
            direction_digits = directional_check(board, next_step, player, direction)
            opposite_direction = current_pos[0] - value[0], current_pos[1] - value[1]
            if not index_validator_rows(opposite_direction[0]) or not index_validator_cols(opposite_direction[1]):
                continue
            if board[current_pos[0] - value[0]][current_pos[1] - value[1]] == player:
                opposite_digits = directional_check(board, opposite_direction, player, direction, operator=op.sub)
        if (direction_digits + opposite_digits + 1) >= WIN_CONDITION:
            player_wins = True
            break

    return player_wins


def index_validator_rows(index):
    if 0 <= index < ROWS:
        return True


def index_validator_cols(index):
    if 0 <= index < COLS:
        return True


def player_turn(desired_column, board, player):
    if not index_validator_cols(desired_column):
        return f"Column does not exist, please enter a valid column!", board, None
    for row in range(ROWS - 1, -1, -1):
        if board[row][desired_column] == 0:
            board[row][desired_column] = player
            return f"Move successful!", board, row

        elif board[row][desired_column] == 1 or board[row][desired_column] == 2:
            if row == 0:
                return f"Spot is already taken, please try again!", board, None
            continue


def create_board():
    board = list()

    for row in range(ROWS):
        board.append([])
        for column in range(COLS):
            board[row].append(0)

    return board


def gameplay(play_field):
    player_one, player_two = 1, 2
    while True:
        print(f"Player {player_one} please choose a column to move")
        player_one_choice = int(input()) - 1
        response, play_field, current_row = player_turn(player_one_choice, play_field, player_one)
        print(response)
        print(*play_field, sep="\n")
        if response != "Move successful!":
            continue
        player_wins = win_condition_check(play_field, player_one, player_one_choice, current_row)
        if player_wins:
            print(f"The winner is player {player_one}")
            break
        player_one, player_two = player_two, player_one


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "top-left": (-1, -1),
    "bottom-right": (1, 1),
    "top-right": (-1, 1),
    "bottom-left": (1, -1),
}

try:
    ROWS = int(input("Please enter desired rows: "))
    COLS = int(input("Please enter desired columns: "))
    WIN_CONDITION = int(input("Please enter win condition number: "))
    field = create_board()
    print(*field, sep="\n")
    gameplay(field)
except ValueError:
    print("All values must be integer!")
