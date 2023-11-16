class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        _min = 10**4
        for price in prices:
            if _min > price:
                _min = price
            else:
                answer = max(answer, price - _min)
        return answer
        