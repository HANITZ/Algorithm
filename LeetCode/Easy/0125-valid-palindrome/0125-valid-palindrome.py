class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ''
        for ch in s:
            if ch.isalnum():
                strs+=ch
        strs = strs.lower()
        st, ed = 0, len(strs)-1
        if len(strs) % 2 :
            while st != ed:
                if strs[st] != strs[ed]:
                    return False
                st+=1
                ed-=1
        else:
            while st < ed:
                if strs[st] != strs[ed]:
                    return False
                st+=1
                ed-=1
        return True

        