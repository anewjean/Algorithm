class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(",  "]": "[", "}": "{"}

        for p in s:
            if p in pairs.values():
                stack.append(p)
            elif p in pairs.keys():
                if not stack or stack.pop() != pairs[p]:
                    return False
        if stack:
            return False
        return True