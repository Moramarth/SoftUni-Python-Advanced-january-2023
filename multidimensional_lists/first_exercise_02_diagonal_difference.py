number_of_rows = int(input())

square_matrix = [list(map(int, input().split())) for _ in range(number_of_rows)]

negative_diagonal_sum = 0
positive_diagonal_sum = 0

for row in range(number_of_rows):
    negative_diagonal_sum += square_matrix[row][row]
    positive_diagonal_sum += square_matrix[row][number_of_rows - row - 1]


print(abs(negative_diagonal_sum - positive_diagonal_sum))
