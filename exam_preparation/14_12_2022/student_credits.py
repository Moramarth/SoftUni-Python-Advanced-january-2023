def students_credits(*args):

    data = args
    report = dict()
    result = []
    for course in data:
        course_name, max_credits, max_test_points, points_earned = course.split("-")
        credits_earned = int(max_credits) * (int(points_earned) / int(max_test_points))
        report[course_name] = credits_earned

    total_credits_earned = sum(list(report.values()))
    if total_credits_earned >= 240:
        result.append(f"Diyan gets a diploma with {total_credits_earned:.1f} credits.")
    else:
        result.append(f"Diyan needs {(240 - total_credits_earned):.1f} credits more for a diploma.")

    for course_name, credits_earned in sorted(report.items(), key=lambda x: -x[1]):
        result.append(f"{course_name} - {credits_earned:.1f}")

    return "\n".join(result)
