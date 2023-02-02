number_of_rows = int(input())

square_matrix = [list(map(int, input().split())) for _ in range(number_of_rows)]

command = input()

while command != "END":
    to_do, *data = command.split()
    row, column, number = [int(x) for x in data]
    if to_do == "Add":
        if 0 <= row < number_of_rows and 0 <= column < number_of_rows:
            square_matrix[row][column] += number
        else:
            print("Invalid coordinates")

    elif to_do == "Subtract":
        if 0 <= row < number_of_rows and 0 <= column < number_of_rows:
            square_matrix[row][column] -= number
        else:
            print("Invalid coordinates")

    command = input()

for row in range(number_of_rows):
    print(*square_matrix[row], sep=" ")
