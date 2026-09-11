class Solution:
    def rob(self, nums: List[int]) -> int:
        best_two_back, best_one_back = 0, 0 #did I rob 1 and did I rob 2?
        for n in nums: 
            temp = max(best_two_back + n, best_one_back )
            best_two_back = best_one_back #move right for one
            best_one_back  = temp #current max 
        return best_one_back