from collections import deque


def hot_chocolate(worker, mats):
    materials.append(mats)
    worker *= 2
    elf_energy.append(worker)


elf_energy = deque(map(int, input().split(" ")))
materials = deque(map(int, input().split(" ")))

energy_used = 0
crafted_toys = 0
turns = 0
while elf_energy and materials:
    elf = elf_energy.popleft()
    if elf < 5:
        continue

    tool_box = materials.pop()
    turns += 1
    if turns % 3 == 0:
        if elf < tool_box * 2:
            hot_chocolate(elf, tool_box)
            continue
        else:
            elf -= 2 * tool_box
            crafted_toys += 2
            elf += 1
            energy_used += 2 * tool_box
            if turns % 5 == 0:
                crafted_toys -= 2
                elf -= 1
                elf_energy.append(elf)
                continue
        elf_energy.append(elf)
        continue
    if turns % 5 == 0:
        if elf < tool_box:
            hot_chocolate(elf, tool_box)
            continue
        else:
            elf -= tool_box
            energy_used += tool_box
        elf_energy.append(elf)
        continue

    if elf < tool_box:
        hot_chocolate(elf,tool_box)
        continue
    else:
        elf -= tool_box
        crafted_toys += 1
        elf += 1
        energy_used += tool_box
    elf_energy.append(elf)

print(f"Toys: {crafted_toys}")
print(f"Energy: {energy_used}")

if elf_energy:
    print(f"Elves left: {', '.join(str(elf) for elf in elf_energy)}")
if materials:
    print(f"Boxes left: {', '.join(str(tool_box) for tool_box in materials)}")
