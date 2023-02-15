def best_list_pureness(list_to_process, count):
    best_pureness = -2147483647
    rotation_number = ""

    for i in range(count + 1):
        pureness = 0
        for j in range(len(list_to_process)):
            pureness += list_to_process[j] * j

        if pureness > best_pureness:
            best_pureness = pureness
            rotation_number = i

        list_to_process.insert(0, list_to_process.pop())

    return f"Best pureness {best_pureness} after {rotation_number} rotations"
