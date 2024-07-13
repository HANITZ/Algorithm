class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = collections.defaultdict(int)

        for num in nums:
            num_dict[num] +=1
        
        _max = -1
        max_idx = -1
        for key, value in num_dict.items():
            if value > _max:
                _max = value
                max_idx = key
        return max_idx