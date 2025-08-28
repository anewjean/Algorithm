A, B = map(int, input().split())

def b_to_a(a, b):
    # 바닥조건
    if a == b:
        return 1 # +1 해서 반환해야 하니까 0 + 1
    if b < a:
        return -1
    
    # 연산이 가능한 경우
    if b % 10 == 1:
        cnt = b_to_a(a, b // 10)
        return cnt + 1 if cnt != -1 else -1
    if b % 2 == 0:
        cnt = b_to_a(a, b // 2)
        return cnt + 1 if cnt != -1 else -1
    
   # 아무 조건에 해당하지 않으면 실패 
    return -1

print(b_to_a(A, B))