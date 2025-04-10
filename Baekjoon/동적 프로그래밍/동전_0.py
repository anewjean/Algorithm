# 1. 동전리스트 내림차순 정렬
# 2. K보다 작거나 같은 금액을 최대한 사용
# 3. K에서 사용한 만큼빼고 동전 개수 누적
# 4. K가 0이 될 때까지 반복

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True) # 내림차순 정렬 -> 큰 금액부터 탐색

count = 0
for coin in coins:
    if K > coin:
        count += K // coin
        K %= coin

print(count)