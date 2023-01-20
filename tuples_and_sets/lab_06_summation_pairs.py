""" 
Task not included in the judge system.

On the first line, you will receive a sequence of numbers separated by space. 
On the second line, you'll receive a target number. 
Your task is to find the pairs of numbers whose sum equals the target number.
For each found pair print "{number} + {number} = {target_number}". 
You may NOT use the same element twice to fulfill the condition above.
Can you come up with an algorithm that has less time complexity?


Test input:
1 5 4 2 2 3 1 3 2
4

Expected output:
1 + 3 = 4
1 + 3 = 4
2 + 2 = 4


Test input 2:
11 8 5 6 9 2 9 7 3 4
11

Expected output 2:
8 + 3 = 11
5 + 6 = 11
9 + 2 = 11
7 + 4 = 11

"""

numbers = list(map(int, input().split()))
target = int(input())

targets = set()
value_map = dict()

for number in numbers:
    if number in targets:
        targets.remove(number)
        pair = value_map[number]
        del value_map[number]
        print(f"{pair} + {number} = {target}")
    else:
        result = target - number
        targets.add(result)
        value_map[result] = number
