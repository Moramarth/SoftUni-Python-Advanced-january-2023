from collections import deque

jobs_for_cpu = list(map(int, input().split(", ")))

index = int(input())
clock_time = 0

sorted_tasks = deque(sorted(jobs_for_cpu))

while True:
    cycle = sorted_tasks.popleft()
    clock_time += cycle
    index_current = jobs_for_cpu.index(cycle)
    jobs_for_cpu[index_current] = "done"
    if jobs_for_cpu[index] == "done":
        break

print(clock_time)
