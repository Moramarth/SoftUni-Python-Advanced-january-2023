def points_calculator(coordinates):
    score = 0
    row_number = coordinates[0] - 1
    column_number = coordinates[1]

    while [row_number, column_number] != coordinates:
        if row_number < 0:
            row_number = board_size - 1
        if board[row_number][column_number] == "B":
            break
        score += int(board[row_number][column_number])
        row_number -= 1

    return score


board_size = 6

board = list()
buckets_positions = list()
buckets_hit = list()
points = 0
prize = ""

for row in range(board_size):
    current_row = input().split()
    for i in range(board_size):
        if current_row[i] == "B":
            buckets_positions.append([row, i])
    board.append(current_row)


for _ in range(3):
    data = input().split(", ")
    throw = [int(data[0][1:]), int(data[1][:-1])]
    if throw in buckets_hit or throw not in buckets_positions:
        continue

    points += points_calculator(throw)
    buckets_hit.append(throw)

if 100 <= points < 200:
    prize = "Football"
elif 200 <= points < 300:
    prize = "Teddy Bear"
elif points >= 300:
    prize = "Lego Construction Set"

if prize:
    print(f"Good job! You scored {points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
