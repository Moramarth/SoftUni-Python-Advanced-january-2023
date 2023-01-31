number_of_rows = int(input())

current_matrix = [list(map(int, input().split())) for _ in range(number_of_rows)]

primary_diagonal_sum = 0

for row in range(number_of_rows):
    primary_diagonal_sum += current_matrix[row][row]

print(primary_diagonal_sum)
