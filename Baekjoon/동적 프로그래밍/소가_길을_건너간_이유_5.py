n, k, b = map(int, input().split())

brokens = [0] * n # 정상: 0, 고장: 1
for _ in range(b):
    x = int(input())
    brokens[x-1] = 1 # 0 based

pre_sum = [0] * (n+1) # i개 원소까지의 고장 개수 합 저장 배열
# pre_sum[i] = brokens[0] + brokens[1] + ... + brokens[i-1]
# pre_sum[i] = pre_sum[i-1] + brokens[i-1]
for i in range(1, n+1):
    pre_sum[i] = pre_sum[i-1] + brokens[i-1]

# j ~ k 까지의 최소 고장개수 구하기
answer = float('inf')
for j in range(n-k+1):
    curr = pre_sum[j+k] - pre_sum[j]
    answer = min(answer, curr)
    
print(answer)