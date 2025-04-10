import sys

N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

count = 0

def dfs(index, total):
    global count
    # 종료 조건 (수열 끝까지 탐색)
    if index == N:
        return

    # 현재 숫자를 포함한 경우의 합 계산
    total += numbers[index]

    # 부분수열의 합이 S가 되면 count 증가
    if total == S:
        count += 1

    # 현재 숫자를 선택한 경우
    dfs(index + 1, total)

    # 현재 숫자를 선택하지 않은 경우 (백트래킹)
    dfs(index + 1, total - numbers[index])

dfs(0, 0)

print(count)