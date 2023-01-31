number_of_rows = int(input())

square_matrix = [list(map(int, input().split(", "))) for _ in range(number_of_rows)]

negative_diagonal_numbers = list()
positive_diagonal_numbers = list()

for row in range(number_of_rows):
    negative_diagonal_numbers.append(square_matrix[row][row])
    positive_diagonal_numbers.append(square_matrix[row][number_of_rows - row - 1])

negative_diagonal_sum = sum(negative_diagonal_numbers)
positive_diagonal_sum = sum(positive_diagonal_numbers)

negative_diagonal_numbers = list(map(str, negative_diagonal_numbers))
positive_diagonal_numbers = list(map(str, positive_diagonal_numbers))

print(f"Primary diagonal: {', '.join(negative_diagonal_numbers)}. Sum: {negative_diagonal_sum}")
print(f"Secondary diagonal: {', '.join(positive_diagonal_numbers)}. Sum: {positive_diagonal_sum}")
