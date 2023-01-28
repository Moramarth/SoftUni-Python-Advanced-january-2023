number_of_rows, number_of_columns = map(int, input().split())

square_matrix = [list(input().split()) for _ in range(number_of_rows)]

sub_matrix_count = 0

for row in range(number_of_rows):
    for column in range(number_of_columns):
        if column + 1 < number_of_columns and row + 1 < number_of_rows:
            first_row = (square_matrix[row][column], square_matrix[row][column + 1])
            second_row = (square_matrix[row + 1][column], square_matrix[row + 1][column + 1])
            if first_row[0] == first_row[1] and second_row[0] == second_row[1] and first_row == second_row:
                sub_matrix_count += 1

print(sub_matrix_count)
