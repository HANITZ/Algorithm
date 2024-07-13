class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(arr, st_idx):

            if len(arr) == k:
                answer.append(arr[:])
                return
            for i in range(st_idx, n+1):
                arr.append(i)
                dfs(arr, i+1)
                arr.pop()
        
        answer = []
        dfs([], 1)

        return answer