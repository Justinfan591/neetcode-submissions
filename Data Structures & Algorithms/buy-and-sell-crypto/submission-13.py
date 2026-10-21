class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        buy = float('inf')

        for price in prices: 
            buy = min(buy, price)
            best = max(best, price - buy)

        return best