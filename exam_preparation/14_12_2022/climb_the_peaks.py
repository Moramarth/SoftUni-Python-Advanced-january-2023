from collections import deque

daily_food_supplies = deque([int(num) for num in input().split(", ")])
daily_stamina = deque([int(num) for num in input().split(", ")])

mountain_peaks = deque([("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)])
total_peaks = len(mountain_peaks)
climbed_peaks = list()

while daily_food_supplies and daily_stamina and mountain_peaks:
    power_for_the_day = daily_food_supplies.pop() + daily_stamina.popleft()
    peak, difficulty = mountain_peaks.popleft()
    if power_for_the_day >= difficulty:
        climbed_peaks.append(peak)
    else:
        mountain_peaks.appendleft((peak, difficulty))

if len(climbed_peaks) == total_peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if climbed_peaks:
    print("Conquered peaks:")
    print(*climbed_peaks, sep="\n")
