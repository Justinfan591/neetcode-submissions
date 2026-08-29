class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # similar to the last question but we track each node and set boundaries
        res = []
        subset = []

        def dfs(i, total): 
            if i >= len(nums) or total >= target: 
                if total == target: 
                    res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i, total + nums[i])
            subset.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res