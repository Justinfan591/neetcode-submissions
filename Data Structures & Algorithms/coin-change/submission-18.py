
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        maxi = 200000
        memo = {}
        def dfs(num): 
            #base case
            if num in memo: 
                return memo[num]
            if num == 0: 
                return 0
            if num < 0: 
                return maxi
            
            best = maxi
            for coin in coins: 
                best = min(best, dfs(num - coin) + 1)
            memo[num] = best
            return best

        return -1 if dfs(amount) == 200000 else dfs(amount)
                