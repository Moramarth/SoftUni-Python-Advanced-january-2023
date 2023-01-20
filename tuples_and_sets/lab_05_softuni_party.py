number_of_guests = int(input())

reservations = set(input() for _ in range(number_of_guests))

while True:
    arriving_guest = input()
    if arriving_guest == "END":
        break
    reservations.discard(arriving_guest)

print(len(reservations))
print(*sorted(reservations), sep="\n")
