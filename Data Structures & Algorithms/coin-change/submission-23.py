
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}

        def minFlip(target): 
            #base cases
            if target in memo: 
                return memo[target]
            best = float('inf')
            for coin in coins: 
                remain = target - coin
                if remain >= 0: 
                    best = min(best, minFlip(remain) + 1)
            memo[target] = best
            return best

        res = minFlip(amount)
        
        if res != float('inf'):
            return res
        else: return -1
        
            
                