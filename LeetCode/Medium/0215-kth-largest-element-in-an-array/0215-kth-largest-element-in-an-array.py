from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heappush(heap, -n)
        for _ in range(1, k):
            heappop(heap)
        return -heappop(heap)