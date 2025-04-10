import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 1. x좌표 기준 정렬
points.sort()


def distance(p1, p2):
    """두 점 사이 거리의 제곱 (루트 안 씀)"""
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def solve(start, end):
    """points[start:end] 구간에서 가장 가까운 거리^2 반환"""
    length = end - start

    # 2. 점이 3개 이하일 경우 직접 계산
    if length <= 3:
        min_dist = float('inf')
        for i in range(start, end):
            for j in range(i + 1, end):
                min_dist = min(min_dist, distance(points[i], points[j]))
        return min_dist

    # 3. 분할
    mid = (start + end) // 2
    mid_x = points[mid][0]

    d_left = solve(start, mid)
    d_right = solve(mid, end)
    d = min(d_left, d_right)

    # 4. 병합 - 경계 근처 strip 만들기
    strip = []
    for i in range(start, end):
        if (points[i][0] - mid_x) ** 2 < d:
            strip.append(points[i])

    # 5. y좌표 기준 정렬 (strip 내에서만)
    strip.sort(key=lambda p: p[1])

    # 6. strip 내에서 가장 가까운 거리 찾기 (최대 6개만 확인)
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) ** 2 >= d:
                break
            d = min(d, distance(strip[i], strip[j]))

    return d


# 실행
print(solve(0, n))