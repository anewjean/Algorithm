import sys
input = sys.stdin.readline

n = int(input().rstrip())
in_ = list(input().rstrip() for _ in range(n))
out = list(input().rstrip() for _ in range(n))

gone = set()
head = 0
answer = 0

for car in out:
    while head < n and in_[head] in gone:
        head += 1
    
    if head < n and in_[head] == car:
        head += 1
    else:
        answer += 1
        gone.add(car)
        
print(answer)