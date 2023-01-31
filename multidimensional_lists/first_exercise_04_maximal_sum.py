from sys import maxsize

number_of_rows, number_of_columns = map(int, input().split())

initial_matrix = [list(map(int, input().split())) for _ in range(number_of_rows)]

max_sum = -maxsize
sub_matrix = []


for row in range(number_of_rows - 2):
    for column in range(number_of_columns - 2):

        first_row = initial_matrix[row][column:column + 3]
        second_row = initial_matrix[row + 1][column:column + 3]
        third_row = initial_matrix[row + 2][column:column + 3]

        matrix_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if matrix_sum > max_sum:
            max_sum = matrix_sum
            sub_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
if sub_matrix:
    for element in sub_matrix:
        print(*element, sep=" ")
