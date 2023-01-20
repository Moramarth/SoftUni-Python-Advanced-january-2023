number_of_students = int(input())

students_names = dict()

for student in range(number_of_students):
    name, grade = input().split()
    if name not in students_names:
        students_names[name] = []
    students_names[name].append(float(grade))

for name, grades in students_names.items():
    print(f"{name} -> {' '.join(list(map(lambda x: f'{x:.2f}', grades)))}"
          f" (avg: {sum(grades)/ len(grades):.2f})")
