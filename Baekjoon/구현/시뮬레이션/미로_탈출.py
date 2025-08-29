# 순간 이동 횟수 구하기

# 끝 -> 끝: 이동 비용 0
# S가 끝이거나 S, E가 서로 인접: 이동 비용 1
# 그 외: 이동 비용 2

def escape(n: int, s: int, e: int):
    if {s, e} == {1, n}:
        print(0)
    elif (s in (1, n)) or (abs(e - s) == 1):
        print(1)
    else:
        print(2)

n = int(input())
for _ in range(n):
    escape(*map(int, input().split()))
