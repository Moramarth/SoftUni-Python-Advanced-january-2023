number_of_rows, number_of_columns = map(int, input().split())

initial_matrix = [input().split() for _ in range(number_of_rows)]

while True:
    command = input()
    if command.startswith("END"):
        break
    if not command.startswith("swap"):
        print("Invalid input!")
        continue

    data = command.split()
    if len(data) != 5:
        print("Invalid input!")
        continue
    first_element_row = int(data[1])
    first_element_column = int(data[2])
    second_element_row = int(data[3])
    second_element_column = int(data[4])
    if first_element_row not in range(0, number_of_rows + 1) or\
            second_element_row not in range(0, number_of_rows + 1) or\
            first_element_column not in range(0, number_of_columns + 1) or\
            second_element_column not in range(0, number_of_columns + 1):

        print("Invalid input!")
        continue

    initial_matrix[first_element_row][first_element_column],\
        initial_matrix[second_element_row][second_element_column]\
        = initial_matrix[second_element_row][second_element_column],\
        initial_matrix[first_element_row][first_element_column]

    for element in initial_matrix:
        print(*element, sep=" ")
