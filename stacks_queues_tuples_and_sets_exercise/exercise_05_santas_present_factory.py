from _collections import deque

materials = deque((int(material) for material in input().split()))
magic_levels = deque((int(magic) for magic in input().split()))

crafting_recipes = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}
crafted_items = list()

while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[-1] else 0
    magic = magic_levels.popleft() if material or not magic_levels[0] else 0

    if not magic:
        continue

    product = material * magic
    if product in crafting_recipes:
        crafted_items.append(crafting_recipes[product])
    elif product < 0:
        new_material = material + magic
        materials.append(new_material)
    elif product > 0:
        materials.append(material + 15)

if {"Teddy bear", "Bicycle"}.issubset(crafted_items) or {"Doll", "Wooden train"}.issubset(crafted_items):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")


if materials:
    materials.reverse()
    print(f"Materials left: {', '.join(str(material) for material in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(magic) for magic in magic_levels)}")

total_toys = dict()
for toy in sorted(crafted_items):
    if toy not in total_toys:
        total_toys[toy] = 0
    total_toys[toy] += 1

for toy, amount in total_toys.items():
    print(f"{toy}: {amount}")
