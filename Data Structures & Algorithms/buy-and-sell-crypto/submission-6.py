class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []: 
            return 0
        buy = prices[0]
        sell = prices[0]
        best = sell - buy

        for price in prices: 
            best = max(best, price - buy)
            buy = min(buy, price)
                
        return best