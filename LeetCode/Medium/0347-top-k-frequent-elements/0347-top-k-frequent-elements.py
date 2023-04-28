from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        nums_counts = collections.Counter(nums)
        heap = []
        for key, val in nums_counts.items():
            heappush(heap, (-val, key))
        
        for _ in range(k):
            answer.append(heappop(heap)[1])
        return answer