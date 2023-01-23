number_of_rows = int(input())

current_matrix = [list(map(int, input().split(", "))) for _ in range(number_of_rows)]

even_matrix = [[number for number in element if number % 2 == 0] for element in current_matrix]

print(even_matrix)
