class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans  = 0
        if len(nums) == 0:
            return 0

        for num in numSet: 
            if (num - 1) not in numSet: 
                curr_len = 1 
                while (num + curr_len) in numSet: 
                    curr_len += 1
                ans = max(ans, curr_len)
        return ans
    