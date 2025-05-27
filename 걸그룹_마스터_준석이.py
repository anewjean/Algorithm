N, M = map(int, input().split())
groups = {}
# 걸그룹 정보 입력
for _ in range(N):
    group_name = input()
    groups[group_name] = []
    member_num = int(input())
    for _ in range(member_num):
        groups[group_name].append(input())
    groups[group_name].sort()

# 퀴즈 정보 입력
for _ in range(M):
    subject = input()
    quiz_type = int(input())
    
    # 그룹명으로 찾은 멤버 이름 사전순으로 출력하기
    if (quiz_type == 0):
        for member in groups[subject]:
            print(member)
    # 멤버 이름으로 찾은 그룹명 출력하기
    elif (quiz_type == 1):
        for group in groups:
            if subject in groups[group]:
               print(group)
               break
