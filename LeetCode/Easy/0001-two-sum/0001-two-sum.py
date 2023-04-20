from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        traces = defaultdict(int)

        for i, num1 in enumerate(nums):
            remain = target - num1
            if remain in traces:
                return [i, traces[remain]]
            traces[num1] = i
            
                