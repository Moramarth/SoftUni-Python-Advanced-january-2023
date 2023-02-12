from collections import deque

caffeine_doses = list(map(int, input().split(", ")))
energy_drinks = deque(list(map(int, input().split(", "))))

caffeine_taken = 0

while caffeine_doses and energy_drinks:
    dose = caffeine_doses.pop()
    drink = energy_drinks.popleft()
    caffeine = dose * drink
    if caffeine_taken + caffeine > 300:
        energy_drinks.append(drink)
        caffeine_taken = caffeine_taken - 30 if caffeine_taken - 30 > 0 else 0
    else:
        caffeine_taken += caffeine

if energy_drinks:
    print(f"Drinks left: {', '.join(list(map(str,energy_drinks)))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_taken} mg caffeine.")
