class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeros = 0
        location = 0
        res = []
        for i in range(len(nums)): 
            if nums[i] == 0: 
                zeros += 1
                location = i
            else: total = total * nums[i]
        
        #if more than 2 zeros, whole string would be 0
        for i in range(len(nums)): 
            if zeros >=2:
                res.append(0)
            elif zeros == 1: 
                if i != location:
                    res.append(0)
                else: res.append(total)
            elif zeros == 0:
                res.append(total//nums[i])
        
        return res
                
        