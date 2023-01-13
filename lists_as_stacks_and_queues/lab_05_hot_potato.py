from _collections import deque

kids_in_circle = deque(input().split())

count_to_remove = int(input())

while len(kids_in_circle) > 1:
    for i in range(count_to_remove - 1):
        kids_in_circle.append(kids_in_circle.popleft())
    print(f"Removed {kids_in_circle.popleft()}")

print(f"Last is {kids_in_circle[0]}")
