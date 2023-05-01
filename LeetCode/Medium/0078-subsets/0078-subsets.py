class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        def dfs(st_idx, arr):
            answer.append(arr[:])
            if len(arr) == len(nums):
                return
            for i in range(st_idx, len(nums)):
                arr.append(nums[i])
                dfs(i+1, arr)
                arr.pop()

        answer = []
        dfs(0, [])

        return answer