class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(' ')
        if len(pattern) != len(arr):
            return False

        dic = {}
        checked = []
        index=0
        for i in range(len(arr)):
            if not pattern[i] in dic:
                dic[pattern[i]] = index
                if arr[i] in checked:
                    return False
                checked.append(arr[i])
                index+=1
            else:
                if checked[dic[pattern[i]]] != arr[i]:
                    return False

        return True