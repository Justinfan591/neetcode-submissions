class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sort = sorted(nums)
        ans = 1
        temp = 1
        prev = sort[0]
        print(sort)
        for i in range(1, len(sort)): 
            if sort[i] == prev + 1: 
                temp += 1
                prev = sort[i]
            
            elif sort[i] > prev + 1:
                prev = sort[i]
                ans = max(ans, temp)
                temp = 1
           
        ans = max(ans,temp)
        return ans