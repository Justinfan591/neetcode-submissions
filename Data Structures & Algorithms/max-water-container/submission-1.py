class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #2 pointers problem 
        # we can get the highest so far
        # we can actually ignore all the bars lower or equal in later positions
        # min(pos1,pos2) * (pos2-pos1)
        pos1 = 0
        pos2 = len(heights) - 1
        ans = 0
        while(pos2>pos1): 
            cur = min(heights[pos1],heights[pos2]) * (pos2-pos1)
            ans = max(cur, ans)
            if heights[pos1] > heights[pos2]: 
                pos2 -=1
            else: pos1 += 1
        return ans