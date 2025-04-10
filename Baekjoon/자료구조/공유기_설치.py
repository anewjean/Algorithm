N, C = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)]) # 집들의 좌표

def can_install(distance: int) -> bool:
    """
    주어진 distance의 간격을 두고 C개의 공유기 설치가 가능한지 판별
    """
    installed_house = houses[0]
    count = 1

    for i in range(1, N):
        if houses[i] - installed_house >= distance:
            count += 1
            installed_house = houses[i]
    return count >= C

# 공유기간 거리를 이분탐색
min_distance, max_distance = 1, houses[-1] - houses[0]
result = 0

while min_distance <= max_distance:
    mid = (min_distance + max_distance) // 2
    if can_install(mid):
        result = mid # 가능한 거리는 저장하고 확장
        min_distance = mid + 1
    else:
        max_distance = mid - 1
  
print(result)
