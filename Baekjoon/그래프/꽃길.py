
N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1] 
answer = float('inf')

def calc_cost(case: list) -> int:
    answer = 0
    flowers = []

    for i in case:
        x = i // N
        y = i % N
        if (x == 0) or (x == N - 1) or (y == 0) or (y == N - 1):
            return float('inf')
        for d in range(5):
            flowers.append((x + dx[i], y + dy[i]))
            answer += ground[x + dx[i]][y + dy[i]]

    if len(set(flowers)) != 15:
        return float('inf')

    return answer

for i in range(N ** 2):
    for j in range(i + 1, N ** 2):
        for k in range(j + 1, N ** 2):
            answer = min(answer, calc_cost([i, j, k]))

print(answer)