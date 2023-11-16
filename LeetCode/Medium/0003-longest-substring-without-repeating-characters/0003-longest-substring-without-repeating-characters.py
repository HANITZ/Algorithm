from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # for -> O(n)
        ans = 0
        q = deque()
        for ss in s:
            if ss in q:
                ans = max(ans, len(q))
                while ss in q:
                    q.popleft()
                q.append(ss)
            else:
                q.append(ss)
        ans = max(ans, len(q))
        return ans
