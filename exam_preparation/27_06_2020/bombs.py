from collections import deque

bomb_effects = deque(map(int, input().split(", ")))
bomb_casings = deque(map(int, input().split(", ")))

recipes = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120,
}
crafted = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0,
}
while bomb_effects and bomb_casings:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()
    mix = effect + casing
    if mix in [40, 60, 120]:
        for key, value in recipes.items():
            if value == mix:
                crafted[key] += 1
    else:
        casing -= 5
        bomb_effects.appendleft(effect)
        bomb_casings.append(casing)

    if crafted["Datura Bombs"] > 2 and crafted["Cherry Bombs"] > 2 and crafted["Smoke Decoy Bombs"] > 2:
        print("Bene! You have successfully filled the bomb pouch!")
        break
else:
    print("You don't have enough materials to fill the bomb pouch.")


print(f"Bomb Effects: {', '.join(str(effect) for effect in bomb_effects) if bomb_effects else 'empty'}")
print(f"Bomb Casings: {', '.join(str(casing) for casing in bomb_casings) if bomb_casings else 'empty'}")

for key, value in crafted.items():
    print(f"{key}: {value}")
