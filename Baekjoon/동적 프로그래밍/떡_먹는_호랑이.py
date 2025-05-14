D, K = map(int, input().split())

# x, y는 A, B의 계수 저장 리스트
x = [0] * (D + 1)
y = [0] * (D + 1)

x[1], x[2] = 1, 0
y[1], y[2] = 0, 1
for i in range(3, D + 1):
    x[i] = x[i-2] + x[i-1]
    y[i] = y[i-2] + y[i-1]

for i in range(1, K+1):
    if (K - i * x[D]) % y[D] == 0:
        A = i
        B = (K - i * x[D]) // y[D]
        if B > 0:
            print(A, B, sep="\n")
            break