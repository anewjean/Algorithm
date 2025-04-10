A, B, C = map(int, input().split())

def power(a, b, c):
    if b == 0:
        return 1
    elif b == 1:
        return a % c
    elif B % 2 == 0:
        return ((power(a, b // 2, c)**2) % c)
    else:
        return ((power(a, b // 2, c)**2) * a % c)
    
print(power(A, B, C))