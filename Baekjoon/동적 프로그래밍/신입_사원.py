def hire(employees: list):
    employees.sort()
    count = 1
    best_interview = employees[0][1]

    for i in range(1, len(employees)):
        if employees[i][1] < best_interview:
            count += 1
            best_interview = employees[i][1]
    
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    employees = [tuple(map(int, input().split())) for _ in range(N)]
    print(hire(employees))