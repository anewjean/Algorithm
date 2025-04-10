N, M = map(int, input().split())
trees = list(map(int, input().split()))
tree_max_len = max(trees)

def cut_trees() -> int:
    end = tree_max_len
    start = 0
    
    while start <= end:
        yields = 0
        h = (end + start) // 2
        for tree in trees:
            if tree > h:
                yields += (tree - h)
        if yields > M:
            start = h + 1
        elif yields == M:
            return h
        else:
            end = h - 1
    return end

print(cut_trees())

    # mid값으로 잘라보고 잘린 값들의 합이 M이면 바로 반환
    # mid값으로 잘라보고 잘린 값들의 합이 M보다 크면 mid를 높인다.
    # mid값으로 잘라보고 잘린 값들의 합이 M보다 작으면 mid를 낮춘다.
    # mid를 tree_max_len 안에서 이분탐색으로 찾기!