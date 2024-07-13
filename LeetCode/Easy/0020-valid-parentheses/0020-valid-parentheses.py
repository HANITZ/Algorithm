class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ss in s:
            if ss == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif ss == "}": 
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif ss == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ss)
        if stack:
            return False
        return True