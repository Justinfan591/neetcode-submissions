class Solution:
    def trap(self, height: List[int]) -> int:
        # Idea is to keep max in the lsit
        # have it stored but only add when hit another height
        # do I need to store second highest? Yes
        # two pointer
        if len(height) <=2:
            return 0
        leftMax, rightMax, ans, l, r =0, 0, 0, 0, len(height) - 1
        
        while l <= r: 
            l_val, r_val = height[l], height[r]
            if l_val < r_val: 
                if l_val > leftMax: 
                    leftMax = l_val
                elif l_val <= leftMax:
                    ans += (leftMax - l_val)
                l+=1 
            elif l_val >= r_val: 
                if r_val >= rightMax: 
                    rightMax = r_val
                elif r_val <= rightMax: 
                    ans += (rightMax - r_val)
                r-=1
            
        return ans