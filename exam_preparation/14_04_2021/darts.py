from collections import deque


def zone(row, column):
    return (int(darts_board[row][0]) + int(darts_board[row][matrix_size - 1])
            + int(darts_board[0][column]) + int(darts_board[matrix_size - 1][column]))


def points_calculator(position):
    score = 0
    row, column = position[0], position[1]

    if darts_board[row][column] == "D":
        score += zone(row, column) * 2

    elif darts_board[row][column] == "T":
        score += zone(row, column) * 3

    else:
        score += int(darts_board[row][column])

    return score


matrix_size = 7

players_turn = deque(input().split(", "))
score_sheet = deque([501, 501])
throw_count = deque([0, 0])

bullseye = []
darts_board = list()

for row_number in range(matrix_size):
    current_row = input().split()
    if "B" in current_row:
        bullseye = [row_number, current_row.index("B")]
    darts_board.append(current_row)

while True:
    player = players_turn.popleft()
    points = score_sheet.popleft()
    throw_number = throw_count.popleft()
    throw_number += 1

    data = input().split(", ")
    coordinates = [int(data[0][1:]), int(data[1][:-1])]

    if coordinates == bullseye:
        print(f"{player} won the game with {throw_number} throws!")
        break

    if not 0 <= coordinates[0] < matrix_size or not 0 <= coordinates[1] < matrix_size:
        players_turn.append(player)
        score_sheet.append(points)
        throw_count.append(throw_number)
        continue

    points -= points_calculator(coordinates)
    if points <= 0:
        print(f"{player} won the game with {throw_number} throws!")
        break
    players_turn.append(player)
    score_sheet.append(points)
    throw_count.append(throw_number)
