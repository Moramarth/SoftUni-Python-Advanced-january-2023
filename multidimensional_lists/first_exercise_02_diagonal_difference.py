number_of_rows = int(input())

square_matrix = [list(map(int, input().split())) for _ in range(number_of_rows)]

negative_diagonal_numbers = list()
positive_diagonal_numbers = list()

diagonal_index = 0

for element in square_matrix:
    for index in range(len(element)):
        if index == diagonal_index:
            negative_diagonal_numbers.append(element[index])
            diagonal_index += 1
            break

diagonal_index = len(square_matrix[0]) - 1
for element in square_matrix:
    for index in range(len(element) - 1, -1, -1):
        if index == diagonal_index:
            positive_diagonal_numbers.append(element[index])
            diagonal_index -= 1
            break

negative_diagonal_sum = sum(negative_diagonal_numbers)
positive_diagonal_sum = sum(positive_diagonal_numbers)

print(abs(negative_diagonal_sum - positive_diagonal_sum))
