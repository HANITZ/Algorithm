class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        n = len(s)
        index= 0
        for ch in t:
            if index == n: return True
            if s[index] == ch:
                index+=1
        if index == n:
            return True
        else:
            return False