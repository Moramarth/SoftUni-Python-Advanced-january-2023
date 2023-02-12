from collections import deque

eggs = deque(map(int, input().split(", ")))
paper = deque(map(int, input().split(", ")))
box_size = 50
filled_boxes = 0

while eggs and paper:
    current_egg = eggs.popleft()
    if current_egg <= 0:
        continue
    if current_egg == 13:
        paper[0], paper[-1] = paper[-1], paper[0]
        continue
    current_paper = paper.pop()
    if current_paper + current_egg <= box_size:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(egg) for egg in eggs)}")
if paper:
    print(f"Pieces of paper left: {', '.join(str(sheet) for sheet in paper)}")
