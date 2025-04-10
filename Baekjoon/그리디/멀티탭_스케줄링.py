# 이미 꽂혀 있으면 패스
# 빈 자리가 있으면 꽂음
# 빈 자리가 없고, 다 꽉 찼으면:
 # 앞으로 안 쓰는 전기용품이 있으면 그걸 뽑고 교체
 # 다 앞으로 또 쓸 거면, 가장 나중에 다시 쓸 전기용품을 뽑음

def multitap(N: int, K: int, order: list):
    plugs = set()
    count = 0

    for i in range(K):
        current = order[i]

        if current in plugs:
            continue

        # 꽂기
        if len(plugs) < N:
            plugs.add(current)
            continue

        # 뽑기
        latest_use = -1
        to_remove = None

        for p in plugs:
            try:
                next_use = order[i+1:].index(p)
            except ValueError:
                next_use = float('inf')
            
            if next_use > latest_use:
                latest_use = next_use
                to_remove = p
    
        plugs.remove(to_remove)
        plugs.add(current)
        count += 1
    
    return count

N, K = map(int, input().split())
order = list(map(int, input().split()))
print(multitap(N, K, order))