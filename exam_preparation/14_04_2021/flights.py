def flights(*args):
    flights_to_process = {}
    for i in range(0, len(args), 2):
        if args[i] == "Finish":
            break
        if args[i] not in flights_to_process:
            flights_to_process[args[i]] = 0
        flights_to_process[args[i]] += args[i + 1]
    return flights_to_process
