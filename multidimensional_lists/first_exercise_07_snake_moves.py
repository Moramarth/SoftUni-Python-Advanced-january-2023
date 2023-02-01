from _collections import deque

number_of_rows, number_of_columns = map(int, input().split())
our_snake = list(input())

snake_path = deque(our_snake)

for row in range(number_of_rows):
    while len(snake_path) < number_of_columns:
        snake_path.extend(our_snake)

    if row % 2 == 0:
        print(*[snake_path.popleft() for _ in range(number_of_columns)], sep="")
    else:
        print(*[snake_path.popleft() for _ in range(number_of_columns)][::-1], sep="")
