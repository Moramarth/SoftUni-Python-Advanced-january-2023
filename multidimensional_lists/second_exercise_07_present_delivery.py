presents_count = int(input())

square_size = int(input())

neighborhood = list()
santa_position = list()

nice_kids = 0
nice_gifts = 0

for row in range(square_size):
    current_row = input().split()
    if "S" in current_row:
        santa_position = [row, current_row.index("S")]
    if "V" in current_row:
        nice_kids += current_row.count("V")
    neighborhood.append(current_row)


directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

while presents_count > 0:
    command = input()
    if command == "Christmas morning":
        break
    row, col = directions[command][0], directions[command][1]
    new_row, new_column = santa_position[0] + row, santa_position[1] + col
    if not (0 <= new_row < square_size and 0 <= new_column < square_size):
        continue

    neighborhood[santa_position[0]][santa_position[1]] = "-"
    if neighborhood[new_row][new_column] == "V":
        nice_gifts += 1
        presents_count -= 1
    elif neighborhood[new_row][new_column] == "C":
        neighborhood[new_row][new_column] = "S"
        for key, value in directions.items():
            if neighborhood[new_row + value[0]][new_column+value[1]] == "V":
                nice_gifts += 1
                presents_count -= 1
                neighborhood[new_row + value[0]][new_column + value[1]] = "-"
            elif neighborhood[new_row + value[0]][new_column+value[1]] == "X":
                presents_count -= 1
                neighborhood[new_row + value[0]][new_column+value[1]] = "-"

            if presents_count == 0:
                break

    neighborhood[new_row][new_column] = "S"
    santa_position = [new_row, new_column]

if presents_count == 0 and nice_kids > nice_gifts:
    print("Santa ran out of presents!")
    
for row in neighborhood:
    print(*row, sep=" ")

if nice_gifts == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_gifts} nice kid/s.")
