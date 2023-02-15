from collections import deque

firework_effects = deque(map(int, input().split(",")))
explosive_power = deque(map(int, input().split(",")))

fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}

while firework_effects and explosive_power:
    effect = firework_effects.popleft() if explosive_power[-1] > 0 or firework_effects[0] <= 0 else 0
    explosive = explosive_power.pop() if effect > 0 or explosive_power[-1] <= 0 else 0

    if explosive <= 0:
        continue

    materials = effect + explosive

    if materials % 3 == 0 and not materials % 5 == 0:
        fireworks["Palm Fireworks"] += 1
    elif materials % 5 == 0 and not materials % 3 == 0:
        fireworks["Willow Fireworks"] += 1
    elif materials % 3 == 0 and materials % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
    else:
        effect -= 1
        firework_effects.append(effect)
        explosive_power.append(explosive)
    if len([value for value in fireworks.values() if value >= 3]) == len(fireworks):
        print("Congrats! You made the perfect firework show!")
        break
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(effect) for effect in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(explosive) for explosive in explosive_power)}")

for key, value in fireworks.items():
    print(f"{key}: {value}")
