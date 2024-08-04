import bisect

# 입력 받기
N = int(input())
ns = sorted(map(int, input().split()))
M = int(input())
ms = list(map(int, input().split()))

# 이분 탐색을 통해 각 ms의 값을 ns에서 찾기
for val in ms:
    # bisect_left로 val의 삽입 위치를 찾음
    index = bisect.bisect_left(ns, val)
    # index가 ns 길이 내에 있고, ns[index]가 val과 같은지 확인
    if index < N and ns[index] == val:
        print(1, end = " ")
    else:
        print(0, end = " ")