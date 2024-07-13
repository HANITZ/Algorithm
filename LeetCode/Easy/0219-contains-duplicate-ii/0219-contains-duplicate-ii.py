class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in dic:
                if abs(dic[nums[i]]-i) <= k:
                    return True
                else:
                    dic[nums[i]] = i
            else:
                dic[nums[i]] = i
        return False