class Stack:
    def __init__(self):
        self.stack = []
    
    def order(self, ):
        self.stack = []

    def push(self, X: int) -> None:
        self.stack.append(X)

    def pop(self) -> int: 
        if self.stack:
            print(self.stack.pop())
        else:
            print(-1)

    def size(self) -> int:
        print(len(self.stack))
    
    def empty(self) -> int:
        if self.stack:
            print(0)
        else:
            print(1)

    def top(self) -> int:
        if self.stack:
            print(self.stack[-1])
        else:
            print(-1)
    
stack = Stack()
N = int(input())
for i in range(N):
    query = input()
    if query.startswith("push"):
        stack.push(query.split()[1])
    elif query == "pop":
        stack.pop()
    elif query == "size":
        stack.size()
    elif query == "empty":
        stack.empty()
    elif query == "top":
        stack.top()