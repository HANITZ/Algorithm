class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        ans = ''
        for ss in s:
            if ss.isalnum():
                ans+=ss
        st, ed = 0, len(ans)-1
        while st <= ed:
            if ans[st] != ans[ed]:
                return False
            st+=1
            ed-=1
        return True
