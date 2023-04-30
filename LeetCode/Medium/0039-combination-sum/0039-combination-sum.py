class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(_sum , arr, st_idx):
            if _sum == target:
                answer.append(arr[:])
                return

            for i in range(st_idx, len(candidates)):
                if _sum + candidates[i] <=target:
                    arr.append(candidates[i])
                    dfs(_sum+candidates[i], arr, i)
                    arr.pop()
        
        answer = []
        dfs(0, [], 0)

        return answer