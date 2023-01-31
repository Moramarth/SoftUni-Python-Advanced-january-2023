number_of_rows, number_of_columns = map(int, input().split())

initial_matrix = [list(input().split()) for _ in range(number_of_rows)]

sub_matrix_count = 0

for row in range(number_of_rows - 1):
    for column in range(number_of_columns - 1):
        first_row = (initial_matrix[row][column], initial_matrix[row][column + 1])
        second_row = (initial_matrix[row + 1][column], initial_matrix[row + 1][column + 1])
        if first_row[0] == first_row[1] and second_row[0] == second_row[1] and first_row == second_row:
            sub_matrix_count += 1

print(sub_matrix_count)
