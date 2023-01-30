initial_matrix = [element.split() for element in input().split("|")]

flattened_list = list()

for index in range(len(initial_matrix) - 1, -1, -1):
    for element in initial_matrix[index]:
        flattened_list.append(element)

print(" ".join(flattened_list))