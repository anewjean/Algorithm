p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for _ in range(90):
    p.append(p[-2] + p[-3])
        
t = int(input())
for _ in range(t):
    n = int(input())
    print(p[n-1])