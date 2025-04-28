import sys
input = sys.stdin.readline

N = int(input())
ingredients = [] 

for _ in range(N):
    s, b = map(int, input().split())
    ingredients.append((s, b))

ans = float('inf')

# 전체 케이스를 탐색하기 위한 루프
for mask in range(1, 1 << N): # mask는 선택/미선택 표시(예: mask값이 3일 때 000~111
    mul, summ = 1, 0
    m = mask
    idx = 0

    # mask의 1비트 개수 만큼만 도는 루프
    while m:               
        if m & 1: # 현재 idx에서 m의 마지막 비트가 1이면 현재 재료 선택(m을 10진수 리터럴로 써도 내부적으로 2진수 비트 연산 가능) 
            s, b = ingredients[idx][0], ingredients[idx][1]
            mul *= s
            summ += b
        idx += 1
        m >>= 1 # m을 오른쪽으로 한 칸 시프트 => m /= 2

    ans = min(ans, abs(mul - summ))
print(ans)