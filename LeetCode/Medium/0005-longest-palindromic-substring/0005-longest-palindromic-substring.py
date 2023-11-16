class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans = ''
        for i in range(len(s)):
            if i+2 <len(s) and s[i] == s[i+2]:
                st=i
                ed=i+2

                while st>=0 and ed<len(s) and s[st] == s[ed]:
                    st-=1
                    ed+=1
                st+=1
                ed-=1
                if ed+1-st > len(ans):
                    print(s[st:ed+1])
                    ans = s[st:ed+1]
            if i+1<len(s) and s[i] == s[i+1]:
                st=i
                ed=i+1

                while st-1>=0 and ed+1<len(s) and s[st-1] == s[ed+1]:
                    
                    st-=1
                    ed+=1

                if ed+1-st > len(ans):
                    ans = s[st:ed+1]
                
        if not ans:
            ans = s[0]


        return ans
            