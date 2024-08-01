n = int(input())
coords = []
coords_x = []
coords_y = []
answer = [-1] * n

for _ in range(n):
    x, y = map(int, input().split())
    coords.append((x, y))
    coords_x.append(x)
    coords_y.append(y)

# 만날 장소 정하기
for y in coords_y:
    for x in coords_x:
        dist = []
        
        # 각 좌표에서 만날 장소로 오는 비용 계산하기
        for ex, ey in coords:
            d = abs(ex - x) + abs(ey - y)
            dist.append(d)
            
        # 가까운 순서대로 정렬
        dist.sort()
        tmp = 0
        for i in range(len(dist)):
            d = dist[i]
            tmp += d
            if answer[i] == -1:
                answer[i] = tmp
            else:
                answer[i] = min(tmp, answer[i])

print(*answer)