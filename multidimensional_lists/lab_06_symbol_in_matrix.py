number_of_rows_and_columns = int(input())

matrix_to_search = [list(input()) for _ in range(number_of_rows_and_columns)]

symbol_to_find = input()
symbol_found = False
for row_index in range(number_of_rows_and_columns):
    for column_index in range(number_of_rows_and_columns):
        if symbol_to_find == matrix_to_search[row_index][column_index]:
            print(f"({row_index}, {column_index})")
            symbol_found = True
            break
    if symbol_found:
        break
else:
    print(f"{symbol_to_find} does not occur in the matrix")
