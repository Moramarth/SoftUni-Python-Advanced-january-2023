def numbers_searching(*args):
    result = list()
    sequence_start = min(args)
    sequence_end = max(args)

    sequence = [number for number in range(sequence_start, sequence_end + 1)]

    missing_number = [integer for integer in sequence if integer not in args]
    result.append(missing_number[0])
    duplicates = list()
    for i in range(len(args)):
        if args[i] not in duplicates and args.count(args[i]) > 1:
            duplicates.append(args[i])
    result.append(sorted(duplicates))

    return result
