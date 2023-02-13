from collections import deque


def current_status():
    white_pawn_pos_ = []
    black_pawn_pos_ = []
    board = []
    for row in range(8):
        current_row = input().split()
        if "w" in current_row:
            white_pawn_pos_ = [row, current_row.index("w")]
        if "b" in current_row:
            black_pawn_pos_ = [row, current_row.index("b")]
        board.append(current_row)
    return board, white_pawn_pos_, black_pawn_pos_


def mark_squares():
    squares = list()
    for num in range(8, 0, -1):
        row_to_mark = []
        for char in range(97, 97 + 8):
            row_to_mark.append(chr(char) + str(num))
        squares.append(row_to_mark)
    return squares


def movement(current_pawn):
    global game_ended

    if current_pawn == "w":
        if 0 <= white_pawn_pos[1] + left < 8:
            left_diagonal = [white_pawn_pos[0] + white_move, white_pawn_pos[1] + left]
            if chessboard[left_diagonal[0]][left_diagonal[1]] == "b":
                game_ended = True
                print(f"Game over! White win, capture on {square_marked[left_diagonal[0]][left_diagonal[1]]}.")

        if 0 <= white_pawn_pos[1] + right < 8:
            right_diagonal = [white_pawn_pos[0] + white_move, white_pawn_pos[1] + right]
            if chessboard[right_diagonal[0]][right_diagonal[1]] == "b":
                game_ended = True
                print(f"Game over! White win, capture on {square_marked[right_diagonal[0]][right_diagonal[1]]}.")

        chessboard[white_pawn_pos[0]][white_pawn_pos[1]] = "-"
        white_pawn_pos[0] += white_move
        chessboard[white_pawn_pos[0]][white_pawn_pos[1]] = "w"

    elif current_pawn == "b":
        if 0 <= black_pawn_pos[1] + left < 8:
            left_diagonal = [black_pawn_pos[0] + black_move, black_pawn_pos[1] + left]
            if chessboard[left_diagonal[0]][left_diagonal[1]] == "w":
                game_ended = True
                print(f"Game over! Black win, capture on {square_marked[left_diagonal[0]][left_diagonal[1]]}.")

        if 0 <= black_pawn_pos[1] + right < 8:
            right_diagonal = [black_pawn_pos[0] + black_move, black_pawn_pos[1] + right]
            if chessboard[right_diagonal[0]][right_diagonal[1]] == "w":
                game_ended = True
                print(f"Game over! Black win, capture on {square_marked[right_diagonal[0]][right_diagonal[1]]}.")

        chessboard[black_pawn_pos[0]][black_pawn_pos[1]] = "-"
        black_pawn_pos[0] += black_move
        chessboard[black_pawn_pos[0]][black_pawn_pos[1]] = "b"


square_marked = mark_squares()
chessboard, white_pawn_pos, black_pawn_pos = current_status()

white_move = -1
left = -1
right = 1
black_move = 1


players_turn = deque(["w", "b"])
game_ended = False

while True:
    pawn = players_turn.popleft()
    movement(pawn)

    if game_ended:
        break

    players_turn.append(pawn)

    if white_pawn_pos[0] == 0:
        print(f"Game over! White pawn is promoted to a queen at {square_marked[white_pawn_pos[0]][white_pawn_pos[1]]}.")
        break
    elif black_pawn_pos[0] == 7:
        print(f"Game over! Black pawn is promoted to a queen at {square_marked[black_pawn_pos[0]][black_pawn_pos[1]]}.")
        break
