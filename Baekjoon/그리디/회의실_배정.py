# 끝나는 시간이 빠를수록 유리하다!

# 1. 회의 끝나는 시간 기준으로 정렬 
# 2. 매순간, '가장 먼저 끝나는' 회의부터 선택
# 3. 다음 회의는 이전 회의 끝난 시간보다 같거나 큰 것 중 '가장 먼저 끝나는' 회의 선택
            
N = int(input())
schedules = [tuple(map(int, input().split())) for _ in range(N)]
answer = 0
end_time = 0
schedules.sort(key=lambda x: (x[1], x[0]))

for start, end in schedules:
    if start >= end_time:
        answer += 1
        end_time = end

print(answer)