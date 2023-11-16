class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        needle_sum = 0
        for nee in needle:
            needle_sum += ord(nee)
        now_sum = 0
        st, ed = 0, 0
        while ed <= len(haystack):
            if now_sum < needle_sum:
                if ed == len(haystack): break
                now_sum+=ord(haystack[ed])
                ed+=1
            elif now_sum > needle_sum:
                now_sum -= ord(haystack[st])
                st+=1
            else:
                if needle == haystack[st:ed]:
                    return st
                elif ed == len(haystack): break
                else:
                    now_sum+=ord(haystack[ed])
                    ed+=1

        return -1

        
        

        return 1