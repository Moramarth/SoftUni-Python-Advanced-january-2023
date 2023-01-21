number_of_lines = int(input())

unique_items = list()

for _ in range(number_of_lines):
    data = input().split()
    unique_items.extend(data)

print(*set(unique_items), sep="\n")
