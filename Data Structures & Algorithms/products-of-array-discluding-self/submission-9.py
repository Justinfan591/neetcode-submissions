class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #iterate twice
        n = len(nums)
        res = [1] * n
        prefix, posfix= 1,1
        for i in range(n):
            res[i] = res[i] * prefix
            prefix = prefix * nums[i]
        for i in range(n): 
            res[n-i-1] = res[n-i-1] * posfix
            posfix = posfix * nums[n-i-1]
        return res

                
        