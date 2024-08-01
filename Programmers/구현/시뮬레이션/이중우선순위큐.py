import heapq

def solution(operations):
    queue = []
    for i in operations:
        operator, num = i.split()
        num = int(num)

        if operator == 'I':
            heapq.heappush(queue, num) 
        elif operator == 'D' and num == -1:
            if queue:
                heapq.heappop(queue)
        else:
            if queue:
                queue.remove(max(queue))
    
    if queue:
        return [max(queue), heapq.heappop(queue)]
    else:
        return [0, 0]