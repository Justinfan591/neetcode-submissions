class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        best = 0

        for price in prices: 
            best = max(best, price - buy)
            buy = min(buy, price)
                
        return best