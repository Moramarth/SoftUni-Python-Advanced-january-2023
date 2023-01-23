rows, columns = map(int, input().split(", "))

current_matrix = []

for row in range(rows):
    data = list(map(int, input().split(", ")))
    current_matrix.append(data)

total_sum = 0

for element in current_matrix:
    total_sum += sum(element)

print(total_sum)
print(current_matrix)
