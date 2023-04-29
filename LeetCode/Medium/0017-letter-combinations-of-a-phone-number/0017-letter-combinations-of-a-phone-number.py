class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def dfs(level, arr):
            if level == n:
                answer.append(''.join(arr))
                return

            key = digits[level]
            for digit in digits_dic[key]:
                arr.append(digit)
                dfs(level+1, arr)
                arr.pop()
        
        
        answer = []
        if not digits:
            return answer
        digits_dic = {}
        
        asc = 97
        num = 2
        for i in range(2, 10):
            digits_dic[str(i)] = []
            for _ in range(3):
                digits_dic[str(i)].append(chr(asc))
                asc+=1
            if i == 9 or i == 7:
                digits_dic[str(i)].append(chr(asc))
                asc+=1
        
        n = len(digits)
        dfs(0, [])
            


        return answer