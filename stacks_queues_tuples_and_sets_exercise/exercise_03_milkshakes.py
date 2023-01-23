from collections import deque

chocolate_stack = [int(value) for value in input().split(", ")]
milk_cups = deque([int(value) for value in input().split(", ")])

milkshakes = 0

while milkshakes < 5 and chocolate_stack and milk_cups:

    chocolate = chocolate_stack.pop()
    milk = milk_cups.popleft()

    if milk <= 0 and chocolate <= 0:
        continue
    elif milk <= 0:
        chocolate_stack.append(chocolate)
        continue
    elif chocolate <= 0:
        milk_cups.appendleft(milk)
        continue

    if milk == chocolate:
        milkshakes += 1
    else:
        chocolate -= 5
        chocolate_stack.append(chocolate)
        milk_cups.append(milk)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(chocolate) for chocolate in chocolate_stack) or 'empty'}")
print(f"Milk: {', '.join(str(milk) for milk in  milk_cups) or 'empty'}")

