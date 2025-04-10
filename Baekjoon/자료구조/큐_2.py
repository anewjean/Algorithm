from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()

    def push(self, X: int) -> None:
        self.deque.append(X)

    def pop(self) -> int: 
        if self.deque:
            print(self.deque.popleft())
        else:
            print(-1)

    def size(self) -> int:
        print(len(self.deque))
    
    def empty(self) -> int:
        if self.deque:
            print(0)
        else:
            print(1)

    def front(self) -> int:
        if self.deque:
            print(self.deque[0])
        else:
            print(-1)
    
    def back(self) -> int:
        if self.deque:
            print(self.deque[-1])
        else:
            print(-1)
    
deque = Deque()
N = int(input())
for i in range(N):
    query = input()
    if query.startswith("push"):
        deque.push(int(query.split()[1]))
    elif query == "pop":
        deque.pop()
    elif query == "size":
        deque.size()
    elif query == "empty":
        deque.empty()
    elif query == "front":
        deque.front()
    elif query == "back":
        deque.back()