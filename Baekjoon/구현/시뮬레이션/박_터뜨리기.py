# 최소로 필요한 공 개수
    # 1+2+...+k 
    # k가 짝수일 때 점화식: (k+1)*(k//2)
    # k가 홀수일 때 점화식: (k+1)*(k//2)+(k+1)//2
n, k = map(int, input().split())
if k % 2 == 0:
    std = (k + 1) * (k // 2)
else: 
    std = (k + 1) * (k // 2) + (k + 1) // 2
    
if n < std:
    print(-1)
else:
    remain = n - std
    if remain % k == 0:
        print(k - 1)
    else:
        print(k)