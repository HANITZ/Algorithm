class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        _min = 10**4
        for price in prices:
            if _min > price:
                _min = price
            else:
                profit = max(profit, price - _min)
        return profit
        