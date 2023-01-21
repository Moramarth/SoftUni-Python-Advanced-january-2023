usernames_count = int(input())

usernames = set(input() for _ in range(usernames_count))

print(*usernames, sep="\n")