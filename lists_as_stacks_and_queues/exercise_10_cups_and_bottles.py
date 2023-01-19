def filling_water_func(cups, bottles):
    cup_capacity = cups[-1]
    current_bottle = bottles.pop()  # we remove the bottle even if there is water left in it
    if cup_capacity <= current_bottle:
        cups.pop()
        waste = current_bottle - cup_capacity
        return waste
    else:
        cup_capacity -= current_bottle
        cups[-1] = cup_capacity
        return 0


cups_capacity = list(map(int, input().split()))
water_bottles = list(map(int, input().split()))

wasted_water = 0
cups_capacity.reverse()  # stacking cups from front to back


while cups_capacity and water_bottles:
    wasted_water += filling_water_func(cups_capacity, water_bottles)

result = list()

if not cups_capacity:
    for bottle in range(len(water_bottles)):
        result.append(str(water_bottles.pop()))
    print(f"Bottles: {' '.join(result)}")
else:
    for cup in range(len(cups_capacity)):
        result.append(str(cups_capacity.pop()))
    print(f"Cups: {' '.join(result)}")

# we always waste some water by default
print(f"Wasted litters of water: {wasted_water}")
