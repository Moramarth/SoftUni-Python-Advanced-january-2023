def age_assignment(*names, **letter_and_age):
    people_names = list(names)
    data_tracking = list()
    for letter, age in letter_and_age.items():
        for name in people_names:
            if name.startswith(letter):
                data_tracking.append((name, age))
                people_names.remove(name)
                break
    data_tracking = sorted(data_tracking, key=lambda x: x[0])
    person_information = [f"{name} is {age} years old." for name, age in data_tracking]

    return "\n".join(person_information)
