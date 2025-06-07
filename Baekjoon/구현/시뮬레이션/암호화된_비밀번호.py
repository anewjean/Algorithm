from collections import Counter

def is_origin_to_encrypted(origin: str, encrypted: str) -> bool:
    window_size = len(origin)
    origin_counter = Counter(origin)
    window_counter = Counter(encrypted[:window_size])
    if window_counter == origin_counter:
        return True

    for i in range(window_size, len(encrypted)):
        start_char = encrypted[i-window_size]
        end_char = encrypted[i]

        window_counter[start_char] -= 1
        if window_counter[start_char] == 0:
            del window_counter[start_char]
        window_counter[start_char] += 1
    
        if window_counter == origin_counter:
            return True
    return False

N = int(input())
for _ in range(N):
    encrypted = input().strip()
    origin = input().strip()
    if is_origin_to_encrypted(origin, encrypted):
        print("YES")
    else:
        print("NO")

from collections import Counter

def is_origin_to_encrypted(origin, encrypted):
    window_size = len(origin)
    origin_counter = Counter(origin)

    window_counter = Counter(encrypted[:window_size])
    if window_counter == origin_counter:
        return True

    for i in range(window_size, len(encrypted)):
        start_char = encrypted[i - window_size]
        end_char = encrypted[i]

        window_counter[start_char] -= 1
        if window_counter[start_char] == 0:
            del window_counter[start_char]
        window_counter[end_char] += 1

        if window_counter == origin_counter:
            return True

    return False

N = int(input())
for _ in range(N):
    encrypted = input().strip()
    origin = input().strip()
    if is_origin_to_encrypted(origin, encrypted):
        print("YES")
    else:
        print("NO")
