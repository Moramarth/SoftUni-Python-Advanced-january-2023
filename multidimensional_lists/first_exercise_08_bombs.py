number_of_rows = int(input())

square_matrix = [list(map(int, input().split())) for _ in range(number_of_rows)]
coordinates = ((int(x) for x in coordinate.split(","))for coordinate in input().split())

alive_cells = list()

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "top-left": (-1, -1),
    "top-right": (-1, 1),
    "bottom-left": (1, -1),
    "bottom-right": (1, 1),
    "bomb-position": (0, 0),
}

for row, column in coordinates:
    if square_matrix[row][column] <= 0:
        continue
    for new_row, new_column in directions.values():
        exploding_row, exploding_column = row + new_row, column + new_column
        if (0 <= exploding_row < number_of_rows) and (0 <= exploding_column < number_of_rows) and\
                square_matrix[exploding_row][exploding_column] > 0:
            square_matrix[exploding_row][exploding_column] -= square_matrix[row][column]

for row in square_matrix:
    for element in row:
        if element > 0:
            alive_cells.append(element)

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for row in square_matrix:
    print(*row, sep=" ")
