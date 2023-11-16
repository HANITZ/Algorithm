class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        l, r = 1, 1
        for i in range(len(nums)):
            answer[i] *= l
            answer[len(nums)-1-i] *= r
            l, r = l*nums[i], r*nums[len(nums)-1-i]
        return answer