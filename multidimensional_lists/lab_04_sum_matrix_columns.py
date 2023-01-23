number_of_rows, number_of_columns = map(int, input().split(", "))

current_matrix = [list(map(int, input().split())) for _ in range(number_of_rows)]

column_sum = 0

for column_index in range(number_of_columns):
    for row_index in range(number_of_rows):
        column_sum += current_matrix[row_index][column_index]
    print(column_sum)
    column_sum = 0
