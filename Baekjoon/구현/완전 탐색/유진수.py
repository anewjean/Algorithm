def mul_each_digit(num: str) -> int: 
    answer = 1
    for n in num:
        answer *= int(n)
    return answer 

is_yoojinnum = False
N = input()
for i in range(1, len(N)):
    if (mul_each_digit(N[:i]) == mul_each_digit(N[i:])):
        is_yoojinnum = True
        break

print("YES" if is_yoojinnum else "NO")