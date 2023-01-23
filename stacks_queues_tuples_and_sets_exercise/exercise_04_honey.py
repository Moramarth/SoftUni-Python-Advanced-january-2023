from _collections import deque

working_bees = deque([int(bee) for bee in input().split()])
nectar = deque([int(x) for x in input().split()])
honey_making = deque(input().split())
honey_processing = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}
total_honey = 0
while working_bees and nectar:

    bee = working_bees.popleft()
    nectar_amount = nectar.pop()

    if nectar_amount < bee:
        working_bees.appendleft(bee)
    else:
        symbol = honey_making.popleft()
        if symbol == "/" and (nectar == 0 or bee == 0):
            continue
        total_honey += abs(honey_processing[symbol](bee, nectar_amount))


print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(bee) for bee in working_bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(nectar_amount) for nectar_amount in nectar)}")
