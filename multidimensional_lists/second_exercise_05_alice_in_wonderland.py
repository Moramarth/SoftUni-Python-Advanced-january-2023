square_size = int(input())

wonderland = list()
alice = list()
tea_quantity = 0

for row in range(square_size):
    current_row = [int(x) if x.isdigit() else x for x in input().split()]
    wonderland.append(current_row)

    if "A" in current_row:
        alice = [row, current_row.index("A")]
        current_row[alice[1]] = "*"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()

while command:
    r, c = directions[command][0] + alice[0], directions[command][1] + alice[1]
    if not (0 <= r < square_size and 0 <= c < square_size):
        print("Alice didn't make it to the tea party.")
        break
    elif wonderland[r][c] == "R":
        wonderland[r][c] = "*"
        print("Alice didn't make it to the tea party.")
        break

    if type(wonderland[r][c]) is int:
        tea_quantity += wonderland[r][c]

    alice = [r, c]
    wonderland[r][c] = "*"
    if tea_quantity >= 10:
        print("She did it! She went to the party.")
        break
    command = input()


for row in wonderland:
    print(*row, sep=" ")
