n = int(input())
prices = sorted(map(int, input().split()))

page = 1
curr_min = prices[0]

for price in prices[1:]:
    if price >= curr_min * 2:  # 새 그룹 필요
        page += 1
        curr_min = price       # 새 그룹 시작 → 최소값 초기화

print(page)