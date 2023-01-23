number_of_rows = int(input())

current_matrix = [list(map(int, input().split(", "))) for _ in range(number_of_rows)]

flattened_matrix = list()

for element in current_matrix:
    flattened_matrix.extend(element)

print(flattened_matrix)
