class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] == -nums[k]
        # if too big we 
        # sort them so the first example becomes
        # [-4, -1, -1, 0, 1, 2]
        # we first use -4 and 2 and goes inside to check over the array
        # Under what condition do we increment left pointer and what condition we increment right pointer? 
        nums.sort()
        ans = []

        for i in range(len(nums) - 2): 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right: 
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum > 0: 
                    right -= 1
                elif current_sum < 0: 
                    left += 1
                else: #found it
                    ans.append((nums[i],nums[left], nums[right]))

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]: 
                        right -= 1
                
        return ans

            
