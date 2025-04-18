# 최대값 만들기
# 짝수개라면 모두 1로 채우고
# 홀수개면 7 하나 넣고 나머지는 1로 채운다.

# 최소값 만들기
# 자릿수가 적을수록 숫자가 작아 → 숫자를 최대한 자릿수 늘리되, 자릿수마다 가장 작은 숫자를 사용해야 해.

match_count = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# 최소값을 위한 dp 초기화
dp = [''] * 101
dp[2] = '1'
dp[3] = '7'
dp[4] = '4'
dp[5] = '2'
dp[6] = '6'
dp[7] = '8'

for i in range(8, 101):
    min_val = None
    for digit, cost in match_count.items():
        if i - cost < 2:
            continue
        if dp[i - cost] == '':
            continue
        cand = dp[i - cost] + str(digit)

        # 가장 작은 수를 만들기 위해 → 정렬 기준: 앞자리가 작은 숫자가 먼저
        # 단, '0'이 앞에 오면 안 되므로, 자리 비교만으로 판별
        cand = ''.join(sorted(cand))

        if cand[0] == '0':
            # 앞에 0이 오면 그 0 다음 작은 수와 swap
            for j in range(1, len(cand)):
                if cand[j] != '0':
                    cand = cand[j] + cand[:j] + cand[j+1:]
                    break

        if min_val is None or int(cand) < int(min_val):
            min_val = cand
    dp[i] = min_val

T = int(input())
for _ in range(T):
    N = int(input())

    # 최소
    print(dp[N], end=' ')

    # 최대
    if N % 2 == 0:
        print('1' * (N // 2))
    else:
        print('7' + '1' * ((N - 3) // 2))

