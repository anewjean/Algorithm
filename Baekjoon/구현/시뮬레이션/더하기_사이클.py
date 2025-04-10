# 주어진 숫자의 각 자리 수를 더해 임시로 숫자를 만든다
# 주어진 숫자의 뒷자리와 새로운 숫자의 뒷자리를 이어붙여 또다른 새로운 숫자를 만든다.
# 처음 주어진 수자와 같아질 때까지 1, 2번을 반복한다. 

N = int(input())

cycle = 0
def find_cycle(num):
    global cycle

    temp = (num // 10) + (num % 10)
    new_num = int(str(num % 10) + str(temp % 10))
    cycle += 1

    if new_num == N:
        return cycle
    else:
        find_cycle(new_num) 

find_cycle(N)
print(cycle)