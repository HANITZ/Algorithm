class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 1: return [str(nums[0])]
        answer = []
        st = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                if i != st+1:
                    answer.append(str(nums[st]) + '->' + str(nums[i-1]))
                else:
                    answer.append(str(nums[st]))
                st = i
            if i == len(nums)-1:
                if i != st:
                    answer.append(str(nums[st]) + '->' + str(nums[i]))
                else:
                    answer.append(str(nums[st]))

        return answer
                




        