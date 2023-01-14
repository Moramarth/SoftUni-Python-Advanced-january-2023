from _collections import deque

gas_station_count = int(input())

fuel = list()
kilometers = list()

for gas_station in range(gas_station_count):
    available_fuel, distance_to_cover = input().split()
    fuel.append(int(available_fuel))
    kilometers.append(int(distance_to_cover))

tank = 0
distance_driven = 0
starting_station = 0
circle_passed = False

circle_road = deque(kilometers)
pump_storage = deque(fuel)
while True:
    for i in range(len(circle_road)):
        tank += pump_storage[i]
        if tank < circle_road[i]:
            break
        tank -= circle_road[i]
        distance_driven += circle_road[i]
        if distance_driven >= sum(kilometers):
            circle_passed = True
            break
    if not circle_passed:
        unsuccessful_station = circle_road.popleft()
        circle_road.append(unsuccessful_station)
        pump_in_line = pump_storage.popleft()
        pump_storage.append(pump_in_line)
        tank = 0
        distance_driven = 0
        starting_station += 1
    else:
        break

print(starting_station)
