class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(arr, _set):

            if len(arr) == n:
                answer.append(arr[:])
                return
            
            for num in nums:
                if num in _set: continue
                arr.append(num)
                _set.add(num)
                dfs(arr, _set)
                arr.pop()
                _set.remove(num)
        
        answer = []
        n = len(nums)
        dfs([], set())
        return answer


        
        