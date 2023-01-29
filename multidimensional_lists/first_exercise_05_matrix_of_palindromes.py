number_of_rows, number_of_columns = input().split()

matrix = list()

for row in range(int(number_of_rows)):
    matrix.append([])
    for column in range(int(number_of_columns)):
        current_palindrome = chr(row + 97) + chr(row + column + 97) + chr(row + 97)
        matrix[row].append(current_palindrome)

for element in matrix:
    print(*element, sep=" ")
