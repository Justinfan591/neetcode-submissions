# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr, lower, upper): 
            #base case
            if curr is None: 
                return True
            if curr.val <= lower or curr.val >= upper: 
                return False 
            #pass to left and right children
            return dfs(curr.left, lower, curr.val) and dfs(curr.right, curr.val, upper)
        
        return dfs(root, float('-inf'), float('inf'))