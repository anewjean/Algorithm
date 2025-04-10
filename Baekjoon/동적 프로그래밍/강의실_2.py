# 최대한 적은 수의 강의실 사용해서 모든 강의가 이루어지도록!
# 한 강의의 종료시간과 다른 강의의 시작시간이 겹치는 것은 상관 없음
# 최소 강의실 수 K, 각 강의마다 강의실 배정 

# 강의실 수가 최소가 되려면?
# 각 강의에 배정할 강의실 번호를 순서대로 출력

# 끝나는 순서대로 정렬
import heapq
import sys

input = sys.stdin.readline

N = int(input())
lectures = []

for _ in range(N):
    num, start, end = map(int, input().split())
    lectures.append((start, end, num))

lectures.sort()  # 시작시간 기준으로 정렬

rooms = []  # (종료시간, 강의실번호)
heapq.heapify(rooms)

assigned = [0] * (N + 1)  # 강의 번호별 강의실 번호 저장

room_count = 0

for start, end, num in lectures:
    if rooms and rooms[0][0] <= start:
        # 가장 빨리 끝나는 강의실을 재사용
        earliest_end, room_num = heapq.heappop(rooms)
    else:
        # 강의실 추가
        room_count += 1
        room_num = room_count

    heapq.heappush(rooms, (end, room_num))
    assigned[num] = room_num

print(room_count)
for i in range(1, N + 1):
    print(assigned[i])