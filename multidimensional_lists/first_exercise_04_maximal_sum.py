from sys import maxsize

number_of_rows, number_of_columns = map(int, input().split())

initial_matrix = [list(map(int, input().split())) for _ in range(number_of_rows)]

max_sum = -maxsize
sub_matrix = []


for row in range(number_of_rows):
    for column in range(number_of_columns):
        if column + 2 < number_of_columns and row + 2 < number_of_rows:
            first_row = [
                initial_matrix[row][column],
                initial_matrix[row][column + 1],
                initial_matrix[row][column + 2]
            ]

            second_row = [
                initial_matrix[row + 1][column],
                initial_matrix[row + 1][column + 1],
                initial_matrix[row + 1][column + 2]
            ]

            third_row = [
                initial_matrix[row + 2][column],
                initial_matrix[row + 2][column + 1],
                initial_matrix[row + 2][column + 2]
            ]
            matrix_sum = sum(first_row) + sum(second_row) + sum(third_row)
            if matrix_sum > max_sum:
                max_sum = matrix_sum
                sub_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
if sub_matrix:
    for element in sub_matrix:
        print(*element, sep=" ")
