class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #run left and then right
        ans = [1] * len(nums)
        arr1 = [1] * len(nums)
        arr2 = [1] * len(nums)

        #left run first
        curr = 1
        for i in range(1,len(nums)): 
            arr1[i] = nums[i-1] * curr
            curr = nums[i-1] * curr
        
        #right run now
        curr = 1
        for i in range(1,len(nums)): 
            arr2[len(nums)- i - 1] = nums[len(nums)-i] * curr
            curr = nums[len(nums) - i] * curr
        
        for i in range(len(nums)): 
            ans[i] = arr1[i] * arr2[i]
        
        return ans
        


                
        