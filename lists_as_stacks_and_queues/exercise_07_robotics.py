from _collections import deque
from datetime import datetime, timedelta

data = input().split(";")
robots_names = dict()
for robot in data:
    name, processing_time = robot.split("-")
    robots_names[name] = [processing_time, 0]

time_stamp = datetime.strptime(input(), "%H:%M:%S")


unprocessed_products = deque()

product = input()

while product != "End":
    unprocessed_products.append(product)
    product = input()


while unprocessed_products:
    time_stamp += timedelta(0, 1)
    product = unprocessed_products.popleft()
    for robot in robots_names:
        current_timer = int(robots_names[robot][1])
        if current_timer != 0:
            current_timer -= 1
            robots_names[robot][1] = current_timer
    free_robots = list()
    for robot in robots_names:
        if int(robots_names[robot][1]) == 0:
            free_robots.append(robot)

    if not free_robots:
        unprocessed_products.append(product)
        continue

    robots_names[free_robots[0]][1] = robots_names[free_robots[0]][0]
    print(f"{free_robots[0]} - {product} [{time_stamp.strftime('%H:%M:%S')}]")
