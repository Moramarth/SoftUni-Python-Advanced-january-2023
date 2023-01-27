number_of_rows, number_of_columns = map(int, input().split(", "))

initial_matrix = [list(map(int, input().split(", "))) for _ in range(number_of_rows)]

max_sum = 0
sub_matrix = []


for row in range(number_of_rows):
    for column in range(number_of_columns):
        if column + 1 < number_of_columns and row + 1 < number_of_rows:
            row_sum = initial_matrix[row][column] + initial_matrix[row][column + 1]
            matrix_sum = row_sum + initial_matrix[row + 1][column] + initial_matrix[row + 1][column + 1]
            if matrix_sum > max_sum:
                max_sum = matrix_sum
                sub_matrix = [[initial_matrix[row][column], initial_matrix[row][column + 1]],
                [initial_matrix[row + 1][column], initial_matrix[row + 1][column + 1]]]

for element in sub_matrix:
    print(*element, sep=" ")
print(max_sum)
