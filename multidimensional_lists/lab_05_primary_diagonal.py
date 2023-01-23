number_of_rows = int(input())

current_matrix = [list(map(int, input().split())) for _ in range(number_of_rows)]

primary_diagonal_sum = 0

diagonal_index = 0

for element in current_matrix:
    for index in range(len(element)):
        if index == diagonal_index:
            primary_diagonal_sum += element[index]
            diagonal_index += 1
            break
print(primary_diagonal_sum)
