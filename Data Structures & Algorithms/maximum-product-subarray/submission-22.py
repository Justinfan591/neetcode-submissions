class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #get initial mini and maxi
        mini=maxi=best=nums[0]

        for n in nums[1:]: 
            new_maxi = max(n, maxi*n, mini*n)
            new_mini = min(n, mini*n, maxi*n)
            mini = new_mini
            maxi = new_maxi
            best = max(best, new_maxi)

        return best