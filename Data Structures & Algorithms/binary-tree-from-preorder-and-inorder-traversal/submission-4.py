class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val: i for i, val in enumerate(inorder)}
        self.pre = 0
        
        def build(left, right):
            if left > right:
                return None
            
            val = preorder[self.pre]
            self.pre += 1
            
            node = TreeNode(val)
            mid = idx[val]
            
            node.left  = build(left, mid - 1)
            node.right = build(mid + 1, right)
            
            return node
        
        return build(0, len(inorder) - 1)