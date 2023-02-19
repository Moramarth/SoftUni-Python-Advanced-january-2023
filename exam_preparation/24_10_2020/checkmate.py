def position_change(start_position, direction):

    current_position = [start_position[0], start_position[1]]

    if direction == 'up':
        current_position[0] -= 1

    elif direction == 'down':
        current_position[0] += 1

    elif direction == 'left':
        current_position[1] -= 1

    elif direction == 'right':
        current_position[1] += 1

    elif direction == "top-left":
        current_position[0] -= 1
        current_position[1] -= 1

    elif direction == "top-right":
        current_position[0] -= 1
        current_position[1] += 1

    elif direction == "bottom-left":
        current_position[0] += 1
        current_position[1] -= 1

    elif direction == "bottom-right":
        current_position[0] += 1
        current_position[1] += 1

    return current_position


def capture_test(king_coordinates):

    for direction in directions:
        next_step = [king_coordinates[0], king_coordinates[1]]
        while True:
            next_step = position_change(next_step, direction)
            if next_step in queens_positions:
                can_capture.append([next_step[0], next_step[1]])
                break
            if not 0 <= next_step[0] < board_size or not 0 <= next_step[1] < board_size:
                break


directions = ["up", "down", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right"]
board_size = 8

queens_positions = list()
king_position = list()
can_capture = list()

for row_number in range(board_size):
    current_row = input().split()
    for j in range(len(current_row)):
        if current_row[j] == "K":
            king_position = [row_number, j]
        elif current_row[j] == "Q":
            queens_positions.append([row_number, j])

capture_test(king_position)

if can_capture:
    print(*can_capture, sep="\n")
else:
    print("The king is safe!")
