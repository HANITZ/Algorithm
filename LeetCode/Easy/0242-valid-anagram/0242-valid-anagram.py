class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_dic = {}
        s_dic = {}
        for ch in s:
            if ch in s_dic:
                s_dic[ch] += 1
            else:
                s_dic[ch] = 1
        for ch in t:
            if ch in t_dic:
                t_dic[ch] +=1
            else:
                t_dic[ch] = 1
            
            if not ch in s_dic or s_dic[ch] == 0:
                return False
            s_dic[ch]-=1
        
        for ch in s:
            if not ch in t_dic or t_dic[ch] == 0:
                return False
            t_dic[ch]-=1
            
            
        return True
