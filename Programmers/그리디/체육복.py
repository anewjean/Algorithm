# https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):

    # 여벌 체육복을 가지고 왔지만 도난당한 학생은 데이터셋에서 제외
    lost_set = set(lost)
    reserve_set = set(reserve)
    both = lost_set & lost_reserve
    lost_set -= both
    reserve_set -= both
    
    # 여벌 체육복을 가진 학생 앞, 뒤로 체육복이 없는 학생이 있다면 빌려주기
    for r in sorted(reserve_set): # 오름차순으로 정렬되어있지 않았을 경우를 대비해서 정렬
        if (r - 1) in sorted(lost_set):
            lost_set.remove(r - 1) # r - 1에게 빌렸다면 체육복 없는 학생 목록에서 r - 1 제거
        elif (r + 1) in sorted(lost_set):
            lost_set.remove(r + 1) # r + 1에게 빌렸다면 체육복 없는 학생 목록에서 r + 1 제거
    
    # 아직도 못 빌려서 체육복이 없는 학생 수를 제외한 학생 수 반환
    return n - lost_set