class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        if len(nums) == 0:
            return []
        rob1, rob2 = 0,0
        rob1_2,rob2_2 = 0,0
        num1 = nums[0:len(nums)-1]
        num2 = nums[1:]

        for n in num1: 
            temp = max(n + rob1, rob2)
            rob1=rob2
            rob2=temp
        for n in num2: 
            temp = max(n + rob1_2, rob2_2)
            rob1_2=rob2_2
            rob2_2=temp

        return max(rob2,rob2_2)