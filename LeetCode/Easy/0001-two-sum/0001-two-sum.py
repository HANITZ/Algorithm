from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        

        for i in range(len(nums)):
            need = target-nums[i]
            if need in dic:
                return [dic[need], i]
            else:
                dic[nums[i]] = i

        
                