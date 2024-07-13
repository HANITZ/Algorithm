class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        answer = ''
        min_len = len(min(strs, key=len))
        print(min_len)
        idx = 0
        while idx<min_len:
            
            flag = 0
            for str in strs:
                if answer+strs[0][idx] != str[:idx+1]:
                    flag=1
            if flag:
                break
            answer+= strs[0][idx]
            idx+=1
        return answer
        