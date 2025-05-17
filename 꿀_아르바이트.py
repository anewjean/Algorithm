n, m = map(int, input().strip().split())
T = list(map(int, input().split()))

curr_sum = sum(T[0:m])
answer = curr_sum
for i in range(m, n):
    curr_sum = curr_sum - T[i-m] + T[i]
    answer = max(answer, curr_sum)

print(answer)