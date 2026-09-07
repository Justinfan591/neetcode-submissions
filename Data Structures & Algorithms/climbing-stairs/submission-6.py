class Solution:
    ans = {}
    def climbStairs(self, n: int) -> int:
        #base case
        if n in self.ans: 
            return self.ans[n]
        if n<0: 
            return 0
        if n == 0: 
            return 1
        add = self.climbStairs(n-1)+ self.climbStairs(n-2)
        self.ans[n] = add
        return add