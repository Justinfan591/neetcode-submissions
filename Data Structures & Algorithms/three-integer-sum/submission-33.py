class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = [] 
        ordered = sorted(nums) # nlogn

        for i in range(0,len(ordered)-2):
            # two pointers, l, r 
            l = i + 1 # the next index for i
            r = len(ordered) - 1 # last index 
            if i > 0 and ordered[i] == ordered[i - 1]: 
                continue
            while l < r: 
                total = ordered[i] + ordered[l] + ordered[r] #sum of the three 
                if total < 0: 
                    l += 1
                elif total > 0: 
                    r -= 1
                else: # when total == 0
                    ans.append([ordered[i], ordered[l], ordered[r]])
                    while l < r and ordered[l] == ordered[l + 1]: 
                        l += 1
                    while l < r and ordered[r] == ordered[r - 1]: 
                        r -= 1  
                    l += 1
                    r -= 1
                        
            
        return ans

            
