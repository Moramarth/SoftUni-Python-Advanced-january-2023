number_of_lines = int(input())

intersection = set()

for _ in range(number_of_lines):
    first_range, second_range = input().split("-")

    first_set = set(range(int(first_range.split(",")[0]), int(first_range.split(",")[1]) + 1))
    second_set = set(range(int(second_range.split(",")[0]), int(second_range.split(",")[1]) + 1))

    current_overlap = first_set.intersection(second_set)
    if len(current_overlap) > len(intersection):
        intersection = current_overlap

print(f"Longest intersection is [{', '.join(str(n) for n in intersection)}] with length {len(intersection)}")
