from collections import deque

male_specimens = deque(map(int, input().split(" ")))
female_specimens = deque(map(int, input().split(" ")))
matches = 0

while male_specimens and female_specimens:
    male = male_specimens.pop() if female_specimens[0] > 0 or male_specimens[-1] <= 0 else 0
    female = female_specimens.popleft() if male > 0 or female_specimens[0] <= 0 else 0

    if female <= 0:
        continue

    if male % 25 == 0:
        male_specimens.pop()
        female_specimens.appendleft(female)
        continue
    if female % 25 == 0:
        female_specimens.pop()
        male_specimens.append(male)
        continue

    if male == female:
        matches += 1
    else:
        male -= 2
        male_specimens.append(male)

print(f"Matches: {matches}")

if male_specimens:
    print(f"Males left: {', '.join(str(male) for male in reversed(male_specimens))}")
else:
    print(f"Males left: none")

if female_specimens:
    print(f"Females left: {', '.join(str(female) for female in female_specimens)}")
else:
    print(f"Females left: none")
