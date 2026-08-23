# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, node, low, high): 
        if not node: 
            return True

        if node.val <= low:
            return False

        if node.val >= high: 
            return False
        
        return self.valid(node.left,low,node.val) and self.valid(node.right, node.val, high)
        

