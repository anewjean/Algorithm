class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 연산자 람다함수
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }
        
        stack = []
        
        for token in tokens:
            if token in ops:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[token](b, a))
            else:
                stack.append(int(token))
                
        return stack[-1]
