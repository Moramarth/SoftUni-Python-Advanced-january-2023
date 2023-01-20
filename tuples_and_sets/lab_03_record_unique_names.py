number_of_names = int(input())

set_of_names = set(input() for _ in range(number_of_names))

print(*set_of_names, sep="\n")

# one line solution:
# print(*{input() for name in range(int(input()))}, sep="\n")
