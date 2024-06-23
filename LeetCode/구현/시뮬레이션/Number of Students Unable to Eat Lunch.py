class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 학생들의 선호도 카운트
        count = [students.count(0), students.count(1)]
        
        for sandwich in sandwiches:
            if count[sandwich] > 0:
                count[sandwich] -= 1
            else:
                # 더 이상 선호하는 학생이 없으면 종료
                break
        
        # 남아 있는 학생 수를 반환
        return sum(count)