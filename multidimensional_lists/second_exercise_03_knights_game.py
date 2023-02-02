def attack_options_func(coordinates):
    attacks = 0
    for x, y in clockwise_moves.values():
        move_row, move_column = x + coordinates[0], y + coordinates[1]
        if 0 <= move_row < board_size and 0 <= move_column < board_size and chess_board[move_row][move_column] == "K":
            attacks += 1
    return attacks


board_size = int(input())

chess_board = [list(input()) for _ in range(board_size)]

removed_knights = 0

clockwise_moves = {
    "1": (-2, 1),
    "2": (-1, 2),
    "3": (1, 2),
    "4": (2, 1),
    "5": (2, -1),
    "6": (1, -2),
    "7": (-1, -2),
    "8": (-2, -1),
}
while True:
    max_possible_attacks = 0
    knight_to_be_removed = []
    for row in range(board_size):
        for column in range(board_size):
            if chess_board[row][column] == "K":
                position = [row, column]
                attack_count = attack_options_func(position)
                if attack_count > max_possible_attacks:
                    max_possible_attacks = attack_count
                    knight_to_be_removed = position
    if max_possible_attacks == 0:
        break
    chess_board[knight_to_be_removed[0]][knight_to_be_removed[1]] = "0"
    removed_knights += 1

print(removed_knights)
