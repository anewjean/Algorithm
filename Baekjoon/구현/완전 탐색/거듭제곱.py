N = int(input())

answer = 0
power = 1
while (N > 0):
    if (N & 1): # N의 마지막 비트가 1이면
        answer += power
    N >>= 1 # N을 오른쪽으로 1비트 이동 (n =/ 2)
    power *= 3

print(answer)