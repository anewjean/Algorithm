# 거스름돈이 n 인 경우, 2원, 5원으로 n원을 만들 수 있는 '최소 동전'의 개수가 몇 개인가
# 기존 값과 현재 동전 n개로 i를 만들 수 있다면 dp 갱신
# 큰 금액을 먼저 써야 동전 개수를 최소로 만들 수 있음

import sys
input = sys.stdin.readline

money = int(input())
coin_count = 0

while money >= 0:
    if money % 5 == 0:
        coin_count += money // 5
        print(coin_count)
        break
    money -= 2
    coin_count += 1
else:
    print(-1)