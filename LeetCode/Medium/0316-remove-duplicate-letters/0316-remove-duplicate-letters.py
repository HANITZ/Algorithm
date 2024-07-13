class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = collections.Counter(s)
        stack = []
        _set = set()
        for ss in s:
            counts[ss] -= 1
            if ss in _set:
                continue
            while stack and ss < stack[-1] and counts[stack[-1]] > 0 :
                _set.remove(stack.pop())

            stack.append(ss)
            _set.add(ss)
        
        return ''.join(stack)