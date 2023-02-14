from collections import deque


def craft_test(number):
    if number < 100:
        pass

    elif number < 200:
        wedding_gifts["Gemstone"] += 1
        crafted_set.add("Gemstone")

    elif number < 300:
        wedding_gifts["Porcelain Sculpture"] += 1
        crafted_set.add("Porcelain Sculpture")

    elif number < 400:
        wedding_gifts["Gold"] += 1
        crafted_set.add("Gold")

    elif number < 500:
        wedding_gifts["Diamond Jewellery"] += 1
        crafted_set.add("Diamond Jewellery")


materials = deque(map(int, input().split()))
genie_magic = deque(map(int, input().split()))

wedding_gifts = {
    "Gemstone":	0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}
crafted_set = set()

while materials and genie_magic:
    tool_kit = materials.pop()
    magic = genie_magic.popleft()
    mixture = tool_kit + magic

    if mixture < 100:
        if mixture % 2 == 0:
            tool_kit *= 2
            magic *= 3
            mixture = tool_kit + magic
        else:
            mixture *= 2
        craft_test(mixture)
        continue

    elif mixture < 500:
        craft_test(mixture)

    else:
        mixture /= 2
        craft_test(mixture)

if {"Gemstone", "Porcelain Sculpture"}.issubset(crafted_set) or {"Gold", "Diamond Jewellery"}.issubset(crafted_set):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(material) for material in materials)}")

if genie_magic:
    print(f"Magic left: {', '.join(str(magic) for magic in genie_magic)}")

if crafted_set:
    for item in sorted(crafted_set):
        print(f"{item}: {wedding_gifts[item]}")
