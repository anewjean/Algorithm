from collections import deque

n = int(input())
stones = list(map(int, input().split()))
s, e = map(int, input().split())
s -= 1
e -= 1

dist = [False] * n   # 최소 점프 횟수 저장
dist[s] = 0

q = deque([s])

while q:
    cur = q.popleft()
    step = stones[cur]

    # 앞으로 점프
    nxt = cur + step
    while nxt < n:
        if not dist[nxt]:         # 아직 방문 안 했으면
            dist[nxt] = dist[cur] + 1
            q.append(nxt)
        nxt += step                 # 배수만큼 계속 점프 가능

    # 뒤로 점프
    nxt = cur - step
    while nxt >= 0:
        if not dist[nxt]:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)
        nxt -= step

print(dist[e])
