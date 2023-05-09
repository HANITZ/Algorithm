class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1, l2, p1, p2 = len(haystack), len(needle), 0, 0
        while p1<l1:
            if p2==l2:
                return p1-l2
            if haystack[p1]==needle[p2]:
                p2 += 1
            else:
                p1 = p1 - p2
                p2 = 0
            p1 += 1
        if p2==l2:
            return l1-l2
        return -1