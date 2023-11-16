class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ss = collections.defaultdict(list)
        tt = collections.defaultdict(list)
        for i,ch in enumerate(s):
            ss[ch].append(i)
        for i,ch in enumerate(t):
            tt[ch].append(i)
        s_li = sorted(ss.values())
        t_li = sorted(tt.values())
        

        return s_li == t_li
