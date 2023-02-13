def position_change(start_position, direction):

    if direction == 'up':
        start_position[0] -= 1
        if start_position[0] < 0:
            start_position[0] = number_of_rows - 1

    elif direction == 'down':
        start_position[0] += 1
        if start_position[0] == number_of_rows:
            start_position[0] = 0

    elif direction == 'left':
        start_position[1] -= 1
        if start_position[1] < 0:
            start_position[1] = number_of_columns - 1
    elif direction == 'right':
        start_position[1] += 1
        if start_position[1] == number_of_columns:
            start_position[1] = 0

    return start_position


number_of_rows, number_of_columns = map(int, input().split(", "))

santa_workshop = list()
your_position = list()

items_to_collect = 0
all_items_collected = False
decorations = 0
gifts = 0
cookies = 0

for row in range(number_of_rows):
    current_row = input().split()
    if "Y" in current_row:
        your_position = [row, current_row.index("Y")]
    for item in current_row:
        if item in ["D", "G", "C"]:
            items_to_collect += 1
    santa_workshop.append(current_row)

command = input()

while command != "End":

    to_go, steps = command.split("-")

    for _ in range(int(steps)):
        santa_workshop[your_position[0]][your_position[1]] = "x"
        new_position = position_change(your_position, to_go)

        if santa_workshop[new_position[0]][new_position[1]] == "D":
            decorations += 1
            items_to_collect -= 1
        elif santa_workshop[new_position[0]][new_position[1]] == "C":
            cookies += 1
            items_to_collect -= 1
        elif santa_workshop[new_position[0]][new_position[1]] == "G":
            gifts += 1
            items_to_collect -= 1
        your_position = new_position
        santa_workshop[your_position[0]][your_position[1]] = "Y"

        if items_to_collect == 0:
            print("Merry Christmas!")
            all_items_collected = True
            break
    if all_items_collected:
        break

    command = input()

print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

for row in santa_workshop:
    print(" ".join(row))
