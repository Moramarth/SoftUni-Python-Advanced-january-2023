random_string = input().split()

colors = ["red", "yellow", "blue", "orange", "purple", "green"]
colors_to_be_made = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"blue", "yellow"}
}

colors_found = list()

while random_string:
    first_substring = random_string.pop(0)
    second_substring = random_string.pop() if random_string else ""
    for color in (first_substring + second_substring, second_substring + first_substring):
        if color in colors:
            colors_found.append(color)
            break
    else:
        for substring in (first_substring[:-1], second_substring[:-1]):
            if substring:
                random_string.insert(len(random_string)//2, substring)

for color in set(colors_to_be_made.keys()).intersection(colors_found):
    if not colors_to_be_made[color].issubset(colors_found):
        colors_found.remove(color)

print(colors_found)
