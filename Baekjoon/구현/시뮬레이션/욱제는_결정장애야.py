import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
menus = list(input().split())

max_cnt = 0
sticker = Counter()
for menu in menus:
    if menu not in sticker:
        sticker[menu] += 1
        max_cnt = max(max_cnt, len(sticker))
    else:
        del sticker[menu]

print(max_cnt)