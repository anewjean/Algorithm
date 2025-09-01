N = int(input())
nums = list(map(int, input().split()))
M = int(input())
ms = map(int, input().split())

def is_in_nums(m):
    if m in nums:
        return 1
    else:
        return 0

for m in ms:
    print(is_in_nums(m))
