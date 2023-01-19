def shooting_func(shots, locks):
    bullet = shots.pop()  # every bullet is removed
    lock = locks[-1]

    if bullet <= lock:
        print("Bang!")
        locks.pop()  # only opened locks are removed
    else:
        print("Ping!")


def reload_func(bullets_count):
    available_bullets = len(bullets_count)
    print("Reloading!")
    if available_bullets >= drum_chambers:
        new_drum = drum_chambers
    else:
        new_drum = available_bullets
    return new_drum


bullet_price = int(input())
drum_chambers = int(input())

# using bullets as a stack back to front
bullets = list(map(int, input().split()))
safe_locks = list(map(int, input().split()))
intelligence_value = int(input())

# reversing locks so we can use it as a stack and still go front to back
safe_locks.reverse()
current_drum = drum_chambers
total_bullets = len(bullets)

while bullets and safe_locks:
    if current_drum > 0:
        shooting_func(bullets, safe_locks)
        current_drum -= 1

    # using second condition with "if" instead of "else" in the previous one
    #  we reload even if  all locks are opened
    if current_drum == 0:
        if bullets:
            current_drum = reload_func(bullets)

shots_fired = total_bullets - len(bullets)
money_earned = intelligence_value - (shots_fired * bullet_price)

if not safe_locks:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(safe_locks)}")
